---
name: "Consistent coding style"
description: "Consistent coding style leads to better suggestions from GitHub Copilot."
authors: [yuhattor] 
category: "design-pattern"
platforms: [copilot, copilot-chat]
level: 100
---

## Consistent coding style

Consistent coding style leads to better suggestions from GitHub Copilot.

### Description

Consistent coding style is crucial in software development, as it not only enhances code readability but also leads to better suggestions from GitHub Copilot. By employing descriptive variable names and functions and adhering to a uniform coding style and pattern, developers find it easier to follow excellent coding practices. For instance, GitHub Copilot can generate relevant code suggestions based on your consistency in coding style.

#### Samples

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
- What tools and techniques can be employed to enforce coding standards within a team or project?
- How can GitHub Copilot assist in adhering to coding best practices? What behaviors does it promote or discourage?