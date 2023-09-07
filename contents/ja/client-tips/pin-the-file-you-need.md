---
title: "便利なファイルのピン留め"
description: "宣言ファイルをはじめとした必要なファイルをピン留めして、GitHub Copilotに文脈を提供しやすくします"
category: client-tips
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv2
aliases:
  - /docs/v/ja/client-tips/pin-the-file-you-need
---

## 便利なファイルのピン留め

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

GitHub Copilot の性能は、提供されるコンテキストに依存します。GitHub Copilot はテキストの類似性で開いているタブを検索し、大規模言語モデルにスニペットを送信します。したがって、私たちは AI に提供したいコンテキストを慎重に考える必要があります。プログラミングでは、宣言ファイル（d.ts）、テストファイル、インターフェイスファイルなどが豊富なコンテキスト情報を含んでいます。Visual Studio Codeのピン留め機能を使用すると、これらのファイルを必要に応じて簡単にアクセスし、GitHub Copilotに効率的に情報を提供できます。

#### Example

Visual Studio Codeでファイルをピン留めする方法は次のとおりです:

1. ピン留めしたいファイルを開きます。
2. ファイルタブ上で右クリックします。
3. コンテキストメニューから"Pin Tab"を選択します。

### Exercise

- **エクササイズ 1**: 現在のプロジェクトで宣言ファイル（例: `.d.ts`ファイル）をピン留めし、GitHub Copilotと一緒に作業する際にアクセスが容易になることに注目してください。
- **エクササイズ 2**: 新しいインターフェイスファイルを作成し、ピン留めします。GitHub Copilotがこのファイルをどのように利用してより良いコード提案ができるのか探究してください。
- **エクササイズ 3**: プロジェクト内で複数のテストファイルをピン留めし、Copilotの助けを借りて新しいテストケースを書く際にどのように助けになるか観察してください。

### Checklist for Further Learning

- ピン留めするファイルの種類を変えると、GitHub Copilot との作業フローにどのような影響がありますか?
- Visual Studio Codeの他の機能は、GitHub Copilot との経験を向上させるためにどう活用できますか?
- 大量のピン留めファイルを管理して、常に GitHub Copilot に適切なコンテキストが利用可能であるようにするにはどうすればよいですか?
