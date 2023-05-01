# Comentarios para generar código

GitHub Copilot puede generar nuevo código basado en las condiciones que especifique el desarrollador. Por ejemplo, puede generar un nuevo método al especificar condiciones como las siguientes:

```ts
// Nombre del método: calculateAverage
// Argumentos del método: numbers (arreglo)
// Tipo de retorno del método: número
```

Al especificar estas condiciones, GitHub Copilot generará el siguiente código:

```ts
function calculateAverage(numbers: number[]): number {
    // Calcula el promedio del arreglo
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

También se pueden especificar definiciones más complejas.
