---
title: "構造化データからのオブジェクト生成"
description: "JSONなどの構造化データからオブジェクトを生成する方法"
category: general
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv2
aliases:
  - /docs/v/ja/general/object-generation-from-structured-data
---

## 構造化データからのオブジェクト生成

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

開発者にとって、構造化データの取り扱いは日常的なタスクです。JSONなどの形式のデータをプログラミング言語内のオブジェクトに変換することで、堅牢で保守性の高いコードを作成できます。例えば、ユーザーのリストがあり、このデータをアプリケーション内のユーザーオブジェクトに変換したい場合を想像してみてください。GitHub Copilot は、この変換プロセスをサポートし、煩雑な作業を一瞬で終わる簡単な作業に変えてくれます。

#### Example

以下は、与えられたJSONデータをユーザーオブジェクトのリストに変換するPythonの例です。

```python
import json

json_data = '[{"id": "1", "name": "Yuki Hattori"}, {"id": "2", "name": "George Hattori"}]'
users = json.loads(json_data)

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

user_objects = [User(user['id'], user['name']) for user in users]

for user in user_objects:
    print(user.id, user.name)
```

### Exercise

- **エクササイズ 1**: 異なる JSON 構造からオブジェクトを生成してみてください。例えば、ユーザーのアドレス情報を含むJSONなどです。
- **エクササイズ 2**: JSON 内のデータが欠落しているようなエッジケースを取り扱ってみてください。コードが適切に処理されるようにしてください。

### 学習のためのチェックリスト

- より複雑なデータ構造に適応するためにコードをどのように変更しますか?
- データをオブジェクトに変換する前に、どのような方法でデータの妥当性を確認できるでしょうか?
- このパターンを異なるプログラミング言語やフレームワークにどのように適用できますか?
