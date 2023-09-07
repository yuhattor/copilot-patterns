---
title: "コメントからコードを生成"
description: "GitHub Copilot では自然言語のコメントからコードを生成することができます。"
category: general
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv3
aliases:
  - /docs/v/ja/general/comment-to-code
---

## コメントからコードを生成

[<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

コードからコードを生成するコード補完のテクニックと同様に、最もベーシックな GitHub Copilot のテクニックです。GitHub Copilot は、開発者が提供した特定のテキストに基づいて新しいコードを生成することができます。コメントの形式で条件を定義することで、GitHub Copilot は要件に応じたコードを作成することができます。

#### Example

以下は、コメントを通じて GitHub Copilot に関数を作成するよう指示する方法です: 

```javascript
// Function name: calculateAverage
// Function arguments: numbers (array)
// Return type of the function: number
```

これらのコメントに基づいて、Copilot は次のようなコードを提案します:

```javascript
function calculateAverage(numbers: number[]): number {
    // calculate the average of the array
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

### Exercise

- **エクササイズ 1**: 配列内の最大数値を計算する関数を作成するよう Copilot に指示するコメントを書いてください。以下の仕様を使用してください: 

```javascript
// Function name: calculateMax
// Function arguments: numbers (array)
// Return type of the function: number
```

- **エクササイズ 2**: さまざまな数値セットで生成された関数をテストし、正しい最大値を返すかどうかを確認してください。

### Checklist for Further Learning

- 生成されたコードは、指定された条件に基づいていますか?
- コードの機能は正しく実装されていますか?
- より複雑な条件定義のためにコメントを書く適切な方法は何ですか?
- より多くのコンテキストを与えるために、キーボードだけでなく、OS の音声入力も使ってみましょう。
