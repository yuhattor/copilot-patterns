---
title: "Asking with open-ended questions"
description: "For code improvements, such as better error handling, troubleshooting methods, refactoring ideas, etc., open-ended questions can be used to pull new ideas from GitHub Copilot."
category: refactoring
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv1
---

## Asking with Open-Ended Questions

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

Refactoring is often a complex process. It is not necessarily about what is right and what is wrong, but about understanding the basic concepts and potential improvements. using open questions in GitHub Copilot, developers can work on improving code in a more thoughtful way with the help of GitHub Copilot GitHub Copilot can help developers work on code improvements in a more thoughtful way.

#### Example

Introducing open-ended questions in your queries with GitHub Copilot can lead to insightful suggestions. For example:

```javascript
// Q: How can I improve the restorability of this function?
// A: <GITHUB COPILOT SUGGESTION>
function backupData(data) {
  // Implementation here
}

// Q: What's the best way to handle errors in this context?
// A: <GITHUB COPILOT SUGGESTION>
try {
  // Some operation
} catch (error) {
  // Error handling
}
```

### Exercise

- **Exercise 1**: Write a function related to file handling and ask Copilot how to make it more reliable and efficient.
- **Exercise 2**: Create a code snippet that includes exception handling and ask Copilot for suggestions to improve error reporting.
- **Exercise 3**: Design a simple UI component and ask Copilot how to access or manipulate it in a more elegant way.

### Checklist for Further Learning

- What other areas of your code can benefit from refactoring?
- How can open-ended questions assist in your development process?
