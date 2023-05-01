# Code Refactoring

Refactoring refers to modifying existing code to improve its quality and maintainability without changing its functionality.

GitHub Copilot makes code refactoring easier by understanding the structure of the code and suggesting candidate refactorings. For example, consider the following code:

```py
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
```

With GitHub Copilot, you can refactor this code to use the `sum()` function to calculate the sum of the list, as shown below. The argument and return types have also been made explicit.

```py
# Refactored calculate_sum() written below
def calculate_sum(numbers):
    return sum(numbers)
```

These features can be explicitly commanded to GitHub Copilot, as shown above, or you can use interactive tools like ChatGPT to perform refactoring more interactively. GitHub Copilot can suggest candidate refactorings to improve the quality of the code. Developers can consider these candidates and manually modify the code as needed. Refactoring like this improves code maintainability, and developers can code more efficiently.

It is very important to write tests when refactoring.
With tests, you can verify that the refactored code behaves the same way as before.
Especially when relying on AI tools for refactoring, GitHub Copilot may propose coding styles that you don't usually use.
Even if the code is excellent from a general programming standpoint, it may not be suitable for you or your organization.
When relying on AI for refactoring, consider how granular the proposed changes should be adopted.

On the other hand, GitHub Copilot can be useful for supporting Test-Driven Development (TDD).
TDD is a method of writing code by writing tests before writing code and writing code to pass the tests.
Using this method, developers can write code that passes tests and improves code quality.
