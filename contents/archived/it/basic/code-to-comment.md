# Comment Generation

GitHub Copilot è un motore di generazione di codice che può anche generare commenti dal codice. Ad esempio, supponiamo di avere il codice seguente per la Cernita di Eratostene senza commenti:

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

GitHub Copilot può generare il seguente commento esplicativo per il metodo:

```py
# Scrivi qui la descrizione del metodo <- [Prompt effettiva]
# Input: n - il numero di primi da restituire
# Output: una lista dei primi n numeri primi
# Esempio: eratosthenes_sieve(5) -> [2, 3, 5, 7, 11]
# Nota: questo è un modo molto inefficiente per trovare i numeri primi, ma è facile da capire
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

Inoltre, è possibile generare una spiegazione del codice dal codice stesso, il che aiuta gli ingegneri a comprendere rapidamente il codice degli altri:

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # Descrizione dell'algoritmo <- [Prompt effettiva]
    # 1. Crea una lista di interi consecutivi da 2 a n: (2, 3, 4, ..., n).
    # 2. Inizialmente, fai sì che p sia uguale a 2, il primo numero primo.
    # 3. A partire da p, enumera i suoi multipli contando fino a n con incrementi di p e segnali nella lista
    #    (questi saranno 2p, 3p, 4p, ...; il p stesso non dovrebbe essere segnato).
    # 4. Trova il primo numero maggiore di p nella lista che non è segnato. Se non esiste tale numero, fermati.
    #    In caso contrario, fai sì che p sia ora uguale a questo nuovo numero (che è il prossimo numero primo), e ripeti dal passaggio 3.
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

## Visualizzazione dei passaggi

È possibile utilizzare la funzione LIST STEPS presente in [Code Brushes](https://githubnext.com/projects/code-brushes/) su GitHub Next per ottenere lo stesso risultato.

```py
def calculate_sum(numbers):
    # inizializza una variabile per tenere traccia del totale
    total = 0
    # itera su ogni numero nella lista
    for number in numbers:
        # aggiunge il numero al totale
        total += number
    # restituisce il totale
    return total
```

## Codice da documentare

Quando si ha a che fare con codice di grandi dimensioni, un modo per ottenere spiegazioni sull'output è utilizzare strumenti AI in formato chat come ChatGPT o Bing. In questo modo si può avere una panoramica dell'intero codice.
