---
title: "Copilot スニペットハンドリング"
description: "GitHub Copilot は 大規模言語モデルを使用してコードを生成します。そして、大規模言語モデルにはトークンの制限があります。GitHub Copilot があなたのコード全てを見ていないことを理解する必要があります。"
category: client-tips
authors: [yuhattor] 
platforms: [copilot]
level: lv2
aliases:
  - /docs/v/ja/client-tips/copilot-snippet-handling
---

## Copilot スニペットハンドリング

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

> この情報は2023年8月現在のものですが、GitHub Copilotとその背後にあるLLMの進化に伴い、状況が変わる可能性があります。常にGitHubから最新の情報を得るようにしてください。

### Description

そして、GitHub Copilot は OpenAI の 大規模言語モデルを利用してコードを生成するため、トークンの数に制限があります。2023 年現在、GitHub Copilot はエディタで開いているコード全てを見ることができず、また AI もすべてのコードをトークンとして受け取るわけではありません。これは、ユーザーが GitHub Copilot に提供するコンテキストを慎重に制限する必要があることを意味しています。特筆すべきは、GitHub Copilot は外部リポジトリや GitHub.com / GitHub Enterprise Cloud に置かれたソースコードにはアクセスしていないということです。

GitHub Copilot が提案に使用するファイルは、主に現在開いているファイルとそれに隣接するタブファイル(基本的には同じファイル拡張子)です。
正確な提案をするためには、関連するファイルだけを開いておくことが不可欠です。
以下は、2023年8月時点のチェックリストです。 GitHub Copilot がスニペットとして含めるファイルの種類は将来変更される可能性がありますが、「不要なファイルを閉じる」などの実践は、GitHub Copilot を使用していない場合であっても、コーディングにプラスの影響を与える可能性があります。

- 参照する必要があるファイルを開く
- 不要なファイルを閉じる
- 参照したい 他の拡張子のファイル (例: .md, .csv) がある場合は、コピーしてコメントアウトする

#### Example

Pythonの関数を1つのタブで書いており、隣接するタブに似たような関数があるシナリオを考えてみましょう。GitHub Copilotはパターンを認識し、改善の提案を行うことができます。

```python
# タブ 1 (隣接)
def add_numbers(a, b):
    return a + b
```

```python
# タブ 2
def subtract_numbers(a, b):
    return a - b

answer = substruct_numbers(1, 2) + add_numbers( # <GitHub Copilot will suggest the code by reading the tab 1 >
```

### Exercise

- **エクササイズ 1**: 複数のタブを開いてGitHub Copilotを試し、提案がどのようにされるかを観察してみてください。
- **エクササイズ 2**: 特定のタブを閉じて、その動作がどのように変わるかを確認してみてください。
- **エクササイズ 3**: 複雑なプロジェクトで Copilot へ送信されるコードの文脈をを減らして実験してみてください。これが提供される提案にどのように影響するか観察してみましょう。

### Checklist for Further Learning

- Copilot に必要なコンテキストを最適に与えるには、どのような戦略を採用することができますか? 
- コメントにおける言語の選択は、多様なチーム内の協力にどのように影響しますか? 

### ノート

GitHub Copilotは常に進化と改善を続けており、アルゴリズムも更新される可能性があります。この情報は2023年8月時点の正確な情報です。
今後このトークン制約は緩和される可能性があります。
