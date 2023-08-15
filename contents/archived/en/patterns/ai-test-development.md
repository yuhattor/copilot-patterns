# Test Development with AI

## Description

It is difficult to expect test case coverage without providing context to AI when using GitHub Copilot for code generation.
To write effective test cases, tools such as GitHub Copilot and ChatGPT should be used.

## Context

GitHub Copilot is an AI-powered code generation tool aimed at reducing manual coding by programmers.
With GitHub Copilot, AI can generate great code for you using syntax and approaches you may not be familiar with.
However, code that is less readable for you can decrease maintainability.
Therefore, it is important to prepare solid test code even while using GitHub Copilot.
Test code plays an important role in ensuring the quality of the program, and the coverage of test cases for automatically generated code is essential.

## Problem

When writing test code using GitHub Copilot, it is difficult to generate test code with sufficient coverage without providing detailed context.

For example, let's use GitHub Copilot to write the following test code that performs multiplication of two numbers.

```py
def multiply(a, b):
    return a * b
```

Using GitHub Copilot, you can easily generate test code for this code.

```py
import unittest

# Write test code for multiply()
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

Now we know that GitHub Copilot can be used for TDD.
However, were the test cases introduced here really good code?
"No way!!" The test code provided by GitHub Copilot is far from being excellent test cases.

Here are some issues to point out.
Firstly, there is duplication in the tests.
Some test cases expect the same results.
This means duplication in the tests and executing unnecessary tests.

The second problem is that errors are not being detected.
In this test case, we are confirming that the multiply() function is working as expected, but it cannot detect errors if they occur.
For example, there is no process to return an error if a string type is passed.

If we pass the following process using the multiply() function that passed the test this time, we can see that it does not work as expected:

```py
print(multiply(2, "Hello World!"))
# Hello World!Hello World!
```

There was duplication in the examples shown and errors were not being detected.
If you were to write the code, it might be better to write it like this:

In the following case, we communicate with GitHub Copilot while specifying the conditions one by one.

```py
# Write the test code for multiply() according to the following conditions.
# Condition: Include successful cases
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        # Condition: Include failure cases
        self.assertIsNot(multiply(2, 3), 7)
        # Condition: Confirm that the return type is numeric
        self.assertIsInstance(multiply(2, 3), int)
```

It has improved a lot compared to before, but it still lacks comprehensiveness.
So how can we make better use of GitHub Copilot to write more comprehensive test cases?

## Solution

When using GitHub Copilot to write test code, it is necessary to provide detailed context.
Using natural language processing models such as ChatGPT, it is possible to create more comprehensive test cases.

Let's pass a prompt like the following to ChatGPT:

> When writing test code for the following code without any omissions, what are the test cases/conditions? Please list them.
> ```py
> def multiply(a, b):
>     return a * b
> ```

Then ChatGPT returns results that look like wonderfully comprehensive test cases.

> The following are examples of test cases that should be included in the test code for the multiply() function:
>
> * When two positive integers are input, confirm that the correct result is returned.
> * When two negative integers are input, confirm that the correct result is returned.
> * When one positive integer and one negative integer are input, confirm that the correct result is returned.
> * When one input is 0, confirm that the result is 0.
> * When one input is a decimal number, confirm that an error occurs.
> * When one input is a string, confirm that an error occurs.
> * When a non-integer input is given, confirm that an error occurs.

Based on the above results, the following test code was written with GitHub Copilot.
It looks much better now:

```py
# Write the test code for multiply() according to the following conditions.
# Condition: Include successful cases
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # When two positive integers are input, confirm that the correct result is returned.
        self.assertEqual(multiply(3, 4), 12)
        # When two negative integers are input, confirm that the correct result is returned.
        self.assertEqual(multiply(-3, -4), 12)
        # When one positive integer and one negative integer are input, confirm that the correct result is returned.
        self.assertEqual(multiply(3, -4), -12)
        # When one input is 0, confirm that the result is 0.
        self.assertEqual(multiply(3, 0), 0)
        # When one input is a decimal number, confirm that an error occurs.
        self.assertRaises(ValueError, multiply, 3, 0.1)
        # When one input is a string, confirm that an error occurs.
        self.assertRaises(ValueError, multiply, 3, "a")
        # When a non-integer input is given, confirm that an error occurs.
        self.assertRaises(TypeError, multiply, 3, "a")
```

However, this is not perfect either.
Whether it is necessary to confirm that an error occurs when one input is a decimal number depends on the implementation, and the last two test cases test the same error.
There is still room for improvement, but it is great that we can reach this level in an instant at the beginning of writing test code.

## Resulting Context

When using GitHub Copilot to generate code automatically, attention must be paid to the comprehensiveness of the test code.
By providing detailed context and using natural language processing models such as ChatGPT, it is possible to create more comprehensive test cases.
However, it should be noted that it is not possible to automatically generate perfect test code, and manual correction is necessary.
Test code is very important for ensuring program quality, and having comprehensive test cases is essential.
