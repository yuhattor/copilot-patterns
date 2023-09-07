---
title: "ハイレベルアーキテクチャを先に"
description: "ハイレベルのコンテキストを最初に提供し、明示的な指示を提供するコメントとコードに続きます。"
authors: [yuhattor]
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/v/ja/design-pattern/high-level-architecture-first
---

## ハイレベルアーキテクチャを先に

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

複雑なシステムを開発するとき、いきなり細部のコードに飛び込み、プログラムの全体的なアーキテクチャを見失うことはよくあることです。このような事が繰り返されると、同時に GitHub Copilot も全体的なアーキテクチャを見失うことに繋がります。これは誤解やエラーの原因となってしまいます。開発において、プログラムのハイレベルなアーキテクチャを先に設計し、コードの各部分の機能と目的についてコメントしていくことにより、GitHub Copilot も文脈をよりよく理解し、より的確な提案をすることができます。

#### Example

ウェブアプリケーションでのAPIエンドポイントファイルを考えてみましょう。初期に設計を自然言語で提案することは、各エンドポイントの機能を GitHub Copilot に理解させるのに役立ちます。

```rb
# GET /items
# - アイテムのリストを取得します。
# - 応答でアイテムのコレクションを返します。
# 
# POST /items
# - 新しいアイテムを作成し、コレクションに追加します。
# - リクエストでアイテムのパラメーターが必要です。
# - 成功時に成功メッセージとともにカートページにリダイレクトします。
# - 失敗した場合、新しいアイテムのフォームを表示します。
# 
# GET /items/:id
# - 特定のIDを持つアイテムを取得します。
# - URLパラメーターとしてアイテムのIDが必要です。
# - 応答で要求されたアイテムの詳細を返します。
# ...
```

### Exercise

- **エクササイズ**:  バックエンドの簡単な API について、各エンドポイントに対するコメントを含め、ログインと登録システムのハイレベルアーキテ クチャのアウトラインを作成します。

### Checklist for Further Learning

- コードの詳細を書く前に明確なロードマップを確立しましたか?
- GitHub Copilot は、ハイレベルのコメントを読むだけで、ファイルの目的を理解できますか?
- このパターンをコードベース全体で一貫して適用していますか?
