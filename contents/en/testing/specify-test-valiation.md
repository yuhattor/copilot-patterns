---
name: "Specify how to generate test code"
description: "Specify how to generate test code, such as the test framework to use and the number of test cases to generate."
category: "test"
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: 100
---

## Specify How to Generate Test Code

Specify how to generate test code, such as the test framework to use and the number of test cases to generate.

### Description

When it comes to testing, specific instructions can be a great way to make sure you're covering all the necessary scenarios. Instead of giving vague instructions like "add unit tests," you can provide concrete details about the testing frameworks and the number of cases you want to generate. This can be helpful in utilizing tools like GitHub Copilot, where specifying "use Junit and Mockito to add unit tests, testing at least 10 variations of valid and invalid input combinations" can yield a more accurate and comprehensive result.

#### Samples

If you are aiming to generate a test code using Junit and Mockito, you can provide the following prompt to GitHub Copilot:

```java
// Using Junit and Mockito, add unit tests
// Test at least 10 variations of valid and invalid input combinations
@Test
public void validateInput() {
  // Your code here
}
```

### Exercise

- **Exercise 1**: Write a unit test using JUnit that tests a simple method with 3 different valid inputs.
- **Exercise 2**: Extend the unit test to include 3 different invalid inputs, and verify that exceptions are handled correctly.
- **Exercise 3**: Integrate Mockito into the existing tests and simulate dependencies to validate interactions within the code under test.

### Checklist for Further Learning

- How can I ensure that the tests cover all the critical paths in the code?
- What strategies can be used to maintain the tests as the codebase evolves?
- How can mocking frameworks like Mockito help in isolating the code under test from its dependencies?
