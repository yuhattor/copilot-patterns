# Context Directory

Also known as a snippet directory for snippet inclusion.

## Description

By collecting the context of the entire codebase in the context directory within the repository, it is easier to provide GitHub Copilot with accurate context during development.

## Problem

* Inaccurate suggestions:
  GitHub Copilot may make inaccurate suggestions if it cannot obtain the context of the entire codebase, which can lead to lower code quality and increased time spent by developers on fixing or adjusting code.
* Reduced efficiency:
  If developers do not have related files open in adjacent tabs, GitHub Copilot cannot obtain information from those files. This can result in inaccurate suggestions and force developers to manually search and reference related files while writing code, potentially decreasing their productivity.
* Loss of code consistency:
  If GitHub Copilot cannot obtain the context of the entire codebase, the code it suggests may lack consistency with existing code. This can negatively impact code readability and maintainability, and slow down the development speed of the entire team.

## Story

One day, an engineer on a project team decided to use GitHub Copilot to develop a new feature. She was excited about GitHub Copilot and believed it would help her write code quickly.

However, as development progressed, she realized that GitHub Copilot occasionally made inaccurate code suggestions. Even though she manually corrected them and continued development, she became increasingly tired of the task. Furthermore, other team members also pointed out that GitHub Copilot's suggested code lacked consistency.

She wondered why GitHub Copilot was not making accurate suggestions, and upon investigation, found that one reason for inaccurate suggestions was not having related files opened correctly. On the other hand, leaving all files open was not realistic, and since GitHub Copilot only sends adjacent tab data as tokens, it did not make sense to open too many files. She also realized that the Codex model used by GitHub Copilot had limits on the number of tokens that could be passed.

Therefore, she decided to introduce the context directory pattern. By keeping related files open, she expects GitHub Copilot to make more accurate suggestions.

## Context

GitHub Copilot, a representative product of AI coding support tools, currently makes suggestions based on information from the currently open file or files with the same extension open in tabs. The number of tokens that can be passed to the Codex model used by GitHub Copilot is limited. Therefore, GitHub Copilot extensions such as VS Code do not send all information from the open files as reference information to the GitHub Copilot server, but prioritize sending data from files with high similarity to the currently open files. Including snippets is called "snippet inclusion". Therefore, it is necessary to open only an appropriate number of related files in adjacent tabs.

## Solution

1. Create a context directory: Create a directory where personal or team files that you want to collect as context or rules that you want to memorize with GitHub Copilot can be collected.
2. Close files unrelated to the current development.
3. Open files related to the current development in VSCode and keep them open in tabs. While GitHub Copilot does not have a feature to obtain the context of the entire codebase, it can read the current file and files opened in the editor. By keeping related files open, GitHub Copilot can provide more accurate suggestions.

## Resulting Context

Using the context directory allows GitHub Copilot to provide more accurate suggestions. By keeping related files open, effective code completion can be obtained.

## Note

* The files that GitHub Copilot currently reads are limited. If you are writing Python code, it is desirable that the snippet files and reference files are also Python code.
* If necessary, you can write these directories in .gitignore to avoid pushing the contents.
* You can also use Git Submodule to separate the context directory from other directories.
