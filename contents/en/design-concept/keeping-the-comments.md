---
name: "Keeping the comments in the codebase"
description: "Keep the comments but make them clearer and more readable."
category: "design-pattern"
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: 100
---

## Keeping the Comments in the Codebase

Keep the comments but make them clearer and more readable.

### Description

When dealing with complex algorithms or intricate business logic, comments are an essential tool for conveying understanding. Detailed comments allow future developers to spend less time deciphering the code and more time innovating and building upon it. This pattern highlights the necessity and implementation of clear, extensive comments that facilitate the comprehension and maintenance of code.
It is also a good idea to specify other functions and variables to be referenced in the function.
You can also improve the quality of the comments themselves by using GitHub Copilot.

#### Samples

Below is an example of a longer comment implementation for a complex function:

```python
# This function takes a list of integers `numbers` as input and returns a new list
# containing only the prime numbers found in the input. Prime numbers are numbers 
# greater than 1 that have no divisors other than 1 and themselves.
#
# Parameters:
#     numbers (List[int]): A list of integers to be filtered for prime numbers.
# Returns:
#     List[int]: A new list containing only the prime numbers from the input.
def filter_primes(numbers):
    if not numbers:
        return []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in numbers if is_prime(x)]
```

### Exercise

- **Exercise 1**: Write a similar detailed comment for a function in your project that has complex logic.
- **Exercise 2**: Collaborate with a team member to review each other's comments. Focus on clarity, completeness, and the alignment of comments with the actual functionality of the code.

### Checklist for Further Learning

- Have I considered visual aids like diagrams in comments to further ease understanding?
- Do I review and update comments as code changes to ensure they remain accurate and helpful?
