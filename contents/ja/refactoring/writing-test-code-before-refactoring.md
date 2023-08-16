Sure, here's the translated version of the documentation you provided:

---
name: "リファクタリング前のテストコードの記述"
description: "GitHub Copilotを使用すれば、コードの変更は非常に簡単ですが、提案されたコードが常に正しいわけではありません。リファクタリング前にテストを記述することは非常に重要です。これは、GitHub Copilotを使用する際も同じです。"
category: "リファクタリング"
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: 100
---

## リファクタリング前のテストコードの記述

<img src="https://img.shields.io/badge/Lv2-実用的なパターン-green">

### Description

ソフトウェア開発の現代世界において、GitHub Copilotのようなツールが手元にあると、リファクタリングは楽しく魅力的なタスクと見なされることがあります。変更を加えることは非常に簡単ですが、適切なテストがない場合、最も有望なコードの変更でも予期せぬ結果につながることがあります。このパターンは、コードをリファクタリングする前にテストを記述して機能が一貫していることを確認する重要性を強調しています。テストを安全ネットと考えてください。問題が深刻化する前に問題を検出します。

#### Example

ショッピングカートの合計価格を計算する関数があるとし、これをより明確にリファクタリングしたいと考えたとします。以下は元のコードです: 

```python
def total_price(items):
    return sum(item['price'] * item['quantity'] for item in items)
```

リファクタリング前に、既存の機能が保持されていることを確認するためにテストを記述します: 

```python
def test_total_price():
    items = [
        {'price': 5, 'quantity': 2},
        {'price': 3, 'quantity': 1}
    ]
    assert total_price(items) == 13
```

これでコードをリファクタリングして、可読性を向上させることができます: 

```python
def total_price(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total
```

テストはまだ合格しますので、リファクタリングによって期待される結果が変わっていないことを保証します。

### Exercise

- **エクササイズ 1**: リファクタリングが必要な関数を記述し、それに対応するテストを記述します。
- **エクササイズ 2**: テストが合格することを確認しながら関数をリファクタリングします。
- **エクササイズ 3**: リファクタリングした関数に誤った変更を加えてエラーが発生する状況を模倣し、テストがエラーを検出する過程を観察します。

### Checklist for Further Learning

- コードの重要な側面をすべてカバーするためにテストがどのように確認されるか? 
- 選択したプログラミング言語で、テストを記述して実行するためのツールやフレームワークは何か? 
- リファクタリング時にテスト駆動開発（TDD）のプラクティスをどのように適用できるか? コードを書いた後にテストを書くとどのように異なるか? 
- テストを整理するためのベストプラクティスは何か? コードが進化するにつれてどのようにメンテナンスや更新ができるか? 