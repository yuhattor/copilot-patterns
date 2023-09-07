---
title: "High-level Architecture First"
description: "When writing code with GitHub Copilot, instead of suddenly starting with the details, design the high-level architecture first, then give clear instructions in comments and code, so that GitHub Copilot can make suggestions more precisely."
authors: [yuhattor] 
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/design-pattern/high-level-architecture-first
  - /docs/en/design-pattern/high-level-architecture-first
---

## High-level Architecture First

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

When developing a complex system, it is common to dive into the details of the code and lose sight of the overall architecture of the program. When this happens repeatedly, GitHub Copilot also loses sight of its overall architecture. This can lead to misunderstandings and errors. By designing the high-level architecture of the program first and commenting on the function and purpose of each piece of code during development, GitHub Copilot can better understand the context and make more precise suggestions.

#### Samples

Consider an API endpoint file in a web application. Suggesting the design in natural language early on will help GitHub Copilot understand the functionality of each endpoint.

```rb
# GET /items
# - Retrieves a list of items.
# - Returns a collection of items in the response.
# 
# POST /items
# - Creates a new item and adds it to the collection.
# - Expects item parameters in the request.
# - Redirects to the cart page with a success message upon success.
# - Displays the form for a new item if failed.
# 
# GET /items/:id
# - Retrieves an item with a specific ID.
# - Expects the item's ID as a URL parameter.
# - Returns the requested item's details in the response.
# ...
```

### Exercise

- **Exercise**: Create an outline of the high-level architecture for a login and registration system, including comments for each endpoint.

### Checklist for Further Learning

- Have you established a clear roadmap before writing code details?
- Does GitHub Copilot understand the purpose of a file just by reading the high-level comments?
- Are you applying this pattern consistently throughout your codebase?
