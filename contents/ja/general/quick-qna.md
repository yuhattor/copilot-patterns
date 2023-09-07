---
title: "GitHub CopilotとのクイックQ&A"
description: "GitHub Copilot を使うことでエディタの中で、質問への迅速な回答を得ることができます。"
category: general
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv3
aliases:
  - /docs/v/ja/general/quick-qna
---

## GitHub CopilotとのクイックQ&A

[<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

コーディングの際には、素早い対話と明確化が効率的な開発の鍵となることがよくあります。GitHubは "GitHub Copilot Chat" プロダクトを持っていますが、"クイックQ&A" テクニックは軽量な代替手段として機能します。これにより、開発者はコードエディタの中でキーボードのポジションを離れることなく GitHub Copilot と素早くやり取りし、簡潔な回答と洞察を得ることができます。これは独自の機能ではなく、GitHub Copilot との素早い対話のためにコメントを活用する方法で、敏捷性のための便利なツールとして役立ちます。

#### Example

クイックチャット技法を使用すると、コード内で直接質問をし、Copilotから簡潔な回答を得ることができます。

```rb
# me: このループを最適化する最良の方法は何ですか? 
# copilot: 
```

その後、GitHub Copilot が質問に回答します

```rb
# me: このループを最適化する最良の方法は何ですか? 
# copilot: ベクトル化されたアプローチを使用するか、中間結果をキャッシュすることを検討してください。
```

"q:" と "a:" だけでも構いません

```javascript
// q: ミリ秒単位で現在の時刻を取得するにはどうすればよいですか? 
// a: 
```

詳細な対話のために、役割を定義することができます: 

```rb
# Roles: copilot
#   Python のエキスパートで 15 年以上の経験があります
# Role: me
#   中堅エンジニア
#
# me: このループを最適化する最良の方法は何ですか? 
# copilot: ベクトル化されたアプローチを使用するか、中間結果をキャッシュすることを検討してください。
```

### Exercise

- **エクササイズ 1**: "GitHub Copilot Chat" とエディタ内でのクイックチャットを使用して比較し、違いを考えてください。
- **エクササイズ 2**: クイックチャットを使用して、3つの異なるコーディングの質問に対するワンライナーの回答を得てください。
- **エクササイズ 3**: クイックチャット内で役割を定義し、文脈情報が Copilot の回答にどのように影響するかを観察してください。

### Checklist for Further Learning

- クイックチャットは GitHub Copilot Chat プロダクトとどう異なり、どちらが他方より優れている場合があるのですか?
- クイックチャットテクニックは、開発プロセスのさまざまな段階にどのように統合することができるのですか?
- クイックチャットの使用における潜在的な欠点や制限は何であり、それらはどのように軽減される可能性があるのですか?
