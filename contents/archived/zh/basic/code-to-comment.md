# 注释生成

GitHub Copilot 是一个生成代码的引擎，但也可以从代码中生成注释。
例如，如果有以下没有注释的埃拉托色尼筛代码。

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

GitHub Copilot 可以编写以下方法的解释性注释。

```py
# 在此处编写方法的描述 <- [实际提示]
# 输入：n-要返回的质数数量
# 输出：前n个质数的列表
# 示例：eratosthenes_sieve(5) -> [2, 3, 5, 7, 11]
# 注意：这是一种非常低效的查找质数的方法，但易于理解
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

此外，可以从代码中编写代码解释，使工程师能够更快地理解其他人的代码。

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # 算法描述 <- [实际提示]
    # 1.从2到n创建一串连续的整数列表：(2，3，4，...，n)。
    # 2.最初，令p等于2，即第一个质数。
    # 3.从p开始，通过计数到n的p倍来枚举它的倍数，并在列表中标记它们（这些将是2p，3p，4p，...；不应标记p本身）。
    # 4.在列表中找到大于p的第一个未标记的数字。 如果没有这样的数字，请停止。否则，现在让p等于这个新数字（即下一个质数），并从步骤3重复。
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

## 显示步骤

通过使用 GitHub Next 的 [Code Brushes](https://githubnext.com/projects/code-brushes/) 中的 LIST STEPS 功能，也可以实现类似的功能。

```py
def calculate_sum(numbers):
    # 初始化变量以跟踪总和
    total = 0
    # 遍历列表中的每个数字
    for number in numbers:
        # 将数字添加到总和
        total += number
    # 返回总和
    return total
```

## 代码到文档

对于大规模当代码规模很大时，另一种方法是使用 ChatGPT 或 Bing 等工具获得解释输出，以了解整个代码的概要。
