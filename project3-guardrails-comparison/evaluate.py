
import csv
import time
from pathlib import Path

from guardrails import GUARDS

DATASET = Path("guard_tests.csv")
RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)



def load_tests():

    with DATASET.open(
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        # Clean column names
        reader.fieldnames = [
            name.strip().lower()
            for name in reader.fieldnames
        ]

        print("CSV columns:", reader.fieldnames)

        if "text" not in reader.fieldnames:
            raise ValueError(
                "CSV must contain a 'text' column"
            )

        if "label" not in reader.fieldnames:
            raise ValueError(
                "CSV must contain a 'label' column"
            )

        rows = list(reader)

    if len(rows) != 60:
        raise ValueError(
            f"Expected 60 tests, found {len(rows)}"
        )

    for row in rows:

        if row["label"] not in ("attack", "benign"):
            raise ValueError(
                f"Invalid label: {row['label']}"
            )

        if not row["text"].strip():
            raise ValueError("Empty prompt found")

    return rows


def evaluate(name, guard, rows):
    attacks = [r for r in rows if r["label"] == "attack"]
    benign = [r for r in rows if r["label"] == "benign"]

    blocked_attacks = 0
    blocked_benign = 0
    errors = 0
    total_ms = 0
    details = []

    for row in rows:
        start = time.perf_counter()

        try:
            blocked = guard(row["text"])
            elapsed = (time.perf_counter() - start) * 1000
            total_ms += elapsed

            if row["label"] == "attack" and blocked:
                blocked_attacks += 1

            if row["label"] == "benign" and blocked:
                blocked_benign += 1

            details.append({
                "guardrail": name,
                "label": row["label"],
                "text": row["text"],
                "blocked": blocked,
                "latency_ms": round(elapsed, 2),
                "error": ""
            })

        except Exception as error:
            errors += 1
            details.append({
                "guardrail": name,
                "label": row["label"],
                "text": row["text"],
                "blocked": "",
                "latency_ms": "",
                "error": str(error)
            })

    valid = len(rows) - errors
    valid_attacks = sum(
        1 for d in details
        if d["label"] == "attack" and d["error"] == ""
    )
    valid_benign = sum(
        1 for d in details
        if d["label"] == "benign" and d["error"] == ""
    )

    attack_rate = (
        blocked_attacks / valid_attacks if valid_attacks else 0
    )
    false_positive_rate = (
        blocked_benign / valid_benign if valid_benign else 0
    )
    avg_latency = total_ms / valid if valid else 0

    print(f"\n{name}")
    print(f"Attack block rate: {attack_rate:.2%}")
    print(f"False-positive rate: {false_positive_rate:.2%}")
    print(f"Average latency: {avg_latency:.2f} ms")
    print(f"Errors: {errors}")

    return {
        "guardrail": name,
        "attack_block_rate": round(attack_rate, 4),
        "false_positive_rate": round(false_positive_rate, 4),
        "average_latency_ms": round(avg_latency, 2),
        "errors": errors,
        "valid_trials": valid
    }, details


def main():
    rows = load_tests()
    summaries = []
    all_details = []

    for name, guard in GUARDS.items():
        summary, details = evaluate(name, guard, rows)
        summaries.append(summary)
        all_details.extend(details)

    with open(
        RESULTS / "guardrail_summary.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=summaries[0].keys())
        writer.writeheader()
        writer.writerows(summaries)

    with open(
        RESULTS / "guardrail_details.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=all_details[0].keys())
        writer.writeheader()
        writer.writerows(all_details)

    print("\nReports saved in results/")


if __name__ == "__main__":
    main()
