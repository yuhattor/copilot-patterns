# A partir de comentários, gerando código

O GitHub Copilot pode gerar novo código com base em condições especificadas pelos desenvolvedores. Por exemplo, é possível gerar código especificando as seguintes condições:

Por exemplo, especificando as seguintes condições, é possível gerar uma nova função:

```ts
// Nome da função: calcularMedia
// Argumentos da função: números (array)
// Tipo de retorno da função: número
```

Com essa condição especificada, o GitHub Copilot gera o seguinte código:

```ts
function calcularMedia(numeros: number[]): number {
    // Calculando a média do array
    const soma = numeros.reduce((a, b) => a + b);
    return soma / numeros.length;
}
```

É possível criar definições mais complexas.
