# Complétion de code

La méthode la plus simple pour utiliser GitHub Copilot est la complétion de code. La complétion de code améliore la productivité des développeurs en fournissant des suggestions de code pendant que le développeur tape du code.

Par exemple, si vous définissez une fonction en JavaScript, en tapant le code suivant :

```js
function calculateSum(a, b) {
    // entrer le code ici
}
```

GitHub Copilot fournira des suggestions de code qui pourraient être utilisées à l'intérieur de la fonction. Par exemple, vous pourriez obtenir des suggestions de code comme :

```js
const sum = a + b;
return sum;
```

Si le développeur choisit cette suggestion, le code suivant sera inséré à l'intérieur de la fonction :

```js
function calculateSum(a, b) {
    const sum = a + b;
    return sum;
}
```

## Priorité de référence de GitHub Copilot

GitHub Copilot référence plusieurs fichiers récemment ouverts dans la même langue et calcule leur similarité pour déterminer quels fichiers inclure dans la suggestion de code. La logique est actuellement non divulguée, mais vous pouvez consulter des articles tels que [celui-ci](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals#how-is-the-prompt-prepared-a-code-walkthrough) pour avoir une idée du fonctionnement interne de l'outil.

## Note

Comme GitHub Copilot fournit du code généré par l'IA, le code généré automatiquement n'est pas toujours parfaitement précis. Les développeurs doivent vérifier le code généré et le modifier manuellement si nécessaire. En utilisant la fonction de complétion de code de GitHub Copilot, les développeurs peuvent entrer moins de code manuellement.
