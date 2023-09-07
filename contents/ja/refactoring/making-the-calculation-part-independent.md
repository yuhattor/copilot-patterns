---
title: "計算ロジックを独立させる"
description: "大規模言語モデルは現時点では計算が得意ではありません。計算部分を別の関数に移動することで、開発と保守が容易になります。"
category: refactoring
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/v/ja/refactoring/making-the-calculation-part-independent
---

## 計算ロジックを独立させる

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

ソフトウェア開発の急速に進化する世界で、GitHub Copilot のようなツールに頼ることで、開発プロセスを強化できます。しかし、複雑な計算を行う際、大規模言語モデルの現行バージョンには限界があるかもしれません。これに対処するため、開発者は計算部分を別の関数に移動してコードをリファクタリングすることができます。これにより、コードの保守性、可読性が向上し、さらに AI ツールをつかったテストや開発が容易になります。金融ソフトウェアシステムを構築している開発者が、利息計算をユーザーインターフェイスロジックから分離する必要がある場合を想像してみてください。毎回 GitHub Copilot が特定のコードを書き換えるたびにロジックが正しいかを検証するのは非常に厄介な作業です。この複雑な計算を分離することで、柔軟でより耐久性のある AI と協働できるコードベースを作成します。

#### Example

**計算と注文合計の処理**

計算ロジックが他の機能と混ざっていた場合は以下のようになります。

```python
def handle_order(order_items):
    tax_rate = 0.05
    total = 0
    for item in order_items:
        total += item['price']
    total += total * tax_rate
    process_payment(total)
    ship_order(order_items)
    return total
```

一方で、計算ロジックを別の関数に移動すると、以下のようになります。

```python
def calculate_total(order_items, tax_rate=0.05):
    subtotal = sum(item['price'] for item in order_items)
    total = subtotal + (subtotal * tax_rate)
    return total

def handle_order(order_items):
    total = calculate_total(order_items)
    process_payment(total)
    ship_order(order_items)
    return total
```

ここで、`calculate_total` 関数は注文合計に関連するすべての計算を処理し、`handle_order` 関数は支払いの処理や注文の発送など、他の関連機能を処理します。

### Exercise

- **エクササイズ1**: プロジェクト内のコードの一部で、計算ロジックが他の機能と混ざっている部分を特定し、上記で説明したパターンを使用してリファクタリングしてください。
- **エクササイズ2**: 計算部分と非計算部分の両方に対してテストを書き、それらが独立して意図通りに機能することを確保してください。

### Checklist for Further Learning

- コードベース内の計算ロジックを隔離できる他のエリアはどのように特定できますか?
- 計算ロジックの分離が新しいエラーや複雑さを導入しないように、どのような戦略を使用できますか?
- この分離は、アプリケーションのより広いアーキテクチャと設計原則とどのように一致しますか?
