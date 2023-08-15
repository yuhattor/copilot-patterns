# Comentario Generado

GitHub Copilot es un motor que genera código, pero también puede generar comentarios a partir del código.
Por ejemplo, supongamos que tenemos el siguiente código de la criba de Eratóstenes sin comentarios.

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

GitHub Copilot puede escribir comentarios explicando el método de la siguiente manera:

```py
# Escribir aquí la descripción del método <- [Prompt Actual]
# Entrada: n - el número de números primos a devolver
# Salida: una lista de los primeros n números primos
# Ejemplo: eratosthenes_sieve(5) -> [2, 3, 5, 7, 11]
# Nota: esta es una forma muy ineficiente de encontrar números primos, pero es fácil de entender
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

Además, se puede escribir una explicación del algoritmo a partir del código, lo que permite a los ingenieros entender el código de otros más rápidamente.

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # Descripción del algoritmo <- [Prompt Actual]
    # 1. Crear una lista de enteros consecutivos desde 2 hasta n: (2, 3, 4, ..., n).
    # 2. Inicialmente, p = 2, el primer número primo.
    # 3. A partir de p, enumerar sus múltiplos contando hasta n en incrementos de p, y marcarlos en la lista
    #    (estos serán 2p, 3p, 4p, ...; el p en sí no debe ser marcado).
    # 4. Encontrar el primer número mayor que p en la lista que no está marcado. Si no existe tal número, detenerse.
    #    De lo contrario, dejar que p ahora sea igual a este nuevo número (que es el siguiente número primo), y repetir desde el paso 3.
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

## Mostrar Pasos

El uso de la función LIST STEPS en [Code Brushes](https://githubnext.com/projects/code-brushes/) de GitHub Next permite hacer lo mismo.

```py
def calculate_sum(numbers):
    # inicializar una variable para seguir la suma total
    total = 0
    # iterar sobre cada número en la lista
    for number in numbers:
        # agregar el número a la suma total
        total += number
    # devolver la suma total
    return total
```

## De Código a Documento

Si el código es muy grande, otra opción es utilizar herramientas de inteligencia artificial en forma de chat, como ChatGPT o Bing, para obtener una explicación de la documentación del código completo y así entender su descripción general.
