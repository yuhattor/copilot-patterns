---
title: "定義に移動"
description: "現在のファイルでの関数やクラスの定義へ移動して、GitHub Copilot が関連するコードをスニペットとして含めるようにします。"
category: client-tips
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/v/ja/client-tips/go-to-definition
---

## 定義に移動

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

> 2023年8月現在、GitHub Copilotはすべてのコードベースを読み込むわけではないので、このテクニックが必要になる場面が出てくるでしょう。一方、近い将来、GitHub Copilotでこのテクニックが不要になる可能性もあり、このテクニックは非常に限定的なものになるかもしれません。

### Description

複雑なコードベースで作業する際に、特定の関数やクラスの定義を見つけるためにファイル間をジャンプしたり、コードのレイヤーを検索するのは面倒です。"定義に移動" は、Visual Studio Code の便利な機能で、開発者が現在のファイル内の関数やクラスの定義にすばやく移動できるようにします。これによって生産性が向上するだけでなく、コード構造の理解も深まります。GitHub Copilot は開いているタブを読み取ります。"定義に移動" を使い実装を遡りながらファイルを開いていくことで、コードの奥深くにある定義に関連するコードスニペットも GitHub Copilot に渡すことができます。

#### Example

Visual Studio Codeの "定義に移動" 機能を使用するには、調べたい関数やクラスを右クリックし、"定義に移動" を選択します。
ショートカット `F12` も使用できます。以下のように行うことができます。

### Exercise

- **エクササイズ 1**: Visual Studio Code で複数のファイルを持つプロジェクトを開き、クラスまたは関数定義へ "定義に移動" を使用して移動してみましょう。
- **エクササイズ 2**: 変数、メソッド、クラスなど、異なる関数やクラスシンボルで "定義に移動" 機能の使用を練習して、その多様性を理解しましょう。

### Checklist for Further Learning

- "定義に移動" 機能は、全体のコーディング体験をどのように向上させることができますか?
- "定義に移動" 機能と GitHub Copilot の統合は、コードナビゲーションと理解にどのようにさらに支援することができますか?
- この機能が開発ワークフローで特に有用である場合を特定できますか?
