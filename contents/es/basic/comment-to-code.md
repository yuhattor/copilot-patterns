# Generación de Código a partir de Comentarios

GitHub Copilot también puede generar nuevo código en función de las condiciones especificadas por los desarrolladores. Por ejemplo, se puede generar código al especificar las siguientes condiciones:

Se pueden especificar las siguientes condiciones para generar una nueva función:

```txt
// Nombre de la función: calculateAverage
// Argumento de la función: numbers (arreglo)
// Tipo de retorno de la función: número
```

Al especificar estas condiciones, GitHub Copilot genera el siguiente código:

```ts
function calculateAverage(numbers: number[]): number {
    // Calculate the average of the array
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

También se pueden proporcionar definiciones más complejas.
