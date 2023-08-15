# Diretório de Contexto

Também conhecido como diretório de trechos para inclusão de trechos.

## Descrição

Ao coletar o contexto de todo o código base no diretório de contexto dentro do repositório, torna-se mais fácil para o GitHub Copilot passar informações precisas de contexto durante o desenvolvimento.

## Problemas

* Sugestões imprecisas
  O GitHub Copilot pode fazer sugestões imprecisas se não conseguir obter o contexto do código base inteiro. Isso pode resultar na diminuição da qualidade do código ou no aumento do tempo que os desenvolvedores gastam ajustando e corrigindo o código.
* Diminuição da eficiência
  Se o desenvolvedor não mantiver os arquivos relevantes abertos em abas adjacentes, o GitHub Copilot não será capaz de obter informações desses arquivos. Como resultado, as sugestões podem ser imprecisas e o desenvolvedor pode ter que escrever código manualmente, consultando e pesquisando arquivos relevantes. Isso pode diminuir a produtividade dos desenvolvedores.
* Perda de coerência do código
  Se o GitHub Copilot não puder obter o contexto de todo o código base, as sugestões de código que ele faz podem não ter coerência com o código existente. Isso pode afetar a legibilidade e a manutenibilidade do código, e diminuir a velocidade de desenvolvimento da equipe como um todo.

## História

Um dia, um engenheiro da equipe de projeto decidiu usar o GitHub Copilot para desenvolver uma nova funcionalidade. Ela estava animada para usar o GitHub Copilot e escrever código rapidamente com a ajuda dele.

No entanto, à medida que o desenvolvimento progredia, ela percebeu que as sugestões de código feitas pelo GitHub Copilot às vezes eram imprecisas. Mesmo assim, ela continuou a ajustar manualmente o código e a trabalhar nele, mas gradualmente ficou cansada desse processo. Além disso, outros membros da equipe também apontaram que as sugestões de código feitas pelo GitHub Copilot não eram coerentes.

Ela se perguntou por que o GitHub Copilot não estava fazendo sugestões precisas e começou a investigar. Descobriu que uma das razões era que ela não havia mantido os arquivos relevantes abertos adequadamente. Por outro lado, manter todos os arquivos abertos o tempo todo não era uma opção realista, e ela também percebeu que o modelo Codex usado pelo GitHub Copilot para sugerir código tem um limite de tokens que pode passar.

Por isso, ela decidiu adotar o padrão de diretório de contexto. Ela espera que manter os arquivos relevantes abertos ajude o GitHub Copilot a fazer sugestões mais precisas.

## Contexto

O GitHub Copilot, um dos principais produtos de suporte à codificação de inteligência artificial, faz sugestões com base nas informações dos arquivos atualmente abertos ou das abas com o mesmo tipo de arquivo aberto.
Os tokens que o modelo Codex usado pelo GitHub Copilot pode passar são limitados. Portanto, as extensões do GitHub Copilot, como VS Code, não enviam todas as informações dos arquivos abertos como informações de referência para os servidores do GitHub Copilot. Em vez disso, eles priorizam o envio de dados dos arquivos com alta similaridade. Isso inclui a inclusão de trechos, chamada de "inclusão de trechos".

Portanto, é importante manter abertas apenas as abas com o número adequado de arquivos relacionados. Tanto poucos como muitos podem ser problemáticos.

## Solução

1. Crie um diretório de contexto
Crie um diretório que contenha os arquivos que você deseja usar como contexto ou regras para o GitHub Copilot aprender. Esse diretório pode ser criado por um indivíduo ou por toda a equipe.
2. Feche arquivos que não estão relacionados ao desenvolvimento atual
3. Mantenha abertas as abas dos arquivos relacionados ao desenvolvimento atual no VSCode
Atualmente, o GitHub Copilot não possui uma funcionalidade que permita que ele colete o contexto de todo o código base. No entanto, ele pode ler os arquivos atuais e os arquivos abertos no editor. Manter abertas as abas dos arquivos relacionados ajudará o GitHub Copilot a fazer sugestões mais precisas.

## Resultados

Usando o diretório de contexto, o GitHub Copilot pode fazer sugestões mais precisas. Manter as abas dos arquivos relevantes abertas ajuda a obter a codificação assistida de forma mais efetiva.

## Observações

* Atualmente, o GitHub Copilot só lê arquivos limitados. Se você está escrevendo em Python, é recomendável que os arquivos de trechos e os arquivos de referência sejam em Python.
* Se necessário, você pode adicionar esses diretórios ao .gitignore para não enviá-los quando você fizer o push.
* Além disso, você pode usar o Git Submodule para separar o diretório de contexto como um diretório separado.
