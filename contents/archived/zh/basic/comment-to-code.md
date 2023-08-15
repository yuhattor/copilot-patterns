# 从评论中生成代码

GitHub Copilot可以根据开发人员指定的条件生成新代码。例如，您可以指定以下条件以生成代码：

例如，您可以指定以下条件以生成新函数：

```ts
// 函数名称：calculateAverage
// 函数参数：numbers（数组）
// 函数返回值类型：number
```

指定这些条件后，GitHub Copilot将生成以下代码：

```ts
function calculateAverage(numbers: number[]): number {
    // 计算数组的平均值
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

您可以更复杂地定义条件。
