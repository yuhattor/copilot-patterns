# Générer du code à partir de commentaires

GitHub Copilot peut également générer du nouveau code en fonction des conditions spécifiées par les développeurs. Par exemple, il est possible de générer du code en spécifiant des conditions telles que :

Par exemple, en spécifiant les conditions suivantes, il est possible de générer une nouvelle fonction :

```ts
// Nom de la fonction : calculateAverage
// Arguments de la fonction : numbers (tableau)
// Type de retour de la fonction : number
```

En spécifiant ces conditions, GitHub Copilot génère le code suivant :

```ts
function calculateAverage(numbers: number[]): number {
    // Calcul de la moyenne des éléments du tableau
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
}
```

Il est possible de définir des conditions plus complexes.
