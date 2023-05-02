# Développement de tests avec l'IA

## Description

Lorsque vous utilisez GitHub Copilot pour générer du code, il est difficile de s'attendre à une couverture suffisante des cas de test sans fournir de contexte à l'IA.
Utilisez des outils tels que GitHub Copilot et ChatGPT pour écrire des cas de test solides.

## Contexte

GitHub Copilot est un outil de génération de code automatisé basé sur l'IA, conçu pour réduire la saisie manuelle de code par les programmeurs.
Avec GitHub Copilot, l'IA peut générer un code brillant en utilisant une syntaxe ou une approche avec lesquelles vous n'êtes pas familier.
Cependant, le code illisible pour vous pourrait réduire la maintenabilité.
Par conséquent, il est important de préparer des tests solides tout en utilisant GitHub Copilot.
Les tests sont essentiels pour garantir la qualité des programmes, donc la couverture des cas de test générés automatiquement est indispensable.

## Problème

Lors de l'écriture de tests avec GitHub Copilot, il est difficile de générer suffisamment de cas de test complets sans fournir de contexte détaillé.

Par exemple, si vous utilisez GitHub Copilot pour écrire le code de test suivant, qui effectue une multiplication de deux nombres :

```py
def multiply(a, b):
    return a * b
```

Vous pouvez facilement générer le code de test suivant avec GitHub Copilot :

```py
import unittest

# Écrivez le code de test pour multiply() ici.
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

Maintenant, vous savez que GitHub Copilot peut également être utilisé pour la méthode TDD. Cependant, les cas de test que nous avons présentés ici étaient-ils vraiment bons ?
Eh bien, les cas de test fournis par GitHub Copilot ne sont pas aussi bons que des cas de test solides.

Voici quelques problèmes que nous pouvons souligner :
Tout d'abord, il y a des cas de test en double, ce qui signifie que certains cas de test s'attendent à des résultats identiques.
Cela signifie qu'il y a des tests en double, ce qui exécute des tests inutiles.

Deuxièmement, certains problèmes n'ont pas été détectés.
Ces cas de test confirment que la fonction multiply() fonctionne comme prévu, mais ne peuvent pas détecter d'erreurs.
Par exemple, il n'y a pas de traitement d'erreur pour les cas où une chaîne de caractères est passée en argument.

Si vous utilisez le code de multiplication ci-dessus et passez le texte "Hello World!", vous constaterez que le comportement ne correspond pas à ce qui est attendu :

```py
print(multiply(2, "Hello World!"))
# Hello World!Hello World!
```

Dans l'exemple ci-dessus, il y avait des cas de test en double et certains problèmes n'ont pas été détectés. Si vous deviez écrire du code, vous pourriez l'écrire comme suit :

Dans cet exemple, vous spécifiez les conditions une par une et interagissez avec GitHub Copilot pour vérifier chaque ligne.

```py
# Écrivez le code de test pour multiply() en suivant les conditions ci-dessous.
# Condition: Inclure les cas de réussite.
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        # Condition: Inclure les cas d'échec.
        self.assertIsNot(multiply(2, 3), 7)
        # Condition: Vérifier que le retour est de type int.
        self.assertIsInstance(multiply(2, 3), int)
```

C'est un peu mieux qu'avant, mais cela ne garantit pas une couverture complète. Comment pouvez-vous utiliser GitHub Copilot de manière plus efficace pour écrire des tests complets ?

## Solution

When writing test code using GitHub Copilot, it is necessary to provide detailed context. By using natural language processing models such as ChatGPT, more comprehensive test cases can be created.

Let's pass the following prompt to ChatGPT:

> When writing test code for the following code, what test cases/conditions should be included? Please list them.
> ```py
> def multiply(a, b):
>     return a * b
> ```

Then ChatGPT returns the following result, which looks like a wonderfully comprehensive set of test cases:

> Here are some examples of test cases that should be included in the test code for the multiply() function:
>
> * When two positive integers are input, verify that the correct result is returned.
> * When two negative integers are input, verify that the correct result is returned.
> * When one positive integer and one negative integer are input, verify that the correct result is returned.
> * When one input is 0, verify that the result is 0.
> * When one input is a decimal number, verify that an error occurs.
> * When one input is a string, verify that an error occurs.
> * When an input other than an integer is given, verify that an error occurs.

Based on the above result, we wrote the following test code with GitHub Copilot, and the result looks much nicer:

```py
# Write test code for multiply() according to the following conditions.
# Condition: Include success cases.
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # When two positive integers are input, verify that the correct result is returned.
        self.assertEqual(multiply(3, 4), 12)
        # When two negative integers are input, verify that the correct result is returned.
        self.assertEqual(multiply(-3, -4), 12)
        # When one positive integer and one negative integer are input, verify that the correct result is returned.
        self.assertEqual(multiply(3, -4), -12)
        # When one input is 0, verify that the result is 0.
        self.assertEqual(multiply(3, 0), 0)
        # When one input is a decimal number, verify that an error occurs.
        self.assertRaises(ValueError, multiply, 3, 0.1)
        # When one input is a string, verify that an error occurs.
        self.assertRaises(ValueError, multiply, 3, "a")
        # When an input other than an integer is given, verify that an error occurs.
        self.assertRaises(TypeError, multiply, 3, "a")
```

However, this is not perfect. Whether to verify that an error occurs when one input is a decimal number depends on the implementation, and the last two test cases test the same error. There is still room for improvement, but it is great to be able to get to this point in writing test code at the beginning of the process with such ease using GitHub Copilot.

## Resulting Context

When using GitHub Copilot to automatically generate code, it is important to pay attention to the comprehensiveness of the test code. Providing detailed context and using natural language processing models such as ChatGPT can create more comprehensive test cases. However, it is not possible to automatically generate perfect test code, so it is important to manually modify it. Test code is very important for ensuring program quality, and having comprehensive test cases is essential.
