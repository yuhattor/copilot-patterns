# Code Completion

Die einfachste Art, GitHub Copilot zu nutzen, ist die Code-Vervollständigung.
Durch die Code-Vervollständigung verbessert GitHub Copilot die Produktivität von Entwicklern, indem es beim Eingeben von Code dem Entwickler Code-Vorschläge zur Verfügung stellt.

Angenommen, Sie definieren eine Funktion in JavaScript. Sie geben den folgenden Code ein:

```js
function calculateSum(a, b) {
    // Hier den Code eingeben
}
```

In diesem Fall bietet GitHub Copilot möglicherweise Code-Vorschläge an, die in der Funktion verwendet werden könnten. Zum Beispiel könnte der folgende Code vorgeschlagen werden:

```js
const sum = a + b;
return sum;
```

Wenn der Entwickler diesen Code-Vorschlag auswählt, wird der folgende Code in die Funktion eingefügt:

```js
function calculateSum(a, b) {
    const sum = a + b;
    return sum;
}
```

## Priorität der Referenz von GitHub Copilot

GitHub Copilot bezieht sich auf mehrere zuletzt geöffnete Dateien in derselben Sprache, berechnet Ähnlichkeiten und bestimmt die zu verwendenden Dateien im Prompt.
Die aktuelle Logik ist nicht öffentlich, aber es gibt einige Ressourcen wie Reverse Engineering Notes, die unter https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals#how-is-the-prompt-prepared-a-code-walkthrough zu finden sind.

## Hinweis

Da GitHub Copilot Code durch KI generiert, ist der automatisch generierte Code möglicherweise nicht vollständig genau. Entwickler müssen den generierten Code überprüfen und gegebenenfalls manuell korrigieren.
Durch die Verwendung der Code-Vervollständigungsfunktion von GitHub Copilot reduzieren Entwickler jedoch die Notwendigkeit, Code manuell einzugeben.
