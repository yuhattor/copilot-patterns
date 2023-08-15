# Kommentar-Generierung

GitHub Copilot ist ein Code-Generator, der auch in der Lage ist, Kommentare aus dem Code zu generieren.
Angenommen, wir haben den folgenden Code des Sieb des Eratosthenes ohne Kommentare:

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

GitHub Copilot kann den folgenden Kommentar zur Beschreibung der Methode generieren:

```py
# Beschreibe hier die Methode <- [Actual Prompt]
# Eingabe: n - Anzahl der zurückzugebenden Primzahlen
# Ausgabe: eine Liste der ersten n Primzahlen
# Beispiel: eratosthenes_sieve(5) -> [2, 3, 5, 7, 11]
# Hinweis: Dies ist eine sehr ineffiziente Methode zur Bestimmung von Primzahlen, aber einfach zu verstehen.
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

Darüber hinaus kann man auch den Code kommentieren, um anderen Entwicklern das Verständnis zu erleichtern:

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # Beschreibung des Algorithmus <- [Actual Prompt]
    # 1. Erstelle eine Liste aufeinanderfolgender ganzer Zahlen von 2 bis n: (2, 3, 4, ..., n).
    # 2. Setze p anfänglich auf 2, die erste Primzahl.
    # 3. Beginnend mit p, zähle dessen Vielfache bis n in Schritten von p auf und markiere sie in der Liste
    #    (diese werden 2p, 3p, 4p, ... sein; p selbst sollte nicht markiert werden).
    # 4. Finde die erste Zahl in der Liste, die größer als p und nicht markiert ist. Wenn es keine solche Zahl gibt, stoppe.
    #    Andernfalls setze p nun auf diese neue Zahl (die nächste Primzahl) und beginne von Schritt 3 erneut.
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

## Schritte anzeigen

Mit der LIST STEPS-Funktion auf GitHub Next's [Code Brushes](https://githubnext.com/projects/code-brushes/) ist es möglich, ähnliche Schritte anzuzeigen.

```py
def calculate_sum(numbers):
    # Initialisierung einer Variablen zur Verfolgung des Gesamtbetrags
    total = 0
    # Iteration über jeden Zahl in der Liste
    for number in numbers:
        # Fügen Sie die Zahl zum Gesamtbetrag hinzu
        total += number
    # Rückgabe des Gesamtbetrags
    return total
```

## Code zu Dokumentieren

Wenn der Code umfangreich ist, kann es eine Möglichkeit sein, mithilfe von ChatGPT oder Bing eine Erklärung zu erhalten. Wenn Sie eine Zusammenfassung des gesamten Codes benötigen, ist es ratsam, eine Chat-basierte AI-Tool zu verwenden.
