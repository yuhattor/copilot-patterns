# Geração de comentários

O GitHub Copilot é um motor de geração de código que também é capaz de gerar comentários a partir do código. Por exemplo, suponha que você tenha o código do crivo de Eratóstenes abaixo sem comentários:

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

O GitHub Copilot pode gerar o comentário explicando o método abaixo:

```py
# Escreva a descrição do método aqui <- [Prompt real]
# Entrada: n - o número de primos a serem retornados
# Saída: uma lista dos primeiros n primos
# Exemplo: eratosthenes_sieve(5) -> [2, 3, 5, 7, 11]
# Nota: esta é uma maneira muito ineficiente de encontrar primos, mas é fácil de entender
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

Além disso, o GitHub Copilot pode gerar explicações para o próprio código, permitindo que outros engenheiros entendam rapidamente o código de outra pessoa. Um exemplo é dado abaixo:

```py
def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # Descrição do algoritmo <- [Prompt real]
    # 1. Criar uma lista de inteiros consecutivos de 2 a n: (2, 3, 4, ..., n).
    # 2. Inicialmente, deixe p igual a 2, o primeiro número primo.
    # 3. Começando a partir de p, enumere seus múltiplos contando até n em incrementos de p e marque-os na lista
    #    (esses serão 2p, 3p, 4p, ...; o próprio p não deve ser marcado).
    # 4. Encontre o primeiro número maior que p na lista que não está marcado. Se não houver tal número, pare.
    #    Caso contrário, deixe p agora igual a este novo número (que é o próximo primo) e repita a partir do passo 3.
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes
```

## Exibição de etapas

Você também pode usar a função LIST STEPS na ferramenta Code Brushes do GitHub Next para obter um resultado semelhante, mostrando as etapas do seu código, como abaixo:

```py
def calculate_sum(numbers):
    # initialize a variable to track the total
    total = 0
    # iterate over each number in the list
    for number in numbers:
        # add the number to the total
        total += number
    # return the total
    return total
```

## Código para documentação

Se o seu código for extenso, uma maneira de obter comentários explicativos é usar ferramentas de AI em formato de chat, como o ChatGPT ou Bing. Isso pode ser útil quando você precisa entender a visão geral de todo o código.
