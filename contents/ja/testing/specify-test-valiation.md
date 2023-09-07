---
title: "テストコード生成の方法を指定する"
description: "テストコード生成の方法を指定する。使用するテストフレームワークや生成するテストケースの数などを指定します。"
category: testing
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv2
aliases:
  - /docs/v/ja/testing/specify-test-valiation
---

## テストコード生成の方法を指定する

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

テストに関する指示を具体的に示すことは、必要なシナリオをすべてカバーする良い方法です。"ユニットテストを追加する"といった曖昧な指示ではなく、テストフレームワークや生成するケースの数などの具体的な詳細を提供することができます。GitHub Copilotのようなツールを活用する際には、「JunitとMockitoを使用してユニットテストを追加し、少なくとも10種類の有効な/無効な入力の組み合わせをテストする」といった指定を行うことで、より正確で包括的な結果を得ることができます。

#### Example

Junit と Mockito を使用してテストコードを生成する場合、次のプロンプトを GitHub Copilot に提供できます:

```java
// JunitとMockitoを使用してユニットテストを追加する
// 少なくとも10種類の有効な/無効な入力の組み合わせをテストする
@Test
public void validateInput() {
  // ここにコードを記述
}
```

### Exercise

- **エクササイズ1**: Junit を使用して、異なる3つの有効な入力で単純なメソッドをテストするユニットテストを書いてみましょう。
- **エクササイズ2**: ユニットテストを拡張して、3つの異なる無効な入力を含め、例外が適切に処理されることを確認します。

### Checklist for Further Learning

- コード内のすべての重要なパスをテストする方法はどのように確保できるでしょうか?
- テストが必ず失敗するようにテストコードを書くことはできますか?
- コードベースが進化するにつれてテストを維持するためにどのような戦略をとることができますか?
