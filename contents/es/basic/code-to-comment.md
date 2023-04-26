# Generación de Comentarios

GitHub Copilot es un motor para generar código, pero también puede generar comentarios a partir del código.
Por ejemplo, suponga que tiene el siguiente código para la Criba de Eratóstenes sin comentarios:

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

GitHub Copilot puede escribir comentarios explicativos para el método, como este:

```py
# Escriba aquí la descripción del método <- [Prompt Actual]
# Entrada: n - el número de primos que se desea retornar
# Salida: una lista de los primeros n primos
# Ejemplo: eratosthenes_sieve(5) -> [2, 3, 5, 7, 11]
# Nota: esta es una forma muy ineficiente de encontrar primos, pero es fácil de entender
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

Además, puede escribir explicaciones de código a partir del código mismo, ayudando a los ingenieros a comprender rápidamente el código de otras personas:

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # Descripción del algoritmo <- [Prompt Actual]
    # 1. Crear una lista de enteros consecutivos desde 2 hasta n: (2, 3, 4, ..., n).
    # 2. Inicialmente, sea p igual a 2, el primer número primo.
    # 3. Comenzando desde p, enumerar sus múltiplos contando hasta n en incrementos de p, y marcarlos en la lista
    #    (estos serán 2p, 3p, 4p, ...; el propio p no debe ser marcado).
    # 4. Encuentre el primer número mayor que p en la lista que no esté marcado. Si no hubo tal número, deténgase.
    #    De lo contrario, deje que p ahora sea igual a este nuevo número (que es el siguiente primo), y repita desde el paso 3.
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

## Mostrar Pasos

Utilizando la característica LIST STEPS en [Code Brushes](https://githubnext.com/projects/code-brushes/) en GitHub Next, puede lograr resultados similares.

```py
def calculate_sum(numbers):
    # inicializar una variable para rastrear el total
    total = 0
    # iterar sobre cada número en la lista
    for number in numbers:
        # agregar el número al total
        total += number
    # devolver el total
    return total
```

## Código a Documentar