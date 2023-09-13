---
title: "コンテキストレス・アーキテクチャ"
description: "コーディングをより小さなコンテキストに限定し、プログラムのアーキテクチャを疎結合にする"
authors: [yuhattor] 
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv0
aliases:
  - /docs/v/ja/design-pattern/context-less-architecture
---

## コンテキストレス・アーキテクチャ

[<img src="https://img.shields.io/badge/Lv0-Pattern_Idea-blueviolet">](https://github.com/orgs/AI-Native-Development/projects/1/)

> 疎結合アーキテクチャ自体も多くの場合推奨されており、このパターンはその考え方に合致しています。しかし、AIを活用した開発の文脈をより広範なアーキテクチャの議論と結びつけ、それを正当化するためには、より多くの議論が必要です。ぜひディスカッションを始めましょう!

### Description

コンテキストレス・アーキテクチャは、システム内のより小さく、明確に定義されたコンテキストにコーディングを限定するデザインパターンです。複雑なプログラムを疎結合で独立したコンポーネントに分割することで、このアーキテクチャは保守性、拡張性、柔軟性を向上させます。

GitHub Copilot のような AIツールと連携する際、その性質と制限を理解することが不可欠です。現在の GitHub Copilot は AGI (Artificial General Intelligence) ではないため、限定された正確なコンテキスト内で最も効果的に動作します。特定のニーズに焦点を当てることで、開発者は GitHub Copilot の正確性と効率を最大化することができます。

キーとなるのは、各コンポーネントが特定の目的に役立つ疎結合なシステムを作成することです。このアプローチは GitHub Copilot の制限と合致しており、開発者がツールをより効果的に使用して、モジュラーで堅牢なソフトウェアを構築することができます。
**一方で、ツールにあわせてシステムのデザインを決めることは本質的なことではありません。**
このパターンは現実のプロジェクトやプロダクトにおいて、疎結合であることが意味を成す場合に、AI の開発における活用を追加で考えることで、より効果的に開発速度が上がることを目的としています。

#### Example

##### Before

ここでは、ユーザー管理と認証が混ざり合っており、コンテキストが不明確で絡み合っています。

```python
class UserManager:
    def create_user(self, username, password):
        # Code to create user
        pass

    def login(self, username, password):
        # Code to handle login
        pass

    def update_user_profile(self, user_id, profile_data):
        # Code to update user profile
        pass
```

##### After

コンテキストレス アーキテクチャを適用することで、ユーザー管理と認証が明確なコンテキストに分離されます。

```python
class Authentication:
    def login(self, username, password):
        # Code to handle login
        pass

class UserProfile:
    def update_profile(self, user_id, profile_data):
        # Code to update user profile
        pass
```

これらの例は、コンテキストレス・アーキテクチャ パターンを適用することで、混在して混乱しがちなコンテキストを、すっきりと明確に定義されたコンテキストに変換することを示しています。
このアプローチは、GitHub Copilot で作業する場合に特に有益で、大規模で混在したコンテキストを処理する上でのGitHub Copilot の限界を考慮する必要があります。

このアーキテクチャにより、開発者はもちろん、GitHub Copilotも個々のコンポーネントに集中することができ、AIがコードを理解し、正確にコード開発にさらに貢献できるようになります。

### Exercise

- **エクササイズ 1**: GitHub Copilot を使用して小さなコンテキストでコンポーネントを実装し、コンテキストの制限が理解を高める方法を反映させます。
- **エクササイズ 2**: コンテキストが制限されたコンポーネント間の通信システムを GitHub Copilot で作成し、限定されたコンテキスト内でのパフォーマンスを評価します。
- **エクササイズ 3**: 全体的なアーキテクチャを見直し、GitHub Copilot との連携の相乗効果と課題を考慮し、潜在的な改良を計画します。

### Checklist for Further Learning

- GitHub Copilot と共にコンテキストレス アーキテクチャパターンを一貫して適用し、最適な結果を達成するためにはどうすればよいですか?
- GitHub Copilot の精度を最大化するために、正しいコンテキストサイズを提供するための戦略は何ですか?
- さまざまなプロジェクトでこのパターンを実装する際の課題は何でしょうか。
- さまざまな開発シナリオにおいて、GitHub Copilot を使ったコンテキストレスアーキテクチャの使い方を進化させ、洗練させていくにはどうすればよいでしょうか。
