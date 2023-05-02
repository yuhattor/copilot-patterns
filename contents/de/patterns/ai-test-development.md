# Testentwicklung mit AI

## Beschreibung

Es ist schwierig, Testfälle mit ausreichender Abdeckung zu erwarten, wenn man keine Kontextinformationen an die AI liefert, während man Codegenerierung mit GitHub Copilot durchführt. Verwenden Sie nicht nur GitHub Copilot, sondern auch Tools wie ChatGPT, um Testfälle zu schreiben.

## Kontext

GitHub Copilot ist ein AI-gestütztes Tool zur automatischen Codegenerierung, das darauf abzielt, Programmierern das manuelle Schreiben von Code zu reduzieren. Mit GitHub Copilot könnte die KI großartigen Code in Syntaxen oder Ansätzen generieren, mit denen Sie nicht vertraut sind. Aber Code, der für Sie schwer lesbar ist, kann die Wartbarkeit beeinträchtigen. Daher ist es wichtig, auch bei Verwendung von GitHub Copilot solide Testfälle vorzubereiten. Testfälle spielen eine wichtige Rolle bei der Sicherung der Programmqualität, daher ist eine ausreichende Testabdeckung der automatisch generierten Testfälle unerlässlich.

## Problem

Wenn Sie mit GitHub Copilot Testfälle schreiben, ist es schwer, Testfälle mit ausreichender Abdeckung automatisch zu generieren, wenn Sie keine detaillierten Kontextinformationen bereitstellen.

Nehmen Sie als Beispiel folgenden Code, der mit GitHub Copilot geschrieben wurde. Dieser Code führt eine Multiplikation zweier Zahlen aus.

```py
def multiply(a, b):
    return a * b
```

Mit GitHub Copilot können Sie leicht Testfälle generieren.

```py
import unittest

# Schreiben Sie Testfälle für multiply()
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

Es wurde gezeigt, dass GitHub Copilot auch für TDD verwendet werden kann. Aber waren die oben genannten Testfälle wirklich gut?

Hier sind einige Probleme aufgeführt:
Zunächst gibt es Testduplizierungen. Einige Testfälle erwarten dasselbe Ergebnis. Dies bedeutet, dass Tests dupliziert werden und unnötige Tests ausgeführt werden.

Das zweite Problem ist, dass Fehler nicht erkannt werden. Dieser Testfall überprüft, ob die multiply() -Funktion wie erwartet funktioniert, erkennt jedoch keinen Fehler, der auftritt, wenn z.B. ein String übergeben wird.

Wenn Sie den multiply() -Funktion, der den oben genannten Test bestanden hat, für die folgende Verarbeitung verwenden, wird festgestellt, dass sie nicht wie erwartet funktioniert.

```py
print(multiply(2, "Hallo Welt!"))
# Hallo Welt!Hallo Welt!
```

Es gab Duplizierungen von Tests und das Erkennen von Fehlern wurde nicht durchgeführt. Wenn Sie Code schreiben möchten, können Sie wie folgt schreiben und dabei Schritt für Schritt Bedingungen festlegen und mit GitHub Copilot kommunizieren.

```py
# Schreiben Sie Testfälle für multiply(), wie folgt:
# Bedingung: Erfolgsfälle einbeziehen
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        # Bedingung: Fehlerfälle einbeziehen
        self.assertIsNot(multiply(2, 3), 7)
        # Bedingung: Überprüfen, ob die Rückgabe eine numerische Art ist
        self.assertIsInstance(multiply(2, 3), int)
