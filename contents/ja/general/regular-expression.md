---
name: "正規表現"
description: "GitHub Copilot と共に正規表現パターンのドラフトを生成"
category: "general"
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: 100
---

## 正規表現

<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">

{% hint style="info" %}
Currently, LLMs do not have the ability to properly represent complex regular expressions.
For complex ones, a human must provide supplemental input. On the other hand, it can be applied to simple regular expressions.
{% endhint %}

### Description

GitHub Copilot は正規表現のパターンのドラフトを作成できます。以下では、文字列の検索や抽出に正規表現を使用する方法について説明します。2つの例を通して、GitHub Copilot が "入力/出力パターン" と "自然言語パターン" の両方で正規表現を生成する方法を示します。

#### Example

##### 入力/出力パターン

最初に、入力と出力を記述することで、GitHub Copilot は正規表現のパターンを作成できます。

```python
import re

# Write a regular expression
# - Input: "Hello World"
# - Output: ["H", "W"]

regex
```

結果として以下のようなコードを得ることができます。

```python
import re
# Write a regular expression
# - Input: "Hello World"
# - Output: ["H", "W"]

regex = r"[A-Z]"
matched = re.findall(regex, "Hello World")
```

##### 自然言語パターン

次に、正規表現で達成したい内容を自然言語で提供します。

```python
import re
# Write a regular expression
# - "I have 3 apples and 2 oranges" like string, extract only the numbers to make an array

sentence
```

結果として以下のようなコードを得ることができます。

```python
import re
# Write a regular expression
# - "I have 3 apples and 2 oranges" like string, extract only the numbers to make an array

sentence = "I have 3 apples and 2 oranges"
regex = r"\d+"
matched = re.findall(regex, sentence)
```

### Exercise

- **エクササイズ**: 文字列 "Hello World" から小文字のみを抽出します。

### Checklist for Further Learning

- 正規表現のパターンは、指定された文字列から正確な一致を抽出していますか?
- 現時点で、GitHub Copilot が使う 大規模言語モデルは、複雑な正規表現を適切に表現する能力を持っていません。複雑な正規表現を表現したい場合、どうしますか? GitHub Copilot をどのように活用して、それを構築するのをサポートし、支援しますか?
