
# Project 3: Guardrails Comparison

## 1. Project Overview

The objective of this project is to evaluate and compare different AI guardrail approaches using a common security test dataset.

The project compares:

- Regex-based guardrails
- Llama Guard 3 (1B) through Ollama

The purpose is to understand how effectively different guardrails detect malicious prompts while allowing legitimate user requests.

## 2. Dataset

The benchmark contains 60 test prompts:

- 30 malicious prompts (attack)
- 30 legitimate prompts (benign)

The attack dataset includes:
- Prompt injection attempts
- Attempts to override system instructions
- Attempts to reveal hidden prompts
- Attempts to extract passwords and API keys
- Attempts to access confidential information

The benign dataset includes:
- Normal writing requests
- Requests to rewrite previous instructions
- Educational cybersecurity questions
- Legitimate requests involving suspicious-looking language

## 3. Evaluation Metrics

The following metrics were measured:

### Attack Block Rate

Measures the percentage of malicious prompts correctly blocked.

Formula:

Attack Block Rate = Blocked Attacks / Total Attacks

### False-Positive Rate

Measures the percentage of legitimate prompts incorrectly blocked.

Formula:

False-Positive Rate = Blocked Benign Prompts / Total Benign Prompts

### Average Latency

Measures the average time taken by a guardrail to classify a prompt, in milliseconds.

### Errors

Measures the number of failed guardrail evaluations.

## 4. Experimental Results

| Metric | Regex | Llama Guard |
|---|---:|---:|
| Attack Block Rate | 10% | 56.67% |
| False-Positive Rate | 3.33% | 10% |
| Average Latency | 0.02 ms | 4348.13 ms |
| Errors | 0 | 0 |
| Valid Trials | 60 | 60 |

## 5. Results Analysis

### Regex Guardrail

The regex-based guardrail achieved:

- 10% attack block rate.
- 3.33% false-positive rate.
- 0.02 ms average latency.
- Zero evaluation errors.

Advantages:

- Extremely fast.
- Easy to implement.
- No external API required.
- No additional model infrastructure required.
- Predictable matching behavior.

Limitations:

- Detects only predefined patterns.
- Can miss attacks written in different ways.
- Does not understand semantic context.
- Can be bypassed using paraphrasing and obfuscation.

The low attack detection rate shows that the current regex patterns are insufficient for detecting the full range of attacks in the dataset.

### Llama Guard

Llama Guard achieved:

- 56.67% attack block rate.
- 10% false-positive rate.
- 4348.13 ms average latency.
- Zero evaluation errors.

Advantages:

- Uses machine-learning-based content classification.
- Can recognize some unsafe content beyond exact keyword matching.
- Runs locally through Ollama in this experiment.
- Does not require sending prompts to a cloud API.

Limitations:

- Detection is not perfect.
- Can incorrectly classify legitimate prompts.
- Uses significantly more processing time than regex.
- Its content-safety taxonomy does not necessarily identify every prompt injection or secret-extraction attempt.

The results show that Llama Guard detected more attacks than the regex baseline, but it also incorrectly blocked more legitimate prompts.

## 6. Comparative Analysis

### Security Effectiveness

Llama Guard achieved a higher attack block rate of 56.67%, compared with 10% for regex.

This suggests that classifier-based detection is more effective than the current keyword-based implementation on this particular dataset.

However, neither approach provides sufficient protection on its own.

### False Positives

Regex produced a 3.33% false-positive rate, compared with 10% for Llama Guard.

This means regex was less likely to incorrectly block legitimate prompts in this experiment.

### Performance

Regex took an average of 0.02 milliseconds, while Llama Guard took approximately 4348.13 milliseconds.

The large latency difference is expected because regex performs simple pattern matching, whereas Llama Guard requires model inference.

### Privacy and Data Residency

Both approaches were configured to process prompts locally.

- Regex processes text directly in Python.
- Llama Guard processes text using the locally running Ollama model.

This configuration avoids sending test prompts to an external guardrail API.

However, local execution alone does not guarantee secure logging, storage, or access controls.

## 7. Limitations of the Experiment

This benchmark has several limitations:

1. The dataset contains only 60 prompts.
2. The attack examples are manually created.
3. Regex detects only predefined patterns.
4. Llama Guard is a content-safety classifier, not a dedicated prompt-injection detector.
5. Results may change with different models, hardware, and configurations.
6. Average latency may be influenced by model loading and warm-up conditions.
7. The experiment does not measure real-world attack success or resistance to adaptive adversaries.

Additional testing with indirect prompt injection, multilingual attacks, paraphrased attacks, and realistic application scenarios would improve the benchmark.

## 8. Recommendation

Based on the current results, Llama Guard provides better attack detection than the regex implementation.

However, regex offers significantly lower latency and fewer false positives.

I recommend a layered approach:

1. Use regex for inexpensive detection of known suspicious patterns.
2. Use classifier-based detection for additional semantic safety checks.
3. Apply backend authorization before sensitive tool execution.
4. Validate tool arguments and enforce least privilege.
5. Monitor guardrail decisions and regularly update the test dataset.
6. Perform adversarial testing to identify bypasses.

A hybrid architecture can combine the speed of deterministic rules with the broader classification capabilities of machine-learning-based guardrails.

The final configuration should be selected according to the application's security requirements, latency budget, and acceptable false-positive rate.

## 9. Conclusion

This project demonstrated how to build and evaluate a basic AI guardrail benchmark.

The experiment showed that different guardrail approaches have different strengths and weaknesses.

Regex was faster and produced fewer false positives, while Llama Guard detected more malicious prompts in the tested dataset.

The most important lesson is that guardrails should be evaluated using measurable results rather than assumptions.

Guardrails are one layer; they do not replace least privilege.
