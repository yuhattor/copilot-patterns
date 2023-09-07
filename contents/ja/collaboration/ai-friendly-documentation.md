---
title: "AIフレンドリーなドキュメンテーション"
description: "テキストベースのドキュメンテーションによってAIに親しみやすくします。AIはテキストベースのドキュメンテーションを読むことができますが、画像ベース や 複雑なエクセルやパワーポイントファイルなどのドキュメンテーションは読むことができません。"
authors: [yuhattor]
category: collaboration
level: lv1
aliases:
  - /docs/v/ja/copilot/ai-friendly-documentation
---

## AIフレンドリーなドキュメンテーション

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

AI を用いたコーディング支援ツールである GitHub Copilotの時代には、テキストベースで AI が容易にアクセスできるドキュメントが重要です。AI の時代では、Infrastructure as Code、データベーステーブル仕様、テスト要件などのファイルは、即座に実際のコードに変換できる可能性を持っています。複雑なエクセル、パワーポイントファイル、PDF、画像形式ではなく、テキストベースのドキュメントによって AI があなたのコーディングを協力に支援することができるようにになります。

以下のファイルがテキストベースであるか確認します:

- インフラストラクチャ定義
- データベーステーブル定義
- テスト仕様

#### Example

例えば、以下のようなマークダウンで書かれたテーブルがある場合、GitHub Copilot はマイグレーションファイルのベースを提供します。

```rb
# | No. | Item Name            | Type                        | Length | Decimal | Required | Primary Key | Remarks                |
# | --- | -------------------- | --------------------------- | ------ | ------- | -------- | ----------- | ---------------------- |
# | 1   | pass_document_id     | integer                     |        |         | Y        | Y           | Document ID            |
# | 2   | checkout_id          | integer                     |        |         | Y        | Y           | Unique Serial Number   |
# | ... | ...                  | ...                         | ...    | ...     | ...      | ...         | ...                    |
# | 15  | update_datetime      | timestamp-without-time-zone |        |         |          |             | Update Timestamp       |

# Create migration file of cooperation_pass public

class CreateGovernmentPass < ActiveRecord::Migration[7.0]
  def change
    # <Copilot Suggestion Here>

```

### Exercise

- **エクササイズ 1**: 既存のドキュメントをチェックし、テキストベースでないファイルをリストします。
- **エクササイズ 2**: テキストベースでないファイルのうちの1つをマークダウンまたはプレーンテキストファイルに変換し、以前の形式とのアクセシビリティを比較します。
- **エクササイズ 3**: リポジトリをスキャンし、テキストベースでないドキュメントがコミットされた場合に警告するスクリプトを書きます。

### Checklist for Further Learning

- チームメンバーがテキストベースのドキュメントの標準を守っていることをどのように確保できますか?
- 他にどんなチーム/プロジェクトのドキュメントがテキストで書かれていたら、開発の速度を上げることができますか?
- テキストベースのドキュメントの採用が AI ツール のGitHub Copilot を使った開発をどのように改善できますか?
