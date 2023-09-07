---
title: "AI が理解可能な命名規則"
description: "変数や関数をAIが理解可能な方法で命名します。GitHub Copilotの 背後にある AI は大規模言語モデルベースで、本質的に自然言語モデルなので、自然言語としてコードを理解します。適当な命名は提案の質を落とす可能性があります。"
authors: [yuhattor] 
category: design-pattern
platforms: [copilot, copilot-chat]
level: lv2
aliases:
  - /docs/v/ja/design-pattern/ai-readable-naming-convention
---

## AIが読み取り可能な命名規則

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

AIが理解可能な命名規則のパターンは、GitHub Copilotのような AI ツールがもっと読みやすくするためにコード内の変数と関数の命名方法に焦点を当てます。一般的でありふれたプログラミング名や、`x` や `y` のような適当な命名を避け、具体的で説明的な名前を採用することで、人間の開発者と GitHub Copilot を動かすAIモデルの両方が容易に理解できるコードを作ります。

例えば、図書館システムを作るエンジニアは、システムの変数名や関数名に「辞書(=dictionary)」「ライブラリ(=library)」「本棚(=stack)」といった一般的な言葉を使うかもしれません。しかし、"dictionary"という名前を含む変数の本当の型が配列だったらどうでしょう。これはほんの一例ですが、GitHub Copilotはこうしたことが積み重なると間違った答えを提案することがあります。
さらに文脈を示す必要がある場合は、言語のタイプヒンティングを用いるか、コメントとして文脈を追加するのがよいでしょう。

このパターンに従うことで、GitHub Copilotの効果を高め、より正確なサジェストと開発者の速度向上につながります。

#### Example

ここでは、異なる命名規則がコードの明快さと正確さにどのような影響を与えるかを示す3つの例を紹介します: 

1. **Ambiguous Naming**:
   ```python
   # This may confuse whether "dictionary" refers to a book or a data type
   dictionary = 
   ```

2. **Better Naming with Comments**:
   ```python
   # sample list of dictionaries in the library, like "Oxford" and "Cambridge"
   library_dictionaries = ["Merriam-Webster", "Oxford", "Cambridge"]
   ```

3. **Specific Naming with Type Hinting**:
   ```python
   from typing import List

   # A clear and specific variable name with type hinting
   list_of_dictionaries_in_library: List[str] = ["Merriam-Webster", "Oxford", "Cambridge"]
   ```

### Exercise

- **エクササイズ 1**: 現在のコードベースを見直し、非記述的な方法で名前が付けられている可能性のある変数や関数を特定します。それらをAIが読み取り可能な命名規則に従ってリネームしてみてください。
- **エクササイズ 2**: 新しい命名パターンで GitHub Copilot を使用して実験し、変更前後の提案と精度を比較してみてください。
- **エクササイズ 3**: この命名規則を念頭に置いて新しいコードを書いてみて、Copilotがコードにどのように反応するかを観察してみてください。
- **エクササイズ 4**: チーム向けに AI の可読性に焦点を当てた命名規則ガイドラインを作成し、チームのコーディング標準に組み込んでみてください。
- **エクササイズ 5**: チームにこれらの命名規則の使用を奨励し、全体のコードの可読性と GitHub Copilot の効果に対する影響を時間をかけて観察してみてください。

### Further Learningのチェックリスト

- 人間の開発者とAIモデルの両方にコードをもっと読みやすくするにはどうすればいいですか?
- この命名パターンが適用できない、または逆効果になる特定のケースはありますか?
