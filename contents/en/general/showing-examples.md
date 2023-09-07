---
title: "Showing Examples"
description: "Generating code from given examples"
category: general
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/general/showing-examples
  - /docs/v/en/general/showing-examples
---

## Showing Examples

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

Using GitHub Copilot, developers can generate code based on provided examples. This can be incredibly useful when you expect the code that produces a specific output. In this pattern, we'll explore how to create a Ruby on Rails model from a given example, such as generating JSON.

#### Example

The following sample illustrates how you can provide an example in comments and ask GitHub Copilot to generate Ruby on Rails code to create the corresponding model.

```bash
# Example of code generation to create the following JSON:
# {
#   "name": "John Smith",
#   "age": 30,
#   "description": "This is a sample description.",
#   "country": "Japan",
#   "title": "Customer Success Architect",
#   "email": "johnsmith@example.com"
# }
rails g model users name:string age:integer description:text country:string title:string email:string
```

### Exercise

- **Exercise 1**: Based on the following example, generate the Ruby on Rails code to create a model for books.
  ```json
  {
    "title": "Book",
    "author": "Jane Doe",
    "price": 19.99
  }
  ```
- **Exercise 2**: Experiment with different attributes and types in the JSON example, then generate the corresponding Rails code.
- **Exercise 3**: Test the generated code in a Rails project to ensure that it creates the expected model.

### Checklist for Further Learning

- Does the generated code accurately reflect the given example, creating the appropriate Ruby on Rails code?
- What were the key considerations or challenges when generating code from the provided example?
- How can you further customize or optimize the generated code to suit specific project requirements?
