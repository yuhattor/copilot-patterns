---
name: "High-level Architecture First"
description: "Provide high-level context first by writing comments at the top of the file, followed by comments and code that provide explicit instructions."
authors: [yuhattor] 
category: "design-pattern"
platforms: [copilot, copilot-chat]
level: 100
---

## Pattern: Provide High-level Context First

Provide high-level context first by writing comments at the top of the file, followed by comments and code that provide explicit instructions.

### Description

Creating a well-understood high-level context can greatly aid developers and GitHub Copilot when working on complex code. By writing comments at the top of the file, followed by specific comments and code that provide explicit instructions, you establish a general context for what the code does. Think of this as a roadmap for your code, providing a bird's eye view to anyone reading or maintaining it. In this pattern, you'll see how adding comments about HTTP routes in a web application can guide the developers through the intended functionality.

#### Samples

Consider an API endpoint file in a Ruby-based web application. The comments at the beginning of the file help the reader understand the functionality of each endpoint.

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

- **Exercise 1**: Analyze a piece of code in your project that could benefit from high-level comments and implement the pattern.
- **Exercise 2**: Write a script for a different set of API endpoints, following the high-level context pattern.
- **Exercise 3**: Review someone else's code, and if lacking high-level context, discuss with them how to implement this pattern.

### Checklist for Further Learning

- Have I established a clear roadmap at the top of my code file?
- Can a new developer understand the file's purpose just by reading the high-level comments?
- Am I consistently applying this pattern across my codebase?