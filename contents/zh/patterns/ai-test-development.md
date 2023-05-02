# 使用AI进行测试开发

## 描述

在使用 GitHub Copilot 进行代码生成时，如果没有为 AI 提供上下文，就难以期望生成具有足够覆盖率的测试用例。
除了 GitHub Copilot 外，还可以使用 ChatGPT 等工具来编写测试用例。

## 背景

GitHub Copilot 是一种通过人工智能实现代码自动生成的工具，旨在减少程序员手动编写代码的工作量。
使用 GitHub Copilot 可能会生成出您不熟悉的语法和方法的优秀代码。
然而，对于您来说可读性较差的代码可能会降低可维护性。
因此，即使使用 GitHub Copilot，编写良好的测试代码也是非常重要的。
测试代码对于保证程序质量发挥着重要作用，因此测试覆盖率是自动生成的代码所需的必要条件。

## 问题

使用 GitHub Copilot 编写测试代码时，如果不提供详细的上下文信息，就无法自动生成具有足够覆盖率的测试代码。

例如，使用 GitHub Copilot 编写以下代码进行两个数字的乘法。

```py
def multiply(a, b):
    return a * b
```

使用 GitHub Copilot，可以轻松地生成测试代码。

```py
import unittest

# 编写 multiply() 的测试代码
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 10), 50)
        self.assertEqual(multiply(7, 7), 49)
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(3, 3), 9)

unittest.main()
```

现在我们知道了 GitHub Copilot 也可以用于 TDD。然而，我们展示的测试用例真的是好的代码吗？
“天哪！” GitHub Copilot 提供的测试代码远远不能与出色的测试用例相媲美。

以下是一些问题指出：
首先，测试中存在重复。一些测试用例期望相同的结果，这意味着测试重复，执行了不必要的测试。

第二个问题是无法检测错误。这些测试用例确认 multiply() 函数按预期工作，但无法检测到错误。
例如，如果传递字符串类型，没有处理错误的操作。

如果使用 multiply() 函数进行以下处理，可以发现其行为不符合预期。

```py
print(multiply(2, "Hello World!"))
# Hello World!Hello World!
```

示例中存在测试重复和未检测到错误的问题。如果要编写代码，可能需要编写以下内容。

在以下情况下，通过逐行指定条件并与 GitHub Copilot 进行通信来编写 multiply() 的测试代码。

```py
# 按以下条件编写 multiply() 的测试代码。
# Condition: 成功和失败的情况都应包括在内
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        # Condition: 包括失败案例
        self.assertIsNot(multiply(2, 3), 7)
        # Condition: 确认返回值为数字类型
        self.assertIsInstance(multiply(2, 3), int)
```

现在测试覆盖率比之前有所提高。那么如何更好地利用 GitHub Copilot 编写具有足够覆盖率的测试代码呢？

## 解决方案

当使用GitHub Copilot编写测试代码时，需要提供详细的上下文信息。通过使用自然语言处理模型（如ChatGPT），可以创建更全面的测试用例。

让我们向 ChatGPT 提供以下提示，以编写给定代码的测试用例。

> 在编写以下代码的测试用例时，有哪些测试案例和条件需要考虑？请以项目符号的形式列出。
> ```py
> def multiply(a, b):
>     return a * b
> ```

然后，ChatGPT 将返回以下结果，看起来像是一个非常全面的测试用例。

> 下面是一个应该包含在 multiply() 函数测试用例中的示例。
>
> * 如果输入两个正整数，则确认返回正确的结果。
> * 如果输入两个负整数，则确认返回正确的结果。
> * 如果输入一个正整数和一个负整数，则确认返回正确的结果。
> * 如果输入一个为0的数字，则确认返回结果为0。
> * 如果输入一个小数，则确认会出现错误。
> * 如果输入一个字符串，则确认会出现错误。
> * 如果输入除整数外的任何内容，则确认会出现错误。

基于上述结果，我们使用 GitHub Copilot 编写了以下测试代码。它看起来更漂亮了。

```py
# 请按照以下条件编写 multiply() 的测试代码。
# 条件：包括成功的案例。
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # 如果输入两个正整数，则确认返回正确的结果。
        self.assertEqual(multiply(3, 4), 12)
        # 如果输入两个负整数，则确认返回正确的结果。
        self.assertEqual(multiply(-3, -4), 12)
        # 如果输入一个正整数和一个负整数，则确认返回正确的结果。
        self.assertEqual(multiply(3, -4), -12)
        # 如果输入一个为0的数字，则确认返回结果为0。
        self.assertEqual(multiply(3, 0), 0)
        # 如果输入一个小数，则确认会出现错误。
        self.assertRaises(ValueError, multiply, 3, 0.1)
        # 如果输入一个字符串，则确认会出现错误。
        self.assertRaises(ValueError, multiply, 3, "a")
        # 如果输入除整数外的任何内容，则确认会出现错误。
        self.assertRaises(TypeError, multiply, 3, "a")
```

然而，这也不是完美的。例如，我们需要根据实现的情况来确定是否需要确认输入小数时是否会出错，而最后两个测试用例测试了相同的错误。虽然我们仍然需要手动进行一些修正，但在编写测试代码的早期阶段，能够快速到达这一步骤是非常好的。

## 结果上下文

当使用GitHub Copilot自动生成代码时，需要注意测试代码的覆盖率。提供详细的上下文信息，并使用自然语言处理模型（如ChatGPT）可以创建更全面的测试用例。然而，自动创建完美的测试代码仍然是不可能的，因此需要手动进行一些修正。测试代码对于确保程序质量非常重要，具有全面的测试用例是必不可少的。
