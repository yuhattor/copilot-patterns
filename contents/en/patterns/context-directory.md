# Context Directory

Also known as: Snippet Inclusion

## Description

Collecting the entire codebase context in the context folder within the repository to enable GitHub Copilot to provide accurate suggestions.

## Problem

* Inaccurate suggestions:
  GitHub Copilot makes suggestions based on the information in the open file and other related files. Copilot may not obtain the context of the entire codebase, resulting in inaccurate suggestions. This may lead to lower code quality and increased time for developers to make corrections and adjustments.
* Decreased efficiency:
  If developers do not keep related files open in adjacent tabs, GitHub Copilot cannot obtain information from those files. As a result, suggestions may become inaccurate, and developers may need to manually search for and reference related files while coding. This may decrease developer productivity.
* Loss of code consistency:
  If Copilot cannot obtain the context of the entire codebase, the code it suggests may be inconsistent with existing code. This may negatively affect code readability and maintainability and slow down the development speed of the entire team.

## Story

One day, a mid-level engineer on the project team decided to develop a new feature using GitHub Copilot. She was fascinated by Copilot and believed that it would help her write code quickly.

However, as development progressed, she noticed that the code suggested by GitHub Copilot was sometimes inaccurate. Nevertheless, she manually corrected it and continued development, but gradually became tired of the task. In addition, other team members pointed out that the code suggested by Copilot lacked consistency.

She wondered why Copilot did not make accurate suggestions and began investigating, discovering that one reason for inaccurate suggestions was that related files were not properly opened. However, keeping all files open is not practical, and Copilot only sends data from adjacent tabs, so there is no point in keeping many files open. Moreover, she realized that there is a limit to the number of tokens that can be passed as part of the Codex model used by GitHub Copilot.

Therefore, she decided to introduce the context directory pattern. By keeping related files open, she hopes that GitHub Copilot will be able to make more accurate suggestions.

## Solution

1. Create a Context directory:
Create a directory where you or your team can collect files that you want to use to assist in providing context and rules for GitHub Copilot.
1. Keep related file tabs open in VSCode:
Currently, GitHub Copilot does not have a feature to obtain the context of the entire codebase, but it can read the current file and all files open in the IDE. Keeping related file tabs open enables GitHub Copilot to make more accurate suggestions.

You can write these directories in .gitignore if you do not want to push their contents.
You can also use Git Submodules to separate the context directory from others.

## Resulting Context

Using the context folder pattern enables GitHub Copilot to provide more accurate suggestions. By keeping related file tabs open, you can get effective code completion.

## Note

* Currently, GitHub Copilot has limited file reading targets. When writing Python, it is desirable for snippet files and reference target files to also be Python code.
