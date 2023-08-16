---
name: "Writing failure case first"
description: "GitHub Copilot will read your implementation and generate a test case based on it. It tends to generate a test case for the success case. Be careful not to forget the failure case."
category: "testing"
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: 100
---

## Writing Failure Case First

<img src="https://img.shields.io/badge/Lv0-Pattern_Idea-blueviolet">

### Description

In a development cycle, writing test cases is an essential aspect. When working with GitHub Copilot, it becomes even more convenient as it reads your implementation and generates test cases accordingly. While GitHub Copilot is very effective in generating success cases, it's vital not to overlook the failure cases. Considering failure cases first can lead to more robust code.

#### Example

To demonstrate the importance of this, consider a function that divides two numbers. GitHub Copilot might suggest a test case that covers the happy path. But what about when the denominator is zero?

```python
def divide(a, b):
  return a / b

# Failure test case
def test_divide_by_zero():
  # <YOUR CODE AND GITHUB COPILOT SUGGESTION HEERE>
```

### Exerecise

- **Exercise 1**: Write a function that multiplies two numbers and include both successful and failure test cases (consider edge cases like multiplying large numbers).
- **Exercise 2**: Analyze an existing piece of code in your project and identify any missing failure test cases. Write these test cases and ensure they pass.
- **Exercise 3**: Implement a failure-first approach in your next project, writing the failure test cases before the actual implementation, and reflect on how this impacts your development process.

### Checklist for Further Learning

- Have you considered all potential failure cases in recent code?
- Do you consistently include failure test cases in your test suite?
- How can you encourage your team to adopt a TDD mindset in creating test cases?
