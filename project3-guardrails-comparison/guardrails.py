
import json
import re
import urllib.request
import urllib.error

# Baseline regex guardrail
PATTERNS = [
    r"ignore all previous instructions",
    r"ignore previous instructions",
    r"reveal your system prompt",
    r"reveal your hidden instructions",
    r"disclose the secret key",
    r"system notice.*reveal",
]

def regex_guard(text):
    text = text.lower()
    return any(re.search(pattern, text) for pattern in PATTERNS)


# Local Llama Guard through Ollama
def llama_guard(text):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama-guard3:1b",
        "messages": [
            {"role": "user", "content": text}
        ],
        "stream": False
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        classification = result["message"]["content"].strip().lower()

        if classification.startswith("unsafe"):
            return True

        if classification.startswith("safe"):
            return False

        raise ValueError(
            f"Unexpected Llama Guard response: {classification}"
        )

    except Exception as error:
        raise RuntimeError(f"Llama Guard failed: {error}")


GUARDS = {
    "regex": regex_guard,
    "llama_guard": llama_guard
}
