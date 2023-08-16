# AI Friendly Naming Convention

{% hint style="info" %}
This document is still under review. We encourage active discussion on [GitHub Issue #6](https://github.com/AI-Native-Development/patterns/issues/6)
{% endhint %}

## Description

This document explains naming convention patterns that can be useful when writing code with AI coding assistance tools. By using these patterns, code can be written in a way that is more readable and understandable by AI.

## Problem

When writing code, it can be difficult to decide what to name variables and functions. Also, if one tries to provide context only through comments, the code can become difficult for the reader to understand. This readability issue can also affect the accuracy of GitHub Copilot's suggestions. Ultimately, it can lead to not receiving accurate suggestions from GitHub Copilot.

## Context

GitHub Copilot, the representative of AI coding assistance tools, uses an engine called Codex, which is based on the GPT3 model. The GPT3 model can understand natural language, and Codex can also understand natural language in the same way. By using variable expressions similar to natural language, more readable and understandable code can be written.

## Solution

If you are struggling with naming variables and functions when writing code, you can create a common naming convention with your team in advance, assuming that AI coding assistance tools will read it, so that you can write code that is more readable and understandable by AI. Instead of providing context only through comments, AI coding assistance tools can make more accurate suggestions by using variable expressions similar to natural language.

The following are examples of naming convention patterns:

* Use lowercase or camelcase
* Use variable expressions similar to natural language
* Use short names
* Use descriptive names

## Resulting Context

By using this naming convention pattern, code can be written in a more readable and understandable way, and AI can make more accurate code suggestions.
