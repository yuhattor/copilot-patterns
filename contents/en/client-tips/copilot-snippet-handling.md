---
title: "Copilot Snippet Handling"
description: "GitHub Copilot uses LLM to generate code. And LLM has a token limitation. You need to know that GitHub Copilot doesn't see all of your code."
category: client-tips
authors: [yuhattor] 
platforms: [copilot]
level: lv2
aliases:
  - /docs/client-tips/copilot-snippet-handling
  - /docs/en/client-tips/copilot-snippet-handling
---

## Copilot Snippet Handling

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

{% hint style="info" %}
While this is accurate as of August 2023, the situation may change as GitHub Copilot and the LLM behind it evolve. Always try to get the most up-to-date information from GitHub.
{% endhint %}

### Description

GitHub Copilot, which utilizes OpenAI's Large Language Models (LLM) to generate code, has a limitation on the number of tokens it can process. As of 2023, it doesn't see all of the code that's open in the editor and doesn't receive every token. This means that users must carefully limit the context provided to GitHub Copilot. Notably, Copilot doesn't have access to external repositories or source code placed in GitHub Enterprise Cloud.

The files that GitHub Copilot uses for suggestions are primarily the currently open file and other tab files adjacent to it (basically with the same file extension). To make accurate suggestions, it's essential to have only the relevant files open. The following is a checklist as of August 2023. The types of files that GitHub Copilot includes as snippets may change in the future, but practices such as "closing unnecessary files" will likely have a positive impact on your coding even if you were not using GitHub Copilot.

- Open the files you need to refer to
- Close unnecessary files
- If there is an .md file you want to refer to, copy it and comment it out

#### Example

Consider a scenario where you have a Python function written in one tab and a similar function in an adjacent tab; GitHub Copilot can recognize patterns and suggest improvements.

```python
# tab 1 (adjacent)
def add_numbers(a, b):.
    return a + b
```

```python
# tab 2
def subtract_numbers(a, b): return a - b
    return a - b

answer = substruct_numbers(1, 2) + add_numbers( # <GitHub Copilot will suggest the code by reading the tab 1 >
```

### Exercise

- **Exercise 1**: Experiment with reducing the code context sent to Copilot in a complex project. Observe how this affects the suggestions provided.
- **Exercise 2**: Discuss with your team the best practice for commenting based on language efficiency and understanding within the team.

### Checklist for Further Learning

- What strategies can be employed to provide the necessary context to Copilot without exceeding token limitations?
- How does the choice of language in comments affect collaboration within a diverse team?
