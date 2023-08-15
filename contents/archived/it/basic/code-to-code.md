# Code Completion

Il modo più semplice per utilizzare GitHub Copilot è attraverso il completamento automatico del codice.
Il completamento automatico del codice migliora la produttività degli sviluppatori fornendo suggerimenti di codice quando l'utente sta digitando.

Ad esempio, supponiamo di definire una funzione in JavaScript. Mentre si digita il codice seguente:

```js
function calculateSum(a, b) {
    // ここに処理を入力する
}
```

GitHub Copilot può fornire suggerimenti di codice che potrebbero essere utilizzati all'interno della funzione. Ad esempio, potrebbe suggerire il seguente codice:

```js
const sum = a + b;
return sum;
```

Se l'utente seleziona questo suggerimento, il codice verrà inserito all'interno della funzione come segue:

```js
function calculateSum(a, b) {
    const sum = a + b;
    return sum;
}
```

## Priorità di riferimento di GitHub Copilot

GitHub Copilot cerca tra alcuni file dello stesso linguaggio aperti recentemente, calcolando la loro somiglianza per determinare quali includere nel prompt.
Attualmente la logica è proprietaria, ma ci sono documenti di reverse engineering come questo [articolo](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals#how-is-the-prompt-prepared-a-code-walkthrough).

## Nota

Poiché GitHub Copilot fornisce codice generato dall'IA, il codice automaticamente generato potrebbe non essere completamente preciso. Gli sviluppatori devono verificare il codice generato e modificarlo manualmente se necessario.
Utilizzando la funzionalità di completamento automatico del codice di GitHub Copilot, gli sviluppatori possono ridurre la quantità di codice da inserire manualmente.
