---
title: "コードからコメントの自動生成"
description: "与えられたコードからコメントの生成をします"
category: general
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv3
aliases:
  - /docs/v/ja/general/code-to-comment
---

## コードからコメントの自動生成

[<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

GitHub Copilot はコードからコメントを生成できます。既存のコードが十分なコメントを欠いている場合や、他の開発者がコードを理解するのを助けるために、GitHub Copilot を使ってコメント形式で自動的に説明を生成しましょう。

#### Example

以下のサンプルは、与えられた数より小さい素数をリストするエラトステネスのふるいのアルゴリズムを示しています。このコードにはコメントが含まれていませんが、GitHub Copilotはコードの機能を説明するコメントを作成しています。

コメントなしのコードはこちらです:

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

GitHub Copilotがそれを説明するコメントを追加する方法は次のとおりです:

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

- **エクササイズ**: 次の関数の先頭にあるコードに適切なコメントを生成してください:
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

- 生成されたコメントは、コードの機能とアルゴリズムを適切に説明していますか?
- コメントは他の開発者がコードを理解するのに役立っていますか?
- 生成されたコメントが間違っている場合、その理由は何だと思いますか?
