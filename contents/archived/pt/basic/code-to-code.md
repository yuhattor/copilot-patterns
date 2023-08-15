# Complemento de código

A forma mais simples de usar o GitHub Copilot é através do complemento de código.
O complemento de código aumenta a produtividade do desenvolvedor fornecendo sugestões de código enquanto o desenvolvedor está digitando.

Por exemplo, se você estiver definindo uma função em JavaScript e digitando o seguinte código:

```js
function calculateSum(a, b) {
    // insira o processamento aqui
}
```

Nesse momento, o GitHub Copilot pode fornecer sugestões de código que podem ser usadas dentro da função. Por exemplo, ele pode fornecer o seguinte código:

```js
const sum = a + b;
return sum;
```

Se o desenvolvedor escolher essa sugestão de código, o seguinte código será inserido dentro da função:

```js
function calculateSum(a, b) {
    const sum = a + b;
    return sum;
}
```

## Prioridade de referência do GitHub Copilot

O GitHub Copilot consulta vários arquivos da mesma linguagem abertos recentemente e calcula a similaridade para determinar quais arquivos incluir nas sugestões do prompt.
Atualmente, a lógica é privada, mas há algumas anotações de engenharia reversa disponíveis, como [esta aqui](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals#how-is-the-prompt-prepared-a-code-walkthrough).

## Nota

O GitHub Copilot fornece código gerado por IA, portanto, o código gerado automaticamente pode não ser totalmente preciso. Os desenvolvedores devem revisar o código gerado e modificá-lo manualmente, se necessário.
O uso do recurso de complemento de código do GitHub Copilot reduz a necessidade de digitar código manualmente.
