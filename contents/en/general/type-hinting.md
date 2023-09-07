---
title: "Type Hinting"
description: "Writing type hints when you write dynamic typing programming language, to increase copilot suggestion accuracy."
category: general
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/general/type-hinting
  - /docs/en/general/type-hinting
---

## Type Hinting

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

In the world of dynamic typing programming languages, developers often face challenges in understanding code, especially when working on complex systems. Type hinting adds a layer of clarity by explicitly declaring the expected data types. With GitHub Copilot, the integration of type hinting can increase the accuracy of code suggestions, empowering developers and GitHub Copilot to write code more efficiently.

Imagine you're working on a project where functions are deeply nested, and tracking the types of variables becomes convoluted. Integrating type hinting also makes the code more readable for your fellow developers.

#### Example

Here's how you can define a function with type hints in Python:

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

Copilot will recognize these type hints and generate code suggestions accordingly.

### Exerecise

- **Exercise 1**: Write a function that takes two string parameters and returns their concatenation, using type hints.
- **Exercise 2**: Convert an existing piece of code in your project to include type hints, and observe the difference in Copilot's suggestions.
- **Exercise 3**: Create a complex class with multiple methods and use type hinting for all the parameters and return types.

### Checklist for Further Learning

- Are you using type hints consistently throughout my codebase?
- Have I considered the potential drawbacks of overusing type hinting, and how do I find the right balance in my code?
