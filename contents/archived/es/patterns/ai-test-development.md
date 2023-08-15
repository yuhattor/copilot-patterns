# Desarrollo de pruebas con IA

## Descripción

Es difícil esperar una cobertura de casos de prueba sin proporcionar contexto a la IA al usar GitHub Copilot para la generación de código.
Para escribir casos de prueba efectivos, se deben utilizar herramientas como GitHub Copilot y ChatGPT.

## Contexto

GitHub Copilot es una herramienta de generación de código impulsada por IA diseñada para reducir la codificación manual de los programadores.
Con GitHub Copilot, la IA puede generar un gran código para ti utilizando la sintaxis y los enfoques que quizás no conozcas.
Sin embargo, el código que es menos legible para ti puede disminuir la mantenibilidad.
Por lo tanto, es importante preparar un código de prueba sólido incluso al utilizar GitHub Copilot.
El código de prueba desempeña un papel importante en garantizar la calidad del programa y la cobertura de casos de prueba para el código generado automáticamente es esencial.

## Problema

Al escribir código de prueba utilizando GitHub Copilot, es difícil generar código de prueba con suficiente cobertura sin proporcionar un contexto detallado.

Por ejemplo, usemos GitHub Copilot para escribir el siguiente código de prueba que realiza la multiplicación de dos números.

```py
def multiply(a, b):
    return a * b
```

Usando GitHub Copilot, puedes generar fácilmente código de prueba para este código.

```py
import unittest

# Write test code for multiply()
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

Ahora sabemos que GitHub Copilot puede usarse para TDD.
¿Pero los casos de prueba introducidos aquí son realmente buenos?
"¡De ninguna manera!" El código de prueba proporcionado por GitHub Copilot está lejos de ser casos de prueba excelentes.

Aquí hay algunos problemas a señalar.
En primer lugar, hay duplicación en las pruebas.
Algunos casos de prueba esperan los mismos resultados.
Esto significa duplicación en las pruebas y la ejecución de pruebas innecesarias.

El segundo problema es que no se están detectando errores.
En este caso de prueba, estamos confirmando que la función multiply() está funcionando según lo esperado, pero no puede detectar errores si ocurren.
Por ejemplo, no hay proceso para devolver un error si se pasa un tipo de cadena.

Si pasamos el siguiente proceso utilizando la función multiply() que pasó la prueba en este momento, podemos ver que no funciona según lo esperado:

```py
print(multiply(2, "¡Hola, mundo!"))
# ¡Hola, mundo!¡Hola, mundo!
```

Hubo duplicación en los ejemplos mostrados y no se estaban detectando errores.
Si fueras a escribir el código, podría ser mejor escribirlo así:

En el siguiente caso, se comunica con GitHub Copilot mientras se especifican las condiciones una por una:

```py
# Escriba el código de prueba para multiply() de acuerdo con las siguientes condiciones.
# Condición: Incluya casos exitosos
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        # Condición: Incluya casos fallidos
        self.assertIsNot(multiply(2, 3), 7)
        # Condición: Confirme que el tipo de retorno es numérico
        self.assertIsInstance(multiply(2, 3), int)
```

Ha mejorado mucho en comparación con antes, pero todavía falta exhaustividad.
¿Cómo podemos hacer mejor uso de GitHub Copilot para escribir casos de prueba más exhaustivos?

## Solución

Cuando se utiliza GitHub Copilot para escribir código de prueba, es necesario proporcionar un contexto detallado.
Utilizando modelos de procesamiento de lenguaje natural como ChatGPT, es posible crear casos de prueba más completos.

Por ejemplo, al pasar una consulta como la siguiente a ChatGPT:

> ¿Cuáles son los casos de prueba/condiciones que deben incluirse en el código de prueba para la siguiente función sin omitir nada?
> ```py
> def multiply(a, b):
>     return a * b
> ```

Entonces, ChatGPT devuelve resultados que parecen ser casos de prueba maravillosamente completos.

> Los siguientes son ejemplos de casos de prueba que deben incluirse en el código de prueba para la función `multiply()`:
>
> * Cuando se ingresan dos enteros positivos, confirme que se devuelve el resultado correcto.
> * Cuando se ingresan dos enteros negativos, confirme que se devuelve el resultado correcto.
> * Cuando se ingresa un entero positivo y un entero negativo, confirme que se devuelve el resultado correcto.
> * Cuando uno de los argumentos es 0, confirme que se devuelve 0 como resultado.
> * Cuando uno de los argumentos es un número decimal, confirme que se produce un error.
> * Cuando uno de los argumentos es una cadena de caracteres, confirme que se produce un error.
> * Cuando se ingresa un valor no entero, confirme que se produce un error.

Basándose en los resultados anteriores, se escribió el siguiente código de prueba con la ayuda de GitHub Copilot.
Ahora se ve mucho mejor:

```py
# Escribir el código de prueba para multiply() de acuerdo a las siguientes condiciones.
# Condición: Incluya casos exitosos
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # Cuando se ingresan dos enteros positivos, confirme que se devuelve el resultado correcto.
        self.assertEqual(multiply(3, 4), 12)
        # Cuando se ingresan dos enteros negativos, confirme que se devuelve el resultado correcto.
        self.assertEqual(multiply(-3, -4), 12)
        # Cuando se ingresa un entero positivo y un entero negativo, confirme que se devuelve el resultado correcto.
        self.assertEqual(multiply(3, -4), -12)
        # Cuando uno de los argumentos es 0, confirme que se devuelve 0 como resultado.
        self.assertEqual(multiply(3, 0), 0)
        # Cuando uno de los argumentos es un número decimal, confirme que se produce un error.
        self.assertRaises(ValueError, multiply, 3, 0.1)
        # Cuando uno de los argumentos es una cadena de caracteres, confirme que se produce un error.
        self.assertRaises(ValueError, multiply, 3, "a")
        # Cuando se ingresa un valor no entero, confirme que se produce un error.
        self.assertRaises(TypeError, multiply, 3, "a")
```

Sin embargo, esto tampoco es perfecto.
La necesidad de confirmar si se produce un error cuando uno de los argumentos es un número decimal depende de la implementación, y los dos últimos casos de prueba prueban el mismo error.
Aún hay margen de mejora, pero es genial que podamos llegar a este nivel en un instante al principio de escribir el código de prueba.

## Contexto Resultante

Al utilizar GitHub Copilot para generar código automáticamente, es necesario prestar atención a la exhaustividad del código de prueba.
Proporcionando un contexto detallado y utilizando modelos de procesamiento de lenguaje natural como ChatGPT, es posible crear casos de prueba más exhaustivos.
Sin embargo, es importante tener en cuenta que no es posible generar automáticamente un código de prueba perfecto, y se necesita corrección manual.
El código de prueba es muy importante para garantizar la calidad del programa, y tener casos de prueba exhaustivos es esencial.
