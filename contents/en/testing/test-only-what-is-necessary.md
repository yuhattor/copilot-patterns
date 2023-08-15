---
name: "Test only what is necessary"
description: "Test only what is necessary, so that you can avoid the cost of maintaining unnecessary tests."
category: "test"
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: 200
---

## Test Only What is Necessary

Test only what is necessary, so that you can avoid the cost of maintaining unnecessary tests.

### Description

In the age of rapid software development, writing efficient and useful tests is more crucial than ever. Using GitHub Copilot, an AI-powered tool, developers may be tempted to generate a plethora of tests to increase coverage. However, generating unnecessary test codes can lead to maintenance burdens and technical debt. This section emphasizes the importance of testing only what is necessary, specifically when using GitHub Copilot to write test code.

#### Samples

Here's an example of how you might choose to write a meaningful test for a specific function rather than writing multiple tests just to boost coverage:

```python
def add(a, b):
    return a + b

# Meaningless Test
def test_add():
    assert add(2, 3) == 5
    assert add(100, 80) == 180
```

Here are some examples of possible unnecessary test codes:

- Testing Setters and Getters
- Testing Language Features
- Testing Framework Functionality
- Testing Constants
- Redundant Tests with Same Logic
- Testing Trivial Logic
- Testing Third-party Libraries
- Testing Random Values Without Logic

Rather than adding numerous tests that only increase coverage without adding value.

### Exerecise

- **Exercise 1**: Identify a function in your codebase that is currently over-tested with meaningless tests and refactor it to only include necessary tests.
- **Exercise 2**: Write a new test for a critical part of your code, focusing only on the crucial aspects, avoiding redundancy.
- **Exercise 3**: Evaluate your current test coverage and identify areas where tests can be reduced without losing essential coverage.

### Checklist for Further Learning

- Am I writing tests that truly validate the functionality, or am I writing tests just to increase coverage?
- How can I ensure that the tests I'm writing are providing value to the project and not just adding to the maintenance burden?
- What strategies can I adopt to keep my test suite lean and meaningful, especially when using tools like GitHub Copilot?