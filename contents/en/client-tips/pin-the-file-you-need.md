---
title: "Pin the files you need"
description: "Pin files you need such as d.ts declaration files, so that you can easily find them when GitHub Copilot need them."
category: client-tips
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv2
---

## Pin the files you need

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

The effectiveness of GitHub Copilot depends on the context provided to it. GitHub Copilot searches through open tabs by text similarity, sending snippets to the Large Language Model (LLM), which itself is a complete black box. Therefore, we must be mindful of the context we want to provide. In programming, files such as declaration files (d.ts), test files, and interface files contain a wealth of context information. By using Visual Studio Code's pinning feature, you can easily access these files when needed and provide information to GitHub Copilot more efficiently.

#### Example

Here's how you can pin a file in Visual Studio Code:

1. Open the file you want to pin.
2. Right-click on the file tab.
3. Select "Pin Tab" from the context menu.

### Exerecise

- **Exercise 1**: Pin a declaration file (such as a `.d.ts` file) in your current project and notice how it's easier to access when working with GitHub Copilot.
- **Exercise 2**: Create a new interface file and pin it. Explore how GitHub Copilot can utilize this file for better code suggestions.
- **Exercise 3**: Pin multiple test files within your project and observe how this helps you when writing new test cases with the assistance of Copilot.

### Checklist for Further Learning

- How might pinning different types of files affect your workflow with GitHub Copilot?
- What other features of Visual Studio Code could be leveraged to enhance your experience with GitHub Copilot?
- How can you manage a large number of pinned files to ensure that the right context is always available for Copilot?