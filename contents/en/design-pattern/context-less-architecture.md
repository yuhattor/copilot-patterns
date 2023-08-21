---
title: "Context-less Architecture"
description: "Confine coding to smaller contexts and loosely coupled program architecture"
authors: [yuhattor] 
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv0
---

## Context-less Architecture

[<img src="https://img.shields.io/badge/Lv0-Pattern_Idea-blueviolet">](https://github.com/orgs/AI-Native-Development/projects/1/)

{% hint style="info" %}
Loosely coupled architectures themselves are also recommended in many cases, and this pattern is consistent with that idea. However, more discussion is needed to tie the context of AI Powered development to the broader architecture discussion and justify it. By all means, let the discussion begin.
{% endhint %}

### Description

Contextless architecture is a design pattern that limits coding to smaller, well-defined contexts within a system. By breaking complex programs into loosely coupled, independent components, this architecture improves maintainability, scalability, and flexibility.

When working with AI tools like GitHub Copilot, it is essential to understand their nature and limitations. Currently GitHub Copilot is not AGI (Artificial General Intelligence) and therefore works best within a limited and precise context. By focusing on specific needs, developers can maximize Copilot's accuracy and efficiency.

The key is to create a loosely coupled system where each component serves a specific purpose. This approach is consistent with the limitations of GitHub Copilot and allows developers to use the tool more effectively to build modular, robust software.

**On the other hand, you should not design a system to fit the tools.**
This pattern is intended to more effectively speed up development by additionally considering the use of AI in development when it makes sense to be loosely coupled in real-world projects and products.

#### Example

##### Before

Here, user management is mixed with authentication, making the context unclear and intertwined.

```python
class UserManager:
    def create_user(self, username, password):
        # Code to create user
        pass

    def login(self, username, password):
        # Code to handle login
        pass

    def update_user_profile(self, user_id, profile_data):
        # Code to update user profile
        pass
```

##### After

By applying Context-less Architecture, user management and authentication are separated into clear contexts.

```python
class Authentication:
    def login(self, username, password):
        # Code to handle login
        pass

class UserProfile:
    def update_profile(self, user_id, profile_data):
        # Code to update user profile
        pass
```

These examples demonstrate the transformation from mixed, confusing contexts to clean, well-defined contexts by applying the Context-less Architecture pattern. This approach is especially beneficial when working with GitHub Copilot, considering its limitations in handling large and mixed contexts.

With this architecture, developers, and also GitHub Copilot, can focus on individual components, ensuring that the AI comprehends and accurately contributes to the code development.

### Exercise

- **Exercise 1**: Implement a small context-contained component using GitHub Copilot, and reflect on how limiting the context enhances its understanding.
- **Exercise 2**: Create a communication system between context-contained components with Copilot, evaluating its performance within confined contexts.
- **Exercise 3**: Review the overall architecture, considering the synergies and challenges with GitHub Copilot, and plan potential refinements.

### Checklist for Further Learning

- How can I consistently apply the Context-less Architecture pattern with GitHub Copilot to achieve optimal results?
- What strategies can ensure that I provide the right context size to maximize Copilot's accuracy?
- What might be the challenges in implementing this pattern across different projects, and how can I adapt accordingly?
- How can I continue to evolve and refine my use of Context-less Architecture with GitHub Copilot in various development scenarios?
