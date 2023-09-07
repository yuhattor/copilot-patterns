---
title: "Code Completion"
description: "Simple code completion with GitHub Copilot"
category: general
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv3
---

## Code Completion

[<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

One of the simplest uses of GitHub Copilot is code completion. Code completion enhances developer productivity by offering potential code snippets as the developer is typing. For example, imagine defining a function in JavaScript. As you input the code below, GitHub Copilot will suggest potential code that could be used inside the function, such as the following code.

#### Example

##### Input Code

```javascript
function calculateSum(a, b) {
    // Enter your code here
}
```

##### Result Suggested by Copilot

```javascript
function calculateSum(a, b) {
    // Enter your code here
    const sum = a + b;
    return sum;
}
```

### Exerecise

- **Exercise 1**: Complete the `calculateSum(a, b)` function by utilizing GitHub Copilot's suggestions. Explore how different prompts or partial code inputs influence the suggestions made by Copilot.

### Checklist for Further Learning

- Did your code output resemble the sample code provided?
- Is the outputted code robust? Is error handling considered? If not, how could you improve the code?
- What prompts or context can you add to write more precise code?
