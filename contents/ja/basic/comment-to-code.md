# コメントからコードを生成

GitHub Copilotは、開発者が指定した条件に基づいて、新しいコードを生成することもできます。例えば、以下のような条件を指定してコードを生成することができます。

例えば、以下の条件を指定して、新しい関数を生成することができます。

```txt
// 関数の名前: calculateAverage
// 関数の引数: numbers (配列)
// 関数の戻り値の型: number
```

この条件を指定すると、Copilotは以下のようなコードを生成します。

```ts
function calculateAverage(numbers: number[]): number {
    // 配列の平均を計算する
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

より複雑に定義をすることができます。
