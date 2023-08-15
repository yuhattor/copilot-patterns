---
name: "Rewriting comments"
description: "Not only refactoring the code, but also refactoring the comment, to improve the suggestion quality of Copilot. For example, hinting at function names directly in the comment."
category: "refactoring"
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: 100
---

## Rewriting Comments

Not only refactoring the code, but also refactoring the comment, to improve the suggestion quality of Copilot. For example, hinting at function names directly in the comment.

### Description

In the world of software development, code refactoring is a common practice, but what often gets overlooked is the refactoring of comments. Rewriting comments involves not just revising the code but also the accompanying explanations and hints. 
GitHub Copilot is a tool, but like a human, it can understand the natural language and context of the code. This pattern aims to improve the suggestion quality of GitHub Copilot by hinting at function names and other context directly in the comments, facilitating a clearer understanding of the code and its functionality.

#### Samples

Here is an example of refactoring both code and comment:

Before:
```python
# Calculates total
def total_amount(x, y):
    return x + y
```

After:
```python
# Calculates the total amount by adding x and y
# Arguments:
#  x: the first number
#  y: the second number
def total_amount(x, y):
    return x + y
```

### Exercise

- **Exercise 1**: Review a code snippet and identify comments that can be refactored to add more context or clarity.
- **Exercise 2**: Rewrite a comment to include specific function or variable names, improving its descriptiveness.
- **Exercise 3**: Use GitHub Copilot to refactor a piece of code, and ensure that the comments are updated accordingly to reflect the changes.

### Checklist for Further Learning

- What are the benefits of rewriting comments along with the code during the refactoring process?
- How can refactoring comments improve the readability and maintainability of the code?
- In what situations might it be necessary to avoid over-descriptive comments, and how can a balance be struck?