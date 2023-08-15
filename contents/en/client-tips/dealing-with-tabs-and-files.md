---
name: "Dealing with Tabs and Files"
description: "Copilot reads files in the same programming language, so it is important to understand the context of the code."
category: "editor"
authors: [yuhattor] 
platforms: [copilot]
level: 100
---

## GitHub Copilot and Tabs

### Description

Imagine working on a complex project with multiple tabs open. As you toggle between files, writing code, and scrutinizing your project's structure, GitHub Copilot is there by your side. This AI pair-programmer doesn't just see your current file; it views adjacent tabs and correlates them. It seeks out similarities in the content of the current line and finds corresponding files in adjacent tabs.

This characteristic of GitHub Copilot enables it to read files written in the same programming language, acting as an intelligent guide through the maze of code. However, it's worth noting that the AI doesn't perfectly understand all context. The goal of GitHub Copilot is to strike a balance between accuracy and response speed to enhance your development process.

#### Samples

Consider a scenario where you are writing a Python function in one tab, and you have a similar function in an adjacent tab. GitHub Copilot can recognize the pattern and suggest improvements.

```python
# Tab 1
def add_numbers(a, b):
    return a + b

# Tab 2 (Adjacent)
def subtract_numbers(a, b):
    return a - b
```

GitHub Copilot will use the context from both tabs to assist in generating relevant code.

### Exerecise

- **Exercise 1**: Experiment with GitHub Copilot by opening multiple tabs and observe how it provides suggestions.
- **Exercise 2**: Try closing a particular tab and see how its behavior changes.

### Checklist for Further Learning

- How does GitHub Copilot handle tabs with different programming languages adjacent to each other?
- What are the limitations of GitHub Copilot's understanding of context across different tabs?
- How can you optimize GitHub Copilot's performance by strategically arranging tabs and related files?

### Notes

GitHub Copilot is constantly evloving and improving and algorithms can also be updated. This inforamtion is accurate as of August 2023.