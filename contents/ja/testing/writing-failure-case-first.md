---
title: "失敗ケースを最初に書く"
description: "GitHub Copilot はあなたの実装を読み取り、それに基づいてテストケースを生成します。そのため GitHub Copilot 成功ケースに対してのみテストケースを生成する傾向があります。失敗ケースを忘れないように注意してください。"
category: testing
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv0
aliases:
  - /docs/v/ja/testing/writing-failure-case-first
---

## 失敗ケースを最初に書く

[<img src="https://img.shields.io/badge/Lv0-Pattern_Idea-blueviolet">](https://github.com/orgs/AI-Native-Development/projects/1/)

> 失敗ケースを最初に書くことは開発において重要なことではありますが、GitHub Copilotにテストケースを適切に提案させる方法について、ベストプラクティスを見つけ出す必要があります。

### Description

開発サイクルにおいて、テストケースの作成は重要な側面です。GitHub Copilot を使用すると、実装を読み取り、それに応じてテストケースを生成するため、さらに便利になります。一方で GitHub Copilot は成功ケースの生成に非常に効果的ですが、失敗ケースを見落とさないようにすることが重要です。最初に失敗ケースを考慮すると、より堅牢なコードにつながることがあります。

#### Example

これの重要性を示すために、2つの数値を割る関数を考えてみましょう。GitHub Copilot は、成功ケースをカバーするテストケースを提案するかもしれません。しかし、分母がゼロの場合はどうでしょうか？

```python
def divide(a, b):
  return a / b

# Failure test case
def test_divide_by_zero():
  # <YOUR CODE AND GITHUB COPILOT SUGGESTION HERE>
```

### Exerecise

- **エクササイズ1**: 2つの数字を掛ける関数を書き、成功ケースと失敗ケースの両方を含めてください（大きな数字の掛け算などのエッジケースを考慮してください）
- **エクササイズ2**: プロジェクト内の既存のコード片を分析し、欠落している失敗ケースを特定してください。これらのテストケースを書いてみましょう。
- **エクササイズ3**: 次のプロジェクトでTDDのアプローチを実装し、実際の実装よりも先に失敗テストケースを書くようにし、これが開発プロセスにどのように影響するかを考えてみてください。

### Checklist for Further Learning

- 最近のコードで全ての潜在的な失敗ケースを考慮しましたか？
- テストスイートに一貫して失敗テストケースを含めていますか？
- チームがテストケースの作成においてTDDのマインドセットを採用するように、どのように促進できますか？
