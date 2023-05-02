# Desenvolvimento de Testes Utilizando IA

## Descrição

Quando se utiliza a geração de código com o GitHub Copilot para criar testes, pode ser difícil alcançar a cobertura adequada dos casos de teste sem fornecer contexto à IA. Além do GitHub Copilot, é importante utilizar outras ferramentas, como o ChatGPT, para escrever testes de qualidade.

## Contexto

O GitHub Copilot é uma ferramenta de geração de código automatizada baseada em IA que visa reduzir a quantidade de código manual que um programador precisa escrever. Utilizando o GitHub Copilot, a IA pode gerar código incrível em uma sintaxe ou abordagem que você não está familiarizado. Entretanto, o código gerado pode ser difícil de ser lido e reduzir a manutenção do código. Por isso, é importante preparar testes de qualidade enquanto se utiliza o GitHub Copilot. Os testes desempenham um papel importante na garantia da qualidade do programa, e a cobertura dos casos de teste gerados automaticamente é essencial.

## Problema

Ao utilizar o GitHub Copilot para escrever testes, é difícil gerar testes abrangentes sem fornecer um contexto detalhado.

Por exemplo, vamos utilizar o GitHub Copilot para escrever o seguinte código de teste que executa uma multiplicação de dois valores:

```py
def multiply(a, b):
    return a * b
```

Com o GitHub Copilot, podemos gerar facilmente o código de teste abaixo:

```py
import unittest

# Escreva o código de teste para multiply() aqui
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

Agora sabemos que o GitHub Copilot pode ser utilizado para o TDD. Mas será que os testes gerados são de boa qualidade? Infelizmente, não. Os testes gerados pelo GitHub Copilot não são tão bons quanto deveriam.

Aqui estão alguns problemas que precisamos apontar. Em primeiro lugar, há testes duplicados. Alguns testes esperam o mesmo resultado. Isso significa que estamos executando testes desnecessários.

O segundo problema é que não conseguimos detectar erros. Esses testes verificam se a função multiply() está funcionando corretamente, mas não conseguimos detectar erros se eles ocorrerem. Por exemplo, não temos testes para verificar se a função retorna um erro quando um argumento do tipo string é passado.

Se utilizarmos a função multiply() que foi aprovada nos testes anteriores e a passarmos os seguintes valores:

```py
print(multiply(2, "Hello World!"))
# Hello World!Hello World!
```

Percebemos que a função não está funcionando como deveria.

Aqui estão os testes reescritos:

```py
# Escreva o código de teste para multiply() seguindo as condições abaixo.
# Condição: incluir casos de sucesso
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        # Condição: incl uir casos de falha
        self.assertIsNot(multiply(2, 3), 7)
        # Condição: verificar se o retorno é do tipo numérico
        self.assertIsInstance(multiply(2, 3), int)
```

Melhoramos bastante em relação aos testes anteriores. No entanto, ainda há lacunas na cobertura dos casos de teste. Como podemos usar o GitHub Copilot de forma mais eficaz para escrever testes abrangentes?

## Solução

Ao escrever código de teste usando o GitHub Copilot, é necessário fornecer um contexto detalhado. Usando modelos de processamento de linguagem natural como o ChatGPT, é possível criar casos de teste mais abrangentes.

Vamos fornecer a seguinte solicitação para o ChatGPT:

> Quais casos de teste/condições devem ser considerados ao escrever o código de teste para o seguinte código? Por favor, liste-os com marcadores.

> ```py
> def multiply(a, b):
>     return a * b
> ```

O ChatGPT retorna o seguinte resultado, parecendo ser um conjunto de casos de teste muito abrangente:

> Aqui estão alguns exemplos de casos de teste que devem ser incluídos no código de teste da função `multiply()`:
>
> * Verificar se a função retorna o resultado correto ao receber dois inteiros positivos como entrada.
> * Verificar se a função retorna o resultado correto ao receber dois inteiros negativos como entrada.
> * Verificar se a função retorna o resultado correto ao receber um inteiro positivo e um negativo como entrada.
> * Verificar se a função retorna 0 quando um dos argumentos é 0.
> * Verificar se um erro é levantado quando um dos argumentos é um número decimal.
> * Verificar se um erro é levantado quando um dos argumentos é uma string.
> * Verificar se um erro é levantado quando um dos argumentos não é um inteiro.

Com base nesses casos de teste, juntamente com o GitHub Copilot, escrevemos o seguinte código de teste que parece muito mais agradável:

```py
# Por favor, escreva código de teste para a função `multiply()` seguindo as condições abaixo.
# Condição: incluir casos de teste bem-sucedidos.
class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # Verificar se a função retorna o resultado correto ao receber dois inteiros positivos como entrada.
        self.assertEqual(multiply(3, 4), 12)
        # Verificar se a função retorna o resultado correto ao receber dois inteiros negativos como entrada.
        self.assertEqual(multiply(-3, -4), 12)
        # Verificar se a função retorna o resultado correto ao receber um inteiro positivo e um negativo como entrada.
        self.assertEqual(multiply(3, -4), -12)
        # Verificar se a função retorna 0 quando um dos argumentos é 0.
        self.assertEqual(multiply(3, 0), 0)
        # Verificar se um erro é levantado quando um dos argumentos é um número decimal.
        self.assertRaises(ValueError, multiply, 3, 0.1)
        # Verificar se um erro é levantado quando um dos argumentos é uma string.
        self.assertRaises(ValueError, multiply, 3, "a")
        # Verificar se um erro é levantado quando um dos argumentos não é um inteiro.
        self.assertRaises(TypeError, multiply, 3, "a")
```

No entanto, isso ainda não é perfeito. Se é necessário verificar se um erro é levantado quando um dos argumentos é um número decimal depende da implementação, e os dois últimos casos de teste estão testando o mesmo erro. Ainda há espaço para correções, mas o fato de poder chegar a esse ponto tão rapidamente ao escrever o código de teste é ótimo.

## Contexto Resultante

Ao usar o GitHub Copilot para gerar automaticamente o código, é importante ter cuidado com a abrangência dos testes. Fornecer um contexto detalhado e usar modelos de processamento de linguagem natural como o ChatGPT pode ajudar a criar casos de teste mais abrangentes. No entanto, não é possível gerar automaticamente um código de teste perfeito, e pode ser necessário fazer ajustes manuais. Os testes de código são muito importantes para garantir a qualidade do programa, e ter casos de teste abrangentes é essencial.
