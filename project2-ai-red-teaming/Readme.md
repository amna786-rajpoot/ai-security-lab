# AI Agent Red Teaming and Security Evaluation

## Overview

This work focuses on identifying and evaluating security vulnerabilities in an AI-powered email agent using adversarial testing and automated security assessment.

The objective is to understand how malicious email content can manipulate an LLM, influence its decisions, expose sensitive information, or trigger unintended tool interactions.

## Security Areas Investigated

- Indirect prompt injection
- Sensitive information disclosure
- Social engineering attacks
- Excessive agency and unauthorized tool use
- Tool argument validation
- Handling of untrusted email content

## Tools and Technologies

- Python
- Ollama
- Garak
- Promptfoo
- Git and GitHub

## Testing Approach

A collection of synthetic adversarial emails was designed to test different attack patterns, including malicious instructions, fake system notices, authority claims, urgency, and attempts to extract protected information.

Repeated trials were used to observe agent responses and identify potential security weaknesses.

Garak was explored for model-level vulnerability probing, while Promptfoo was explored for structuring repeatable adversarial evaluations.

## Security Evaluation

The evaluation focuses on:

- Sensitive information disclosure
- Unauthorized tool calls
- Actions attempted versus actions executed
- Invalid tool arguments
- Reproducibility of test outcomes
- Changes in behavior after applying security controls

## Security Considerations

All experiments use synthetic data and a controlled local environment. No real credentials or unauthorized external email services are used.

## Key Objective

The goal is to evaluate AI agent security beyond model responses by examining the complete application, including tool access, execution logic, and authorization controls.
