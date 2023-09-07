---
title: "Consistent coding style"
description: "Consistent coding style leads to better suggestions from GitHub Copilot."
authors: [yuhattor] 
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv3
aliases:
  - /docs/design-pattern/conistent-coding-style
  - /docs/v/en/design-pattern/consistent-coding-style
---

## Consistent coding style

[<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

Consistent coding style is crucial in software development, as it not only enhances code readability but also leads to better suggestions from GitHub Copilot. Indentation, tabs, naming conventions, comment writing, language-specific abbreviations, and many other areas of coding style. By adhering to a uniform coding style and pattern, developers find it easier to follow excellent coding practices. 

#### Example

Here's a positive example of using clear function names and following the codebase pattern using snake_case:

```python
def calculate_area(length, width):
    return length * width
```

Compare this with the inconsistent coding style below, where inappropriate function naming may lead to generic comments like "code goes here" from GitHub Copilot:

```python
def calcSomething(l, w):
    # code goes here
    return
```

### Exercise

- **Exercise 1**: Practice writing functions using descriptive and consistent naming conventions.
- **Exercise 2**: Analyze a code snippet and identify inconsistencies in coding style. Make necessary adjustments.
- **Exercise 3**: Utilize GitHub Copilot to create a small project, observing how it responds to different coding styles.

### Checklist for Further Learning

- How does consistent coding style affect readability and maintainability of the codebase?
- What communication is needed to enforce coding standards within a team or project?
- How can GitHub Copilot assist in adhering to coding best practices? What behaviors does it promote or discourage?