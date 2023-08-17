---
name: "Making the calculation part independent"
description: "LLM is not good at calculating for now. Moving the calculation part to a separate function makes it easier to develop and maintain."
category: "refactoring"
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: 100
---

## Making the Calculation Part Independent

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

In the rapidly evolving world of software development, relying on tools like GitHub Copilot can enhance the development process. However, current versions of large language models may have limitations when handling complex calculations. To address this, developers can refactor their code by moving the computation part to another function. This improves code maintainability, readability, and makes it easier to test and develop with AI tools. Imagine a developer building a financial software system who needs to separate interest calculations from the user interface logic. Every time GitHub Copilot rewrites a particular piece of code, verifying that the logic is correct is a very cumbersome task. By separating this complex computation, you create a codebase that can work with a flexible and more durable AI.

#### Example

**Calculating and Handling Order Totals**

Before, when the calculation logic was mixed with other functionalities:

```python
def handle_order(order_items):
    tax_rate = 0.05
    total = 0
    for item in order_items:
        total += item['price']
    total += total * tax_rate
    process_payment(total)
    ship_order(order_items)
    return total
```

After, when the calculation logic is completely separated from other functionalities:

```python
def calculate_total(order_items, tax_rate=0.05):
    subtotal = sum(item['price'] for item in order_items)
    total = subtotal + (subtotal * tax_rate)
    return total

def handle_order(order_items):
    total = calculate_total(order_items)
    process_payment(total)
    ship_order(order_items)
    return total
```

Here, the `calculate_total` function takes care of all the calculations related to the order total, while the `handle_order` function handles other related functionalities, such as processing payment and shipping the order.

### Exerecise

- **Exercise 1**: Identify a portion of code in your project where the calculation logic is mixed with other functionalities and refactor it using the pattern described above.
- **Exercise 2**: Write tests for both the calculation part and the non-calculation part to ensure that they function as intended independently.

### Checklist for Further Learning

- How can I identify other areas in my codebase where the calculation logic can be isolated?
- What strategies can I employ to ensure that the separation of calculation logic doesn’t introduce new errors or complexities?
- How does this separation align with the broader architecture and design principles of my application?
