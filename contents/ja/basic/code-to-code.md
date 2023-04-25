# コード補完

GitHub Copilot の一番簡単な利用方法はコード補完です。
コード補完は、開発者がコードを入力しているときに、Copilotが候補のコードを提供することで開発者の生産性を向上させます。

例えば、あなたがJavaScriptで関数を定義しているとします。以下のようなコードを入力しているとします。

```js
function calculateSum(a, b) {
    // ここに処理を入力する
}
```

この時、Copilotは関数の内部で使用する可能性があるコードの候補を提供します。例えば、以下のようなコードが提供される場合があります。

```js
const sum = a + b;
return sum;
```

開発者がこの候補のコードを選択すると、関数の内部に以下のコードが挿入されます。

```js
function calculateSum(a, b) {
    const sum = a + b;
    return sum;
}
```

## GitHub Copilot の参照優先度

GitHub Copilot は直近開いたいくつかの同じ言語のファイルを参照し、類似性を計算してプロンプトに含めるファイルを決定します。
現在ロジックは非公開になっていますが、[リバースエンジニアリングの手記](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals.html#how-is-the-prompt-prepared-a-code-walkthrough)などがありますので、ご覧ください。

## Note 

GitHub Copilotは、AIによって生成されたコードを提供するため、自動生成されたコードが完全に正確であるとは限りません。開発者は、生成されたコードを確認し、必要に応じて手動で修正する必要があります。
このように、Copilotのコード補完機能を使用することで、開発者は手動でコードを入力することが少なくなります。
