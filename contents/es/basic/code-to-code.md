# Completado de código

La forma más sencilla de utilizar GitHub Copilot es mediante el completado de código.
El completado de código mejora la productividad del desarrollador al proporcionar sugerencias de código cuando el desarrollador está escribiendo código.

Por ejemplo, supongamos que está definiendo una función en JavaScript. Está escribiendo código como este:

```js
function calculateSum(a, b) {
    // Inserte el procesamiento aquí
}
```

En este momento, GitHub Copilot puede proporcionar sugerencias de código que podrían ser utilizadas dentro de la función. Por ejemplo, se podría ofrecer el siguiente código:

```js
const sum = a + b;
return sum;
```

Si el desarrollador selecciona este código sugerido, se insertará el siguiente código dentro de la función:

```js
function calculateSum(a, b) {
    const sum = a + b;
    return sum;
}
```

## Prioridad de referencia de GitHub Copilot

GitHub Copilot revisa varios archivos del mismo lenguaje de programación que se han abierto recientemente y calcula su similitud para determinar qué archivos se incluirán en la lista de sugerencias.
Actualmente, la lógica detrás de esto no es pública, pero hay algunas notas sobre la ingeniería inversa disponible en [esta entrada de blog](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals#how-is-the-prompt-prepared-a-code-walkthrough).

## Nota 

GitHub Copilot proporciona código generado por inteligencia artificial, por lo que no se garantiza que el código generado automáticamente sea completamente preciso. Los desarrolladores deben revisar el código generado y corregirlo manualmente según sea necesario.
Al utilizar la función de completado de código de GitHub Copilot, los desarrolladores pueden escribir menos código manualmente.
