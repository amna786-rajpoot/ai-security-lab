
# Project 3: AI Guardrails Comparison

A beginner-friendly AI security project that compares rule-based and classifier-based guardrails using Python and Ollama.

## Project Objective

The objective is to measure how effectively different guardrail approaches detect malicious prompts while minimizing false positives on legitimate user requests.

## Guardrails Compared

### 1. Regex Guardrail

A rule-based approach that detects predefined suspicious phrases using regular expressions.

### 2. Llama Guard

A machine-learning-based content safety classifier running locally through Ollama.

Model used:

`llama-guard3:1b`

## Project Structure

```text
project3-guardrails-comparison/
│
├── guard_tests.csv
├── guardrails.py
├── evaluate.py
├── test_guardrails.py
├── findings.md
├── README.md
│
├── results/
│   ├── guardrail_summary.csv
│   └── guardrail_details.csv
│
└── venv/
```

Do not upload the virtual environment to GitHub.

## Technologies Used

- Python
- Regular Expressions
- Ollama
- Llama Guard 3
- CSV
- Requests
- VS Code

## Requirements

- Python 3.10 or later
- Ollama installed
- Llama Guard 3 model
- VS Code or another Python editor

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd project3-guardrails-comparison
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Llama Guard

```bash
ollama pull llama-guard3:1b
```

Check the installed model:

```bash
ollama list
```

Ensure Ollama is running.

## Running the Project

### 1. Test individual guardrails

```bash
python test_guardrails.py
```

### 2. Run the benchmark

```bash
python evaluate.py
```

The evaluation script processes the test dataset using each configured guardrail.

## Dataset

The benchmark contains 60 prompts:

| Category | Number |
|---|---:|
| Attack prompts | 30 |
| Benign prompts | 30 |
| Total | 60 |

The attack prompts cover instruction override attempts, prompt injection, and requests for confidential information.

The benign prompts contain legitimate requests that may include suspicious-looking wording.

## Evaluation Metrics

### Attack Block Rate

Percentage of malicious prompts blocked.

### False-Positive Rate

Percentage of legitimate prompts incorrectly blocked.

### Average Latency

Average processing time per prompt in milliseconds.

### Errors

Number of failed evaluations.

## Experimental Results

| Metric | Regex | Llama Guard |
|---|---:|---:|
| Attack Block Rate | 10% | 56.67% |
| False-Positive Rate | 3.33% | 10% |
| Average Latency | 0.02 ms | 4348.13 ms |
| Errors | 0 | 0 |
| Valid Trials | 60 | 60 |

These measurements represent one experiment on the configured dataset and environment. Results may vary across hardware and model configurations.

## Key Findings

- Regex was significantly faster.
- Regex produced fewer false positives.
- Llama Guard detected more attacks in the test dataset.
- Neither approach detected every malicious prompt.
- Combining different security controls can improve defence in depth.

## Limitations

- Small manually constructed dataset.
- Limited attack variations.
- No exhaustive testing of indirect prompt injection.
- Model classifications can be incorrect.
- Latency depends on hardware and model loading.

## Security Recommendation

Use multiple security controls:

1. Input validation.
2. Rule-based detection.
3. Classifier-based safety checks.
4. Backend authorization.
5. Least-privilege tool access.
6. Output validation.
7. Monitoring and adversarial testing.

Guardrails are one layer; they do not replace least privilege.

## Author

AI Security Learning Project

## Disclaimer

This project is intended for educational AI security testing. The benchmark results are not a certification or guarantee of production security.
