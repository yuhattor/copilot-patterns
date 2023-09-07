---
title: "Regular Expression"
description: "Generating regular expression patterns drafts with GitHub Copilot"
category: general
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv1
---

## Regular Expression

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

{% hint style="info" %}
Currently, LLMs do not have the ability to properly represent complex regular expressions.
For complex ones, a human must provide supplemental input. On the other hand, it can be applied to simple regular expressions.
{% endhint %}

### Description

GitHub Copilot can create a draft of regular expression patterns. Below, we'll explain how to use regular expressions to search or extract strings. Two examples illustrate how GitHub Copilot can generate regular expressions through both input-output pattern and natural language pattern.

#### Example

##### Input and Output Pattern

###### Sample Code

First, by writing the input and output, GitHub Copilot can create the regular expression pattern:

```python
import re

# Write a regular expression
# - Input: "Hello World"
# - Output: ["H", "W"]

regex
```

###### Sample Result

```python
import re
# Write a regular expression
# - Input: "Hello World"
# - Output: ["H", "W"]

regex = r"[A-Z]"
matched = re.findall(regex, "Hello World")
```

##### Natural Language Pattern

Second, by providing what you want to achieve with the regular expression in natural language:

###### Sample Code

```python
import re
# Write a regular expression
# - "I have 3 apples and 2 oranges" like string, extract only the numbers to make an array

sentence
```

###### Sample Result

```python
import re
# Write a regular expression
# - "I have 3 apples and 2 oranges" like string, extract only the numbers to make an array

sentence = "I have 3 apples and 2 oranges"
regex = r"\d+"
matched = re.findall(regex, sentence)
```

### Exercise

- **Exercise 1**: Extract only the lowercase letters from the string "Hello World."

### Checklist for Further Learning

- Are the regular expression patterns extracting the exact matches from the given strings?
- Currently, LLMs like GitHub Copilot do not have the ability to properly represent complex regular expressions. What would you do if you want to represent a complex regular expression? How would you leverage GitHub Copilot to support and assist you in building it?
