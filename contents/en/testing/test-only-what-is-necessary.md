---
name: "Test only what is necessary"
description: "Test only what is necessary, so that you can avoid the cost of maintaining unnecessary tests."
category: "testing"
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: 200
---

## Test Only What is Necessary

[<img src="https://img.shields.io/badge/Lv0-Pattern_Idea-blueviolet">](https://github.com/orgs/AI-Native-Development/projects/1/)

{% hint style="info" %}
There is no need to write unnecessary test cases, but it depends on the team what tests are needed. More specific discussion is needed to flesh this out as a pattern.
{% endhint %}

### Description

In the era of rapid software development, writing efficient and useful tests is more important than ever, and when using GitHub Copilot, developers may generate a lot of test code to increase coverage. However, unnecessary test code generation can lead to maintenance burdens and technical debt, so it is important to test only what is necessary when writing test code using GitHub Copilot.

#### Example

Here's an example of how you might choose to write a meaningful test for a specific function rather than writing multiple tests just to boost coverage:

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

- Are you writing tests that truly validate the functionality, or am I writing tests just to increase coverage?
- How can you ensure that the tests I'm writing are providing value to the project and not just adding to the maintenance burden?
- What strategies can you adopt to keep my test suite lean and meaningful, especially when using tools like GitHub Copilot?
