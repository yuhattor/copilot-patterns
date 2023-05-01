# Generare codice dal commento

GitHub Copilot può generare nuovo codice in base alle condizioni specificate dallo sviluppatore. Ad esempio, è possibile generare codice specificando le seguenti condizioni:

Ad esempio, specificando le seguenti condizioni, è possibile generare una nuova funzione:

```ts
// Nome della funzione: calculateAverage
// Argomenti della funzione: numeri (array)
// Tipo di ritorno della funzione: numero
```

Specificando queste condizioni, GitHub Copilot genererà il seguente codice:

```ts
function calculateAverage(numbers: number[]): number {
    // Calcola la media dell'array
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

È possibile definire condizioni più complesse.
