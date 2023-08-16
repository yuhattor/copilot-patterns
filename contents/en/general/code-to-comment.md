---
name: "Code to Comment"
description: "Generating comments from code"
category: "general"
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: 100
---

## Code to Comment: Generating Comments from Code

<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">

### Description

GitHub Copilot can generate comments from code. When existing code lacks sufficient comments, or to assist other developers in understanding the code, GitHub Copilot can automatically generate explanations in comment form. The following sample demonstrates the Sieve of Eratosthenes algorithm to list prime numbers less than a given number. While this code does not contain comments, GitHub Copilot can create comments to describe the code's functionality.

#### Example

Here's the code without comments:

```python
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

Here's how GitHub Copilot can add comments to explain it:

```python
# Write the description of the method here <- [Actual Prompt]
# Input: n - the number of primes to return
# Output: a list of the first n primes
# Example: eratosthenes_sieve(5) -> [2, 3, 5, 7, 11]
# Note: this is a very inefficient way to find primes, but it is easy to understand
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

### Exercise

- **Exercise**: Generate appropriate comments for the code at the top of the following function:

```python
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

### Checklist for Further Learning

- Do the generated comments adequately explain the code's functionality and algorithm?
- Are the comments helpful for other developers to understand the code?
- What do you think could be the reason for any incorrect comments that were generated?
