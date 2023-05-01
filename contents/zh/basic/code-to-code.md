# 代码自动补全

GitHub Copilot 的最简单使用方式是代码自动补全。当开发者输入代码时，GitHub Copilot 会提供候选代码，从而提高开发者的生产力。

例如，假设您正在使用 JavaScript 定义函数。假设您正在输入以下代码：

```js
function calculateSum(a, b) {
    // 在此输入处理
}
```

此时，GitHub Copilot 可能会提供候选代码，用于函数内部的使用。例如，可能会提供以下代码：

```js
const sum = a + b;
return sum;
```

当开发者选择该候选代码时，以下代码将被插入函数内部：

```js
function calculateSum(a, b) {
    const sum = a + b;
    return sum;
}
```

## GitHub Copilot 的参考优先级

GitHub Copilot 将引用最近打开的几个相同语言的文件，计算相似性并确定要包含在提示中的文件。虽然当前的逻辑是不公开的，但是有一些关于逆向工程的记录（例如 [Copilot Explorer](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals#how-is-the-prompt-prepared-a-code-walkthrough)），可以查看。

## 注意事项

由于 GitHub Copilot 提供由 AI 生成的代码，自动生成的代码可能不完全准确。开发者需要检查生成的代码，并在必要时进行手动修正。因此，通过使用 GitHub Copilot 的代码自动补全功能，开发者可以减少手动输入代码的次数。