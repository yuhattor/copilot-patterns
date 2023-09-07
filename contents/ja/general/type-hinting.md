---
title: "タイプヒンティング"
description: "動的型付けプログラミング言語を書く際にも型のヒントをしっかりと書くことで、GitHub Copilot の提案精度を向上させることができます。"
category: general
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/v/ja/general/type-hinting
---

## タイプヒンティング

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

動的型付けプログラミング言語の世界では、開発者は特に複雑なシステムでコードを理解する際に課題に直面することがよくあります。タイプヒンティングは、期待されるデータ型を明示的に宣言することで、明確さの層を追加します。
GitHub Copilot を使う際にもタイプヒンティングを使うことにより、コード提案の精度を高め、開発者と GitHub Copilot がより効率的にコードを書くのを支援します。

深くネストされた関数でプロジェクトに取り組んでいると想像してみてください。変数の型を追跡するのが複雑になります。タイプヒンティングの統合は、同僚の開発者にとってコードをより読みやすくすることにも繋がります。

#### Example

Python でタイプヒンティングを使用して関数を定義する方法は以下の通りです。

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

GitHub Copilot はこれらのタイプヒンティングを認識し、それに応じてコード提案を生成します。

### Exercise

- **エクササイズ 1**: タイプヒンティングを使用して、2つの文字列パラメータを取り、それらの連結を返す関数を書いてください。
- **エクササイズ 2**: プロジェクト内の既存のコード片をタイプヒンティングを含むように変換し、GitHub Copilot の提案の違いを観察してください。
- **エクササイズ 3**: 複数のメソッドを持つ複雑なクラスを作成し、すべてのパラメータと戻り値のタイプヒンティングを使用してください。

### Checklist for Further Learning

- コードベース全体でタイプヒンティングを一貫して使用していますか?
- タイプヒンティングの過剰な使用の潜在的な欠点を考慮しましたか、そしてコード内での適切なバランスをどのように見つけるかですか?
