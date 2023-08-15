# Comment Generation

GitHub Copilot est un moteur de génération de code, mais il peut également générer des commentaires à partir du code.
Par exemple, si nous avons le code suivant pour le crible d'Ératosthène sans commentaire :

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

GitHub Copilot peut écrire un commentaire expliquant la méthode comme suit :

```py
# Écrire la description de la méthode ici <- [Prompt actuel]
# Entrée : n - le nombre de nombres premiers à retourner
# Sortie : une liste des n premiers nombres premiers
# Exemple : eratosthenes_sieve(5) -> [2, 3, 5, 7, 11]
# Note : ceci est une méthode très inefficace pour trouver des nombres premiers, mais elle est facile à comprendre.
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

Il est également possible de générer des commentaires expliquant le code à partir du code lui-même, ce qui permet aux ingénieurs de comprendre rapidement le code d'autres personnes :

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # Description de l'algorithme <- [Prompt actuel]
    # 1. Créer une liste d'entiers consécutifs de 2 à n : (2, 3, 4, ..., n).
    # 2. Initialement, laisser p égal à 2, le premier nombre premier.
    # 3. En commençant par p, énumérer ses multiples en comptant jusqu'à n par incréments de p, et les marquer dans la liste
    # (ceux-ci seront 2p, 3p, 4p, ... ; le p lui-même ne doit pas être marqué).
    # 4. Trouver le premier nombre supérieur à p dans la liste qui n'est pas marqué. S'il n'y a pas de tel nombre, arrêter.
    # Sinon, laisser p égal à ce nouveau nombre (qui est le prochain nombre premier), et répéter à partir de l'étape 3.
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

## Affichage des étapes

Il est possible de faire la même chose avec la fonction LIST STEPS de [Code Brushes](https://githubnext.com/projects/code-brushes/) sur GitHub Next.

```py
def calculate_sum(numbers):
    # initialiser une variable pour suivre le total
    total = 0
    # parcourir chaque nombre dans la liste
    for number in numbers:
        # ajouter le nombre au total
        total += number
    # retourner le total
    return total
```

## Code à documenter

Pour les codes de grande envergure, il est possible d'obtenir une sortie de commentaire en utilisant des outils d'IA de type chatbot comme ChatGPT ou Bing.
Il est également recommandé d'utiliser des outils de chatbot pour comprendre rapidement l'ensemble du code.
