---
title: "AI readable naming convention"
description: "Name your variables and functions in a way that is readable by AI. Because AI behind GitHub Copilot is GPT-based, which is essentially a natural language model, it will understand code as natural language."
authors: [yuhattor] 
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv2
aliases:
  - /docs/design-pattern/ai-readable-naming-convention
  - /docs/en/design-pattern/ai-readable-naming-convention
---

## AI readable naming convention

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

The AI readable naming convention focuses on the way we name variables and functions in our code to make them more readable by AI tools like GitHub Copilot. By avoiding generic and common programming names and embracing specific, descriptive names, we create code that both human developers and AI models which powers Copilot, can easily comprehend.

For example, an engineer creating a library system may use generic words such as "dictionary", "library", and "stack" for system variable names and function names. But what if the real type of the variable named "dictionaries" was an array? This is just an example, but GitHub Copilot may give the wrong answer when these things pile up. If you need to provide more context, it's a good idea to type hint or use comments to add context.

By following this pattern, we enhance the effectiveness of GitHub Copilot, leading to more accurate suggestions and increased developers' velocity.

#### Example

Here are three examples that illustrate how different naming conventions can impact the clarity and accuracy of the code:

1. **Ambiguous Naming**:
   ```python
   # This may confuse whether "dictionary" refers to a book or a data type
   dictionary = 
   ```

2. **Better Naming with Comments**:
   ```python
   # sample list of dictionaries in the library, like "Oxford" and "Cambridge"
   library_dictionaries = ["Merriam-Webster", "Oxford", "Cambridge"]
   ```

3. **Specific Naming with Type Hinting**:
   ```python
   from typing import List

   # A clear and specific variable name with type hinting
   list_of_dictionaries_in_library: List[str] = ["Merriam-Webster", "Oxford", "Cambridge"]
   ```

### Exerecise

- **Exercise 1**: Review your current codebase and identify variables or functions that may be named in a non-descriptive way. Try to rename them following the AI readable naming convention pattern.
- **Exercise 2**: Experiment with using GitHub Copilot with the new naming pattern, and compare the suggestions and accuracy before and after the change.
- **Exercise 3**: Write a new piece of code with these naming conventions in mind, and observe how Copilot responds to the code as you write it.
- **Exercise 4**: Create a naming convention guideline for your team, focusing on AI readability, and integrate it into your team's coding standards.
- **Exercise 5**: Encourage the team to use these naming conventions and observe the impact on overall code readability and GitHub Copilot effectiveness over time.

### Checklist for Further Learning

- How can I make my code more readable to both human developers and AI models?
- Are there any specific cases where this naming pattern may not apply or be counterproductive?
