# Kommentare in Code umwandeln

Mit GitHub Copilot ist es möglich, neuen Code auf der Grundlage von vom Entwickler festgelegten Bedingungen zu generieren. Beispielsweise können Sie durch Angabe von Bedingungen wie folgt neuen Code generieren:

Sie können beispielsweise durch die folgenden Bedingungen eine neue Funktion generieren:

```ts
// Name der Funktion: calculateAverage
// Argumente der Funktion: numbers (Array)
// Rückgabetyp der Funktion: number
```

Wenn Sie diese Bedingungen angeben, generiert GitHub Copilot den folgenden Code:

```ts
function calculateAverage(numbers: number[]): number {
    // Berechnung des Durchschnitts des Arrays
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

Es ist auch möglich, komplexere Definitionen zu erstellen.
