---
name: "Eliminating a tiny OSS dependency"
description: "Eliminating a tiny OSS dependency that can be actually implemented in a few lines of code"
authors: [yuhattor] 
category: "design-pattern"
platforms: [copilot, copilot-chat]
level: 100
---

## Eliminating a tiny OSS dependency

<img src="https://img.shields.io/badge/Lv0-Pattern_Idea-blueviolet">

{% hint style="info" %}
This may be of limited applicability. As more cases are discovered, this maturity level will increase.
{% endhint %}

### Description

Do you know about the left-pad issue? In 2016, the left-pad library was suspended from npm, causing well-known libraries that depended on it to cease working. left-pad is a simple JavaScript library that only fills the left side of a string with a specified number of characters, or spaces if not specified. Excluding blank lines, it's a simple code with only about 10 lines.

There are many ideas to avoid reinventing the wheel, On the other hand, we must also pay attention to external code that can have a significant impact. If the provided code's scope is very limited, it might be better to contain it internally rather than depending on an external source.

### Samples

Implementing a left-pad function can be done as shown below:

```ruby
def leftpad(string, length, char = ' ')
    string.rjust(length, String(char))
end
```

### Exercise

- **Exercise 1**: Implement the left-pad function that takes the string, length, and character to pad with. The default character should be a space.
- **Exercise 2**: Consider a scenario where multiple small external dependencies exist in a project. Identify a small utility function that can replace one such dependency and implement it.

### Checklist for Further Learning

- Have you considered the trade-offs between using an external dependency and implementing the code yourself?
- How might this pattern of eliminating tiny dependencies affect the maintainability of the code?
- What principles or guidelines can be used to decide when to replace a tiny external dependency with an internal implementation?
