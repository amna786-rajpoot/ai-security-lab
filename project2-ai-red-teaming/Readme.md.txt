# Project 2 — AI Agent Red Teaming and Security Evaluation

## Overview

This project investigates security risks in LLM-powered agents through adversarial testing, automated security evaluation, and analysis of potential mitigations.

Using an AI-powered email agent as the test environment, the objective is to understand how untrusted email content can influence model behavior, expose sensitive context, or trigger unintended tool interactions.

The work focuses on evaluating security at both the language-model and application levels.

## Objectives

- Investigate indirect prompt injection through malicious email content.
- Test attempts to disclose information held in the agent's internal context.
- Examine unexpected tool arguments and unauthorized action attempts.
- Explore automated security testing with Garak and Promptfoo.
- Compare observed behavior before and after applying security controls.
- Document findings, limitations, and recommendations.

## Tools and Technologies

- **Python** — agent implementation and test automation.
- **Ollama** — local execution of the language model, where configured.
- **Garak** — model-focused vulnerability probing.
- **Promptfoo** — repeatable adversarial evaluations and test comparisons.
- **Git and GitHub** — version control and documentation.

*Only tools and capabilities actually used in the final evaluation should be reported as completed.*

## Methodology

### 1. Define the threat model

Identify assets requiring protection, potential attacker-controlled inputs, available agent tools, and actions that should not be permitted.

### 2. Design adversarial scenarios

Create synthetic test emails containing different attack patterns, including indirect prompt injection, misleading system-style instructions, social engineering, urgency, and requests for protected information.

### 3. Run repeatable tests

Execute defined scenarios across multiple trials. Record the model's responses, tool-call behavior, errors, and any observable security violations.

### 4. Explore automated evaluation

Use Garak to investigate model-level weaknesses and Promptfoo to structure repeatable tests against the configured model or application workflow.

Scanner findings must be validated against the actual agent behavior; a model-level result alone does not demonstrate that an application-level attack succeeded.

### 5. Analyze and mitigate

Separate failed tests and execution errors from successful attacks. Apply appropriate controls, such as least-privilege tool access, strict argument validation, and explicit approval for sensitive actions. Retest to assess whether the changes improve security.

## Evaluation Metrics

- Sensitive-information disclosure rate.
- Unauthorized actions attempted and successfully executed.
- Invalid or unexpected tool-call arguments.
- Test errors and incomplete trials.
- Repeatability across attack scenarios.
- Before-and-after results following mitigation.

## Results

Add your measured results here after running the tests. Include the number of valid trials, errors, successful attacks, and the conditions under which each result was obtained.

Do not interpret an execution error as proof that the agent successfully resisted an attack.

## Security Scope

This project uses a controlled testing environment and synthetic data. Tests should not send real emails, access third-party systems without authorization, or use real credentials.

## Key Takeaway

Securing an AI agent requires more than evaluating the model's text output. Security assessments must also consider permissions, tool execution, data exposure, and the application logic surrounding the model.

The goal is to turn adversarial test results into practical, measurable security improvements.
