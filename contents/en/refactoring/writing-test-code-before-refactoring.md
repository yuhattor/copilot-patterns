---
name: "Writing test code before refactoring"
description: "GitHub Copilot makes it incrediblly easy to modify code, but the suggested code is not always correct even if it looks good. Writing tests is very important before refactoring it. This is no different when using GitHub Copilot."
category: refactoring
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv2
---

## Writing test code before refactoring

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

In the modern world of software development, refactoring can be seen as a fun and engaging task, especially with tools like GitHub Copilot at your disposal. It's so easy to dive in and make changes, but without proper tests, even the most promising code modification can lead to unexpected results. This pattern emphasizes the importance of writing tests before refactoring code to ensure that the functionality remains consistent. Think of tests as your safety net; they catch the problems before they become catastrophic.

#### Example

Suppose you have a function that calculates the total price of a shopping cart, and you want to refactor it for better clarity. Here's the original code:

```python
def total_price(items):
    return sum(item['price'] * item['quantity'] for item in items)
```

Before refactoring, write tests to ensure that the existing functionality is preserved:

```python
def test_total_price():
    items = [
        {'price': 5, 'quantity': 2},
        {'price': 3, 'quantity': 1}
    ]
    assert total_price(items) == 13
```

Now you can refactor the code to make it more readable:

```python
def total_price(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total
```

The test still passes, ensuring that your refactoring didn't change the expected outcome.

### Exercise

- **Exercise 1**: Write a function that needs refactoring and then write corresponding tests for it.
- **Exercise 2**: Refactor the function while ensuring that the tests still pass.
- **Exercise 3**: Simulate a failure by making an incorrect change in the refactored function and observe how the test helps in catching the error.

### Checklist for Further Learning

- How can you make sure that your tests are covering all the important aspects of the code?
- What tools and frameworks are available in your language of choice to help write and run tests?
- How can the practice of Test-Driven Development (TDD) be applied when refactoring? How does it differ from writing tests after the code is written?
- What are the best practices for organizing your tests? How can they be maintained and updated as the code evolves?