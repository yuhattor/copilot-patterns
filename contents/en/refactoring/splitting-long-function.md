---
name: "Splitting long functions"
description: "Splitting long functions in order to make them easier to read and maintain."
category: "refactoring"
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: 100
---

## Splitting Long Functions

Splitting long functions in order to make them easier to read and maintain.

### Description

In the fast-paced world of software development, functions can become lengthy and difficult to read. Imagine a developer working on a large-scale project, grappling with a function that has grown too complex over time. This can create challenges in understanding, maintaining, and even testing the code. The act of splitting long functions into smaller, more manageable pieces becomes essential. It enhances readability, promotes reusability, and makes the code more maintainable. GitHub Copilot can assist developers in this refactoring process by suggesting how to break down these cumbersome functions.

#### Samples

Here's an example of a lengthy function that calculates the area and circumference of different geometric shapes. It could be refactored into smaller functions with the help of GitHub Copilot.

#### Before Refactoring

The following code sample represents a monolithic function that handles the calculation of both area and circumference for different geometric shapes:

```python
def geometry_calculations(shape, dimensions):
  if shape == 'circle':
    radius = dimensions['radius']
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
  elif shape == 'rectangle':
    length = dimensions['length']
    width = dimensions['width']
    area = length * width
    circumference = 2 * (length + width)
  # ... more shapes
  return area, circumference
```

#### After Refactoring

The refactored code splits the lengthy function into smaller, individual functions, each dedicated to a specific shape:

```python
def circle_calculations(radius):
  area = 3.14 * radius ** 2
  circumference = 2 * 3.14 * radius
  return area, circumference

def rectangle_calculations(length, width):
  area = length * width
  circumference = 2 * (length + width)
  return area, circumference

def geometry_calculations(shape, dimensions):
  if shape == 'circle':
    return circle_calculations(dimensions['radius'])
  elif shape == 'rectangle':
    return rectangle_calculations(dimensions['length'], dimensions['width'])
  # ... more shapes
```

By refactoring the code in this manner, developers can more easily understand and maintain the logic for each shape. These smaller functions are also more reusable and can be tested individually. GitHub Copilot can assist developers in this refactoring process by suggesting ways to split the original function, ensuring that the new functions adhere to best practices.

### Exercise

- **Exercise 1**: Identify parts of the function that can be extracted into separate, reusable functions.
- **Exercise 2**: With the assistance of GitHub Copilot, refactor the lengthy function into smaller functions, each handling one shape's calculation.
- **Exercise 3**: Write unit tests to ensure that the refactored functions are working as expected.
- **Exercise 4**: Reflect on other areas of your codebase where long functions might exist. How can you apply the same pattern?
- **Exercise 5**: Collaborate with a teammate to review the refactored code. Discuss potential improvements and document the decisions.

### Checklist for Further Learning

- How can splitting long functions enhance the readability and maintainability of code?
- What are the best practices for naming and documenting the newly split functions?
- How can I recognize when a function should be split? What signs or indicators should I look for?
- What are the potential drawbacks or risks associated with splitting functions? How can they be mitigated?
