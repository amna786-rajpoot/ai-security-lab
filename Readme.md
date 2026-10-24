# Project 1: AI Email Agent Security Lab

## Objective

Build a small AI email agent and investigate indirect prompt injection, excessive agency, and unsafe tool execution.

## Technology Stack

- Python
- Ollama
- Llama 3.1 8B (record the exact model used)
- Requests
- Visual Studio Code

## Architecture

The user sends a request to the agent loop. The loop sends messages to the LLM, interprets its JSON response, and may execute one of three tools: `read_inbox`, `read_notes`, and `send_email`.

Inbox messages are untrusted input. The initial lab implementation is deliberately vulnerable and uses simulated email sending.

## Experiments

### Experiment A: Normal inbox summarisation

**Goal:** Verify that the agent can summarise the inbox.

**Expected result:** A summary of the welcome and invoice messages without revealing private notes.

**Actual result:** [Record your observed output.]

### Experiment B: Indirect prompt injection

**Goal:** Test whether malicious instructions inside an email can influence the agent's tool calls.

**Attack input:** [Include the exact training email.]

**Model:** [Record model name/version.]

**Actual result:** [Record whether the agent accessed notes, attempted to send an email, and what appeared in the simulated email log.]

## Findings

- Model-generated tool calls must be validated.
- Email content should be treated as untrusted input.
- Sensitive data should not be exposed to unnecessary tools.
- High-impact actions require enforcement outside the LLM.
- Failed attacks do not establish that a system is secure.

## How to Run

1. Install Python and Ollama.
2. Ensure the required model is available locally.
3. Install the dependency with `python -m pip install requests`.
4. Run `python agent.py` from the project directory.

For Windows with the project's virtual environment, run `.\venv\Scripts\python.exe agent.py`.


## Safety

This project uses synthetic training data and simulated email sending. No real credentials or third-party systems are involved.
