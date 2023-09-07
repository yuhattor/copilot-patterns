---
title: "Creating unit tests"
description: "Create unit test with GitHub Copilot"
category: testing
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv3
aliases:
  - /docs/testing/creating-unit-tests
  - /docs/v/en/testing/creating-unit-tests
---

## Creating Unit Tests

[<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

Testing is a fundamental part of the software development process, ensuring that the code meets its design and behaves as intended. The creation of unit tests, which test individual components of the system, can be both challenging and time-consuming. With GitHub Copilot, this process becomes more streamlined. Let's explore how a developer named Alice leverages GitHub Copilot to write unit tests for her application, reducing her workload and boosting her efficiency.
This pattern is also applicable to functional and API testing.

#### Example

Alice is working on a JavaScript function that needs to be thoroughly tested. With the help of GitHub Copilot, she can quickly generate the required unit tests.

Here's a simple function she wants to test:

```javascript
function add(x, y) {
  return x + y;
}
```

And here's how she might create a unit test with Copilot's assistance:

```javascript
const assert = require('assert');

describe('add function', () => {
  it('should add two numbers correctly', () => {
    assert.equal(add(2, 3), 5);
  });
});
```

### Exercise

- **Exercise 1**: Create a unit test for a function that multiplies two numbers using GitHub Copilot.
- **Exercise 2**: Utilize Copilot to create a suite of tests for various edge cases, such as handling null or undefined values.
- **Exercise 3**: Reflect on your current project. Identify a part of the code that lacks testing and create unit tests for it using Copilot.

### Checklist for Further Learning

- How can you make sure you tests are comprehensive and cover all possible scenarios?
- What prompts do you add when GitHub Copilot does not cover a scenario at all?
- How is GitHub Copilot beneficial for other types of testing (E2E testing, integration testing, functional testing, etc.) and how can GitHub Copilot assist you in writing them?
