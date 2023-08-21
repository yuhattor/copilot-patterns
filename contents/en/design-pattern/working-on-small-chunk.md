---
name: "Working on small chunks"
description: "Working on small chunks of code with less context, improves the quality of Copilot's output."
authors: [yuhattor] 
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv2
---

## Working on Small Chunks

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

Working on small chunks of code with less context can lead to improved Copilot's output. Imagine you're building a complex application with several interconnected components. Instead of trying to generate everything in one go, you break down the task into smaller parts, providing a confined context for Copilot. This approach not only streamlines the development process but also enhances the quality of the generated code.

Some ideas consider context-less architecture in the design phase, but it is difficult to apply a loosely coupled architecture to every project.

Also, changing the architectural design to improve the accuracy of AI tools is not the way to go. This pattern aims to improve GitHub Copilot's proposal by at least working in small chunks so that the context is as small as possible in the working environment, so that GitHub Copilot does not become overwhelmed by the complexity of the overall project. more controlled, accurate, and efficient code generation that allows you to understand the specific tasks of the clues.

#### Example

Suppose you want to write a function to calculate the factorial of a number. Instead of asking Copilot for the entire solution, you may start by writing the function signature and then ask for the body:

```python
def factorial(n):
  # Ask Copilot to complete this function
```

### Exerecise

- **Exercise 1**: Break down a complex algorithm into smaller parts and use Copilot to generate code for each part.
- **Exercise 2**: Write a high-level description of a task, and then ask Copilot for code in a narrow context. Compare the results.
- **Exercise 3**: Reflect on your personal development process and identify areas where breaking tasks into smaller chunks can be beneficial.

### Checklist for Further Learning

- How can narrowing down the context impact the relevancy of Copilot's suggestions?
- What strategies can be used to provide Copilot with a more precise context for better code generation?
- How does Copilot's probabilistic nature influence its ability to generate code in different scenarios?
- In what situations might working in smaller chunks with Copilot be less effective or more challenging?
