# Sviluppo di test utilizzando l'IA

## Descrizione

Quando si utilizza GitHub Copilot per la generazione di codice, è difficile aspettarsi una copertura sufficiente dei casi di test senza fornire un contesto all'IA.
Non solo con GitHub Copilot, ma anche utilizzando strumenti come ChatGPT, è importante scrivere test case in modo approfondito.

## Contesto

GitHub Copilot è uno strumento di generazione automatica di codice basato sull'IA, che mira a ridurre la scrittura manuale di codice da parte del programmatore.
Utilizzando GitHub Copilot, l'IA potrebbe generare del codice eccellente in sintassi e approcci che non sei abituato a usare.
Tuttavia, il codice generato potrebbe essere di bassa leggibilità per te, il che potrebbe diminuire la manutenibilità.
Pertanto, è importante fornire dei test case solidi anche quando si utilizza GitHub Copilot.
I test case svolgono un ruolo importante nell'assicurare la qualità del programma e la copertura dei casi di test del codice generato automaticamente è essenziale.

## Problema

Nel caso in cui si voglia utilizzare GitHub Copilot per scrivere i test case, senza fornire un contesto dettagliato, non è possibile generare dei test case sufficientemente coprenti.

Ad esempio, supponiamo di voler scrivere i seguenti test case utilizzando GitHub Copilot. Questo codice esegue la moltiplicazione di due numeri.

```py
def multiply(a, b):
    return a * b
```

Utilizzando GitHub Copilot, è possibile generare facilmente il seguente codice di test.

```py
import unittest

# Scrivi i test case per multiply()
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 10), 50)
        self.assertEqual(multiply(7, 7), 49)
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(3, 3), 9)

unittest.main()
```

Ora, sappiamo che GitHub Copilot può essere utilizzato anche per il Test-Driven Development (TDD). Tuttavia, questi test case che abbiamo presentato sono veramente buoni?
"No way!" I test case forniti da GitHub Copilot non si avvicinano nemmeno ai test case eccellenti.

Qui sono elencati alcuni problemi con questi test case. Innanzitutto, c'è duplicazione nei test. Alcuni test case si aspettano lo stesso risultato, il che significa che stiamo eseguendo test ridondanti.

In secondo luogo, non viene rilevato alcun errore. Questi test case controllano se la funzione multiply() funziona correttamente, ma non rilevano errori. Ad esempio, non c'è alcun controllo per la gestione di input di tipo stringa.

Se utilizzassimo la funzione multiply() testata fino ad ora, e le passassimo il seguente input, scopriremmo che non produce il risultato previsto.

```py
print(multiply(2, "Hello World!"))
# Hello World!Hello World!
```

Come abbiamo visto, ci sono duplicazioni nei test case e non vengono rilevati errori. Se si volesse scrivere codice, potrebbe essere utile comunicare con GitHub Copilot e specificare ogni condizione di test una per una, come nell'esempio seguente:

```py
# Scrivi i test case per multiply() seguendo le seguenti condizioni.
# Condizione: includi casi di successo
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        # Condizione: includi casi di fallimento
        self.assertIsNot(multiply(2, 3), 7)
        # Condizione: controlla che il valore restituito sia di tipo numerico
        self.assertIsInstance(multiply(2, 3), int)
```

Questo approccio è già un miglioramento rispetto ai test case precedenti. Tuttavia, non è ancora sufficientemente esaustivo. Come possiamo utilizzare al meglio GitHub Copilot per scrivere test case più coprenti?

Soluzione

Quando si scrivono codici di test utilizzando GitHub Copilot, è necessario fornire un contesto dettagliato. Utilizzando modelli di elaborazione del linguaggio naturale come ChatGPT, è possibile creare casi di test più completi.

Proviamo a passare una prompt come questa a ChatGPT:

> Quali sono i casi di test/le condizioni da includere per scrivere codice di test completo per il seguente codice? Si prega di elencare puntualmente.
> ```py
> def multiply(a, b):
>     return a * b
> ```

ChatGPT restituirà una lista di casi di test da includere, che sembrano molto completi:

> Ecco alcuni esempi di casi di test da includere nel codice di test per la funzione multiply ():
>
> * Verificare che restituisca il risultato corretto quando si inseriscono due numeri interi positivi.
> * Verificare che restituisca il risultato corretto quando si inseriscono due numeri interi negativi.
> * Verificare che restituisca il risultato corretto quando si inserisce un numero intero positivo e un numero intero negativo.
> * Verificare che restituisca 0 quando uno dei due input è 0.
> * Verificare che si verifichi un errore quando si inserisce un numero decimale come input.
> * Verificare che si verifichi un errore quando si inserisce una stringa come input.
> * Verificare che si verifichi un errore quando si inserisce un input non intero.

Utilizzando questi casi di test, possiamo scrivere il seguente codice di test con GitHub Copilot. Il risultato sembra molto meglio.

```py
# Si prega di scrivere il codice di test per multiply () con le seguenti condizioni:
# Condizione: Includere casi di successo
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # Verificare che restituisca il risultato corretto quando si inseriscono due numeri interi positivi.
        self.assertEqual(multiply(3, 4), 12)
        # Verificare che restituisca il risultato corretto quando si inseriscono due numeri interi negativi.
        self.assertEqual(multiply(-3, -4), 12)
        # Verificare che restituisca il risultato corretto quando si inserisce un numero intero positivo e un numero intero negativo.
        self.assertEqual(multiply(3, -4), -12)
        # Verificare che restituisca 0 quando uno dei due input è 0.
        self.assertEqual(multiply(3, 0), 0)
        # Verificare che si verifichi un errore quando si inserisce un numero decimale come input.
        self.assertRaises(ValueError, multiply, 3, 0.1)
        # Verificare che si verifichi un errore quando si inserisce una stringa come input.
        self.assertRaises(ValueError, multiply, 3, "a")
        # Verificare che si verifichi un errore quando si inserisce un input non intero.
        self.assertRaises(TypeError, multiply, 3, "a")
```

Tuttavia, non è ancora perfetto. Ad esempio, la necessità di verificare se si verifica un errore quando si inserisce un numero decimale come input dipende dall'implementazione del codice, e gli ultimi due casi di test stanno testando lo stesso errore. Ci sono ancora margini per la correzione manuale. Tuttavia, è fantastico che si possa raggiungere questo punto in pochi istanti durante la scrittura del codice di test.

In sintesi, quando si utilizza GitHub Copilot per generare codice automaticamente, è necessario prestare attenzione alla completezza del codice di test. È possibile creare casi di test più completi utilizzando modelli di elaborazione del linguaggio naturale come ChatGPT e fornendo un contesto dettagliato. Tuttavia, è importante tenere presente che non è possibile generare automaticamente codice di test perfetto, e che è necessario apportare correzioni manuali. Il codice di test è molto importante per garantire la qualità del programma, e avere casi di test completi è essenziale.
