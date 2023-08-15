---
name: "Context-less Architecture"
description: "Confine coding to smaller contexts and loosely coupled program architecture"
authors: [yuhattor] 
category: "design-pattern"
platforms: [copilot, copilot-chat]
level: 100
---

## Context-less Architecture

Confine coding to smaller contexts and loosely coupled program architecture.

### Description

Context-less Architecture is a design pattern that emphasizes confining coding to smaller, well-defined contexts within a system. By breaking down complex programs into loosely coupled, independent components, this architecture enhances maintainability, scalability, and flexibility.

When working with GitHub Copilot, an AI-driven tool for code development, understanding its nature and limitations is essential. Since Copilot is not an Artificial General Intelligence (AGI), it operates most effectively within limited and precise contexts. Focusing on specific needs, developers can maximize Copilot's accuracy and efficiency.

In addition to the above, you should also be aware of the current token limit for large language models, affecting how much information can be processed in a single interaction. Please note that GitHub Copilot does not read all source code, further emphasizing the importance of limiting context for optimal results.

The key is to create a cohesive system where each component serves a specific purpose without unnecessary dependencies. This approach aligns with Copilot's limitations, allowing developers to utilize the tool more effectively to build modular and robust software.

#### Samples

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
- **Exercise 3**: Analyze a complex system with Copilot, breaking it into smaller, independent components, and assess the approach's effectiveness.
- **Exercise 4**: Collaborate with Copilot to write tests for your context-contained components, evaluating how well it assists in this specific architecture.
- **Exercise 5**: Review the overall architecture, considering the synergies and challenges with GitHub Copilot, and plan potential refinements.

### Checklist for Further Learning

- How can I consistently apply the Context-less Architecture pattern with GitHub Copilot to achieve optimal results?
- What strategies can ensure that I provide the right context size to maximize Copilot's accuracy?
- What might be the challenges in implementing this pattern across different projects, and how can I adapt accordingly?
- How can I continue to evolve and refine my use of Context-less Architecture with GitHub Copilot in various development scenarios?