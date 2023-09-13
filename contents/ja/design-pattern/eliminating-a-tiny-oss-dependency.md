---
title: "微細な OSS 依存関係の排除"
description: "実際には数行のコードで実装できる、微細な OSS 依存関係の排除"
authors: [yuhattor]
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv0
aliases:
  - /docs/v/ja/design-pattern/eliminating-a-tiny-oss-dependency
---

## 微細な OSS 依存関係の排除

[<img src="https://img.shields.io/badge/Lv0-Pattern_Idea-blueviolet">](https://github.com/orgs/AI-Native-Development/projects/1/)

> これは限定的な適用かもしれません。より多くの事例が発見されれば、この成熟度レベルは上がっていきます。

### Description

left-pad 問題をご存知ですか? 2016年に、left-pad ライブラリがnpmから停止され、それに依存するよく知られたライブラリが動作しなくなりました。left-pad は、指定された文字数、または指定されていない場合はスペースで、文字列の左側を埋めるだけのシンプルなJavaScriptライブラリです。空白行を除いて、約10行のシンプルなコードです。

車輪の再発明を避けるための多くのアイデアがありますが、一方で、重大な影響を及ぼす可能性のある外部コードにも注意を払う必要があります。提供されたコードの範囲が非常に限られている場合、外部ソースに依存するよりも、内部に含める方が良いかもしれません。

### Samples

以下のように、left-pad 関数を実装することができます: 

```ruby
def leftpad(string, length, char = ' ')
    string.rjust(length, String(char))
end
```

### Exercise

- **エクササイズ 1**: 文字列、長さ、パディングする文字を引数とする left-pad 関数を GitHub Copilot を使って実装します。デフォルトの文字はスペースであるべきです。
- **エクササイズ 2**: プロジェクト内に複数の小さな外部依存関係が存在するシナリオを考えます。そのような依存関係を置き換えることができる小さなユーティリティ関数を特定し、実装します。

### Checklist for Further Learning

- 外部依存関係を使用するか、自分でコードを実装するかのトレードオフを考慮しましたか?
- この小規模な依存関係を排除するパターンが、コードの保守性にどのように影響する可能性がありますか?
- 小規模な外部依存関係を内部実装に置き換える際に使用できる原則やガイドラインは何ですか?
