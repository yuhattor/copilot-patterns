# Completado de Código

La forma más fácil de usar GitHub Copilot es mediante el completado de código.
El completado de código mejora la productividad del desarrollador al proporcionar código candidato mientras el desarrollador escribe.

Por ejemplo, suponga que está definiendo una función en JavaScript. Es posible que escriba el siguiente código:

```js
function calculateSum(a, b) {
    // Ingrese aquí el procesamiento
}
```

En este punto, GitHub Copilot ofrecerá código candidato que podría ser utilizado dentro de la función. Por ejemplo, podría proporcionar el siguiente código:

```js
const sum = a + b;
return sum;
```

Si el desarrollador selecciona este código candidato, se insertará el siguiente código dentro de la función:

```js
function calculateSum(a, b) {
    const sum = a + b;
    return sum;
}
```

## Prioridad de Referencia de GitHub Copilot

GitHub Copilot se refiere a varios archivos recientemente abiertos del mismo lenguaje y calcula similitudes para determinar qué archivos incluir en la sugerencia.
La lógica actual no es pública, pero hay notas sobre ingeniería inversa, así que por favor eche un vistazo.

## Nota

GitHub Copilot proporciona código generado por IA, por lo que el código generado automáticamente puede no ser completamente preciso. Los desarrolladores deben revisar el código generado y realizar correcciones manualmente si es necesario.
Al utilizar la función de completado de código de GitHub Copilot, los desarrolladores necesitarán ingresar código manualmente con menos frecuencia.