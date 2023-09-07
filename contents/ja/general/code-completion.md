---
title: "コード補完"
description: "GitHub Copilot によるシンプルなコード補完"
category: general
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv3
aliases:
  - /docs/v/ja/general/code-completion
---

## コード補完

[<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

GitHub Copilot の最もシンプルな使用法のひとつはコード補完です。コード補完は、開発者がタイピングする際に潜在的なコードスニペットを提供することで開発者の生産性を向上させます。例えば、JavaScript の関数を定義することを想像してみてください。以下のコードを入力する際に、GitHub Copilot は関数内で使用できる潜在的なコードを提案します。

#### Example

##### 入力コード

```javascript
function calculateSum(a, b) {
    // Enter your code here
}
```

##### Copilot による提案結果

```javascript
function calculateSum(a, b) {
    // Enter your code here
    const sum = a + b;
    return sum;
}
```

### Exercise

- **エクササイズ 1**: GitHub Copilot の提案を活用して `calculateSum(a, b)` 関数を完成させます。異なるプロンプトや部分的なコード入力が Copilot による提案にどう影響するかを探求します。

### Checklist for Further Learning

- あなたのコードの出力は提供されたサンプルコードに似ていましたか?
- 出力されたコードは堅牢ですか? エラー処理は考慮されていますか? されていない場合どうすればよいですか?
- より正確なコードを書くためにどのようなプロンプトや文脈を追加できますか?
