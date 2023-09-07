---
title: "オープン・クエスチョンで尋ねる"
description: "エラーハンドリングの改善、トラブルシューティングの方法、リファクタリングアイデアなど、コード改善についてはオープンクエスチョンを使用することで、新しいアイデアを GitHub Copilot から引き出すことができます。"
category: refactoring
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv1
aliases:
  - /docs/v/ja/refactoring/asking-with-open-ended-questions
---

## オープン・クエスチョンで尋ねる

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

リファクタリングは、しばしば複雑なプロセスであります。必ずしも何が正しく、何が間違っているかについてではなく、基本概念と潜在的な改善を理解することが重要です。GitHub Copilotでオープン・クエスチョンを利用することで、開発者は GitHub Copilot の助けを借りてより熟慮した方法でコードの改善に取り組むことができます。

#### Example

GitHub Copilotでのクエリに開かれた質問を導入すると、洞察に満ちた提案が得られることがあります。例えば: 

```javascript
// Q: この関数の復元性をどのように改善できますか? 
// A: <GITHUB COPILOT SUGGESTION>
function backupData(data) {
  // 実装はこちら
}

// Q: この文脈でエラーを処理する最良の方法は何ですか? 
// A: <GITHUB COPILOT SUGGESTION>
try {
  // 何かの操作
} catch (error) {
  // エラー処理
}
```

### Exercise

- **エクササイズ 1**: ファイルハンドリングに関連する関数を記述し、それをより信頼性があり効率的にする方法について Copilot に尋ねてみてください。
- **エクササイズ 2**: 例外処理を含むコードスニペットを作成し、エラー報告の改善について Copilot に提案を求めてください。
- **エクササイズ 3**: シンプルな UI コンポーネントを設計し、それに対するアクセスや操作をよりエレガントにする方法について Copilot に尋ねてみてください。

### Checklist for Further Learning

- 既存のコードのどの部分がリファクタリングから利益を得ることができますか?
- オープンクエスチョンが開発プロセスでどのように機能しますか?
