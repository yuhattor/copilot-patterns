# Code Refactoring

Refactoring refers to improving the quality of existing code and enhancing its maintainability by making changes. Code refactoring does not change the functionality of the code but aims to improve its quality.

GitHub Copilot makes it easier to refactor code.
GitHub Copilot can understand the structure of the code and provide candidates for recommended refactoring. For example, consider the following code:

```py
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
```

You can refactor this code using GitHub Copilot. Here's an example of a refactoring candidate provided by GitHub Copilot. 
This code has been rewritten to calculate the sum of a list using the sum() function. Also, the argument and return types have been made explicit.

```py
# Write the refactored calculate_sum() below

def calculate_sum(numbers):
    return sum(numbers)
```

You can instruct GitHub Copilot to perform these functions explicitly by commenting as shown above, or you can interactively refactor using tools like ChatGPT.
In this way, GitHub Copilot can provide candidates for refactoring to improve code quality. Developers can consider these candidates and manually modify the code as needed. Such refactoring enhances code maintainability and allows developers to develop code more efficiently.

It is crucial to have tests written when refactoring.
With tests, you can verify whether the refactored code behaves the same as before.
Especially when relying on AI tools for refactoring, GitHub Copilot may suggest code styles that you do not usually use.
Even if the code is excellent from a general programming perspective, it may not be suitable for you or your organization.
Consider the granularity of adoption when relying on AI for refactoring.

On the other hand, GitHub Copilot can be useful for supporting test-driven development (TDD).
TDD is a method of writing tests before writing code and then writing code to pass those tests.
Using this method, developers can write code that passes tests, improving the quality of the code.