```

Es hat sich im Vergleich zu früher deutlich verbessert. Auf der anderen Seite mangelt es jedoch immer noch an Vollständigkeit.
Wie können wir GitHub Copilot besser nutzen, um umfassendere Tests zu schreiben?

## Lösung

Wenn Sie Testcode mit GitHub Copilot schreiben, ist es wichtig, einen detaillierten Kontext zu geben. Mit Natural Language Processing-Modellen wie ChatGPT können Sie umfassendere Testfälle erstellen.

Geben Sie ChatGPT beispielsweise folgende Aufforderung:

> Welche Testfälle/Bedingungen müssen berücksichtigt werden, um den folgenden Code vollständig zu testen? Bitte als Liste auflisten:
> ```py
> def multiply(a, b):
>     return a * b
> ```

ChatGPT gibt Ihnen dann eine Antwort, die wie ein umfassender Testfall aussieht:

> Hier sind einige Beispiele für Testfälle, die in den Testcode für die multiply() Funktion aufgenommen werden sollten.
>
> * Überprüfen, ob es das richtige Ergebnis zurückgibt, wenn zwei positive ganze Zahlen eingegeben werden.
> * Überprüfen, ob es das richtige Ergebnis zurückgibt, wenn zwei negative ganze Zahlen eingegeben werden.
> * Überprüfen, ob es das richtige Ergebnis zurückgibt, wenn eine positive ganze Zahl und eine negative ganze Zahl eingegeben werden.
> * Überprüfen, ob das Ergebnis 0 ist, wenn eine Eingabe 0 ist.
> * Überprüfen, ob es einen Fehler gibt, wenn eine Eingabe eine Dezimalzahl ist.
> * Überprüfen, ob es einen Fehler gibt, wenn eine Eingabe eine Zeichenkette ist.
> * Überprüfen, ob es einen Fehler gibt, wenn eine Eingabe außerhalb des Ganzzahlbereichs liegt.

Basierend auf diesen Ergebnissen können Sie mit GitHub Copilot den Testcode wie folgt schreiben. Es sieht viel besser aus:

```py
# Bitte schreiben Sie Testcode für multiply() unter den folgenden Bedingungen.
# Bedingungen: Beinhaltet erfolgreiche Fälle

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # Überprüfen, ob das richtige Ergebnis zurückgegeben wird, wenn zwei positive Ganzzahlen eingegeben werden.
        self.assertEqual(multiply(3, 4), 12)
        # Überprüfen, ob das richtige Ergebnis zurückgegeben wird, wenn zwei negative Ganzzahlen eingegeben werden.
        self.assertEqual(multiply(-3, -4), 12)
        # Überprüfen, ob das richtige Ergebnis zurückgegeben wird, wenn eine positive Ganzzahl und eine negative Ganzzahl eingegeben werden.
        self.assertEqual(multiply(3, -4), -12)
        # Überprüfen, ob das Ergebnis Null ist, wenn eine der Eingaben Null ist.
        self.assertEqual(multiply(3, 0), 0)
        # Überprüfen, ob ein Fehler auftritt, wenn eine der Eingaben eine Dezimalzahl ist.
        self.assertRaises(ValueError, multiply, 3, 0.1)
        # Überprüfen, ob ein Fehler auftritt, wenn eine der Eingaben eine Zeichenkette ist.
        self.assertRaises(ValueError, multiply, 3, "a")
        # Überprüfen, ob ein Fehler auftritt, wenn eine Eingabe keine Ganzzahl ist.
        self.assertRaises(TypeError, multiply, 3, "a")
```

Allerdings ist dies nicht perfekt. Ob es notwendig ist, einen Fehler zu melden, wenn eine der Eingaben eine Dezimalzahl ist, hängt von der Implementierung ab. Die letzten beiden Testfälle testen denselben Fehler. Es gibt also noch Raum für Verbesserungen. Aber es ist großartig, dass Sie mit diesem Schreibbeginn so schnell dorthin gekommen sind.

## Ergebniskontext

Beim Generieren von Code automatisch mit GitHub Copilot müssen Sie darauf achten, dass Ihre Testfälle abgedeckt sind. Wenn Sie detaillierten Kontext bereitstellen und natürliche Sprachverarbeitungsmodelle wie ChatGPT verwenden, können Sie umfassendere Testfälle erstellen. Es ist jedoch zu beachten, dass es nicht möglich ist, perfekten Testcode automatisch zu generieren, und dass manuelle Korrekturen erforderlich sein können. Testfälle sind sehr wichtig, um die Qualität von Programmen zu gewährleisten, und umfassende Testfälle sind unerlässlich.
