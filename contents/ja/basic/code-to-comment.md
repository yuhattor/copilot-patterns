# コメント生成

GitHub Copilot はコードを生成するエンジンですが、コードからコメントの生成することができます。
例えばコメントがない以下のようなエラトステネスの篩のコードがあるとします。

```py
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

GitHub Copilot は以下のようなメソッドの解説のコメントを書くことができます

```py
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

また、コードからコードの解説を書き出すことができ、エンジニアは他の人のコードを早く理解することができます。

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # Description of the algorithm <- [Actual Prompt]
    # 1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
    # 2. Initially, let p equal 2, the first prime number.
    # 3. Starting from p, enumerate its multiples by counting to n in increments of p, and mark them in the list
    #    (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
    # 4. Find the first number greater than p in the list that is not marked. If there was no such number, stop.
    #    Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

## ステップの表示

GitHub Next の [Code Brushes](https://githubnext.com/projects/code-brushes/) にある LIST STEPS 機能を使うことで、同様のことが可能です。

```py
def calculate_sum(numbers):
    # initialize a variable to track the total
    total = 0
    # iterate over each number in the list
    for number in numbers:
        # add the number to the total
        total += number
    # return the total
    return total
```

## Code to Document

コードが大規模な場合、ChatGPT や Bing などを使って解説の出力をもらうのも一つの方法です。
コード全体の概要を知りたいときはチャット形式のAIツールを使うと良いでしょう。
