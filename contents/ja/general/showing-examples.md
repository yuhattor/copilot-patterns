---
title: "例示によるコード生成"
description: "GitHub Copilot では与えられた例からのコード生成が可能です。"
category: general
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/v/ja/general/showing-examples
---

## 例示によるコード生成

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

GitHub Copilotを使用して、開発者は提供された例に基づいてコードを生成できます。特定の出力を生成するコードが期待される場合、これは非常に便利です。このパターンでは、例としてJSONを生成するなど、Ruby on Rails のモデルを作成する方法を探ります。

#### Example

以下のサンプルは、コメント内で例を提供し、GitHub Copilot に対応するモデルを作成する Ruby on Rails コードを生成するように頼む方法を示しています。

```bash
# 以下のJSONを作成するコード生成の例:
# {
#   "name": "John Smith",
#   "age": 30,
#   "description": "これはサンプルの説明です。",
#   "country": "Japan",
#   "title": "Customer Success Architect",
#   "email": "johnsmith@example.com"
# }
rails g model users name:string age:integer description:text country:string title:string email:string
```

### Exercise

- **エクササイズ 1**: 以下の例に基づいて、書籍のモデルを作成する Ruby on Rails のコードを生成してください。
  ```json
  {
    "title": "Book",
    "author": "Jane Doe",
    "price": 19.99
  }
  ```
- **エクササイズ 2**: JSONの例で異なる属性とタイプを試し、対応する Rails のモデル生成コードを生成してください。
- **エクササイズ 3**: Rails プロジェクトで生成されたコードをテストし、期待されるモデルを作成することを確認してください。

### Checklist for Further Learning

- 生成されたコードは、与えられた例を正確に反映し、適切なコードを作成していますか?
- 提供された例からコードを生成する際の主要な考慮点や課題は何でしたか?
- 特定のプロジェクト要件に合わせて、生成されたコードをさらにカスタマイズまたは最適化するにはどうすればよいですか?
