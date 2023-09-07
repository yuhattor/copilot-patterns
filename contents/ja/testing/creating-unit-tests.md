---
title: "ユニットテストの作成"
description: "GitHub Copilot を使用してユニットテストを作成することができます。"
category: testing
authors: [yuhattor]
platforms: [copilot, copilot-chat]
level: lv3
aliases:
  - /docs/v/ja/testing/creating-unit-tests
---

## ユニットテストの作成

[<img src="https://img.shields.io/badge/Lv3-Mature_Best_Practice-brightgreen">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

テストはソフトウェア開発プロセスの基本的な部分であり、コードが設計どおりであり、意図した通りに動作することを確認します。システムの個々のコンポーネントをテストするユニットテストの作成は、チャレンジングで時間のかかる作業です。GitHub Copilotを使用すると、このプロセスがより効率的になります。開発者のAliceさんがGitHub Copilotをどのように活用してアプリケーションのユニットテストを記述し、作業量を減少させ、効率を向上させるかを探ってみましょう。
このパターンは、機能テストや API テストにも適用可能です。

#### Example

徹底的にテストする必要のある JavaScript の関数に取り組んでいます。GitHub Copilotの助けを借りて、必要なユニットテストを素早く生成できます。

以下は、テストしたいシンプルな関数です:

```javascript
function add(x, y) {
  return x + y;
}
```

そして、GitHub Copilotの支援を受けてユニットテストを作成する方法は次のとおりです:

```javascript
const assert = require('assert');

describe('add関数', () => {
  it('2つの数値を正しく加算する必要があります', () => {
    assert.equal(add(2, 3), 5);
  });
});
```

### Exercise

- **エクササイズ1**: GitHub Copilotを使用して2つの数値を掛ける関数のユニットテストを作成してください。
- **エクササイズ2**: Copilotを活用して、nullやundefinedの値を処理するなど、さまざまなエッジケースのテストスイートを作成してください。
- **エクササイズ3**: 現在のプロジェクトを振り返り、テストが不足しているコードの部分を特定し、Copilotを使用してユニットテストを作成してください。

### Checklist for Further Learning

- 自分のテストが包括的であり、すべての可能なシナリオをカバーしていることをどのように確認できますか?
- GitHub Copilot がシナリオを全くカバーしなかった際にどのようなプロンプトを追加しますか?
- 他の種類のテスト(E2Eテスト、統合テスト、機能テストなど) に対して、GitHub Copilot はどのように有益であり、それらを記述する際に GitHub Copilotはどのように支援できるか?
