---
title: "小さなコードチャンクで作業する"
description: "より少ないコンテキストで小さなコードの断片を扱うことで、GitHub Copilot の出力の品質が向上します。"
authors: [yuhattor] 
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv2
aliases:
  - /docs/v/ja/design-pattern/working-on-small-chunk
---

## 小さなまとまりで作業する

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

小さなコードの断片をより少ないコンテキストで扱うと、GitHub Copilot の出力が向上します。複雑なアプリケーションを構築していると想像してください。すべてを一度に生成しようとする代わりに、タスクを小さな部分に分割し、限定されたコンテキストを GitHub Copilot に提供します。このアプローチは開発プロセスを合理化するだけでなく、生成されたコードの品質も向上させます。

コンテキストレスなアーキテクチャをデザインの段階で考慮するアイデアもありますが、すべてのプロジェクトで疎結合のアーキテクチャを適用することは難しいです。また、AIツールの精度を高めるためにアーキテクチャデザインを変えるのは本末転倒です。このパターンでは、少なくとも作業環境でコンテキストができるだけ小さくなるように、小さなチャンクで作業することによりGitHub Copilot の提案を向上させることを目的としています。GitHub Copilot が、全体的なプロジェクトの複雑さに圧倒されることなく、手がかりの具体的なタスクを理解できるようにする、よりコントロールされた、正確で、効率的なコード生成が可能です。

#### Example

複雑な計算する関数を書くとしましょう。GitHub Copilot に全体の複雑な解決策を求める代わりに、いくつかの関数に分けて、それぞれの関数を生成するように求めます。このアプローチは、GitHub Copilot がより小さなコンテキストで作業することを可能にし、より正確なコードを生成します。

```python
def complex_calculation(n):
  # Ask GitHub Copilot to complete this function
```

```python
# Just write your code description by yourself
class complex_calculation:
  def __init__(self, n):
    self.n = n

  def foo_calculation(self):
    # Ask GitHub Copilot to complete this function

  def bar_calculation(self):
    # Ask GitHub Copilot to complete this function
```

### Exercise

- **エクササイズ 1**: 複雑なアルゴリズムを小さな部分に分割し、各部分のコードを GitHub Copilot で生成します。
- **エクササイズ 2**: タスクのハイレベルの説明を書き、狭いコンテキストで GitHub Copilot にコードを求めます。結果を比較します。
- **エクササイズ 3**: 個人的な開発プロセスを振り返り、タスクを小さなチャンクに分割することが有益であるエリアを特定します。

### Checklist for Further Learning

- コンテキストを絞り込むことが、GitHub Copilot の提案の精度にどのように影響しますか?
- GitHub Copilot により正確なコンテキストを提供するために、どのような戦略を使用できますか?
- GitHub Copilot の確率的な性質が、異なるシナリオでコードを生成する能力にどのように影響しますか?
- GitHub Copilot との小さなチャンクでの作業が、効果が少ないか、より困難である状況はありますか?
