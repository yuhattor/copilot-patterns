# Generating Code from Comments

GitHub Copilot can also generate new code based on conditions specified by developers. For example, you can generate code by specifying the following conditions:

You can specify the following conditions to generate a new function:

```txt
// Function name: calculateAverage
// Function argument: numbers (array)
// Function return type: number
```

By specifying these conditions, Copilot generates the following code:

```ts
function calculateAverage(numbers: number[]): number {
    // Calculate the average of the array
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

You can provide more complex definitions as well.
