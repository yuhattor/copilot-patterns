# Documentação Amigável para IA

## Descrição

Ao criar documentação em formato compreensível para IA em equipe, é possível aumentar a produtividade geral da equipe, não apenas para os engenheiros que escrevem o código. Por exemplo, a definição de tabelas de banco de dados pode ser escrita em Markdown e gerenciada no Git como documentação, em vez de usar PowerPoint ou Excel.

## Problema

No desenvolvimento de produtos, é necessário vários tipos de documentos, como especificações de requisitos, documentos de design, diagramas de arquitetura, especificações de configuração de infraestrutura e documentos de casos de teste. Geralmente, formatos como PowerPoint ou Excel são preferidos, mas a IA não pode ler esses documentos. Além disso, gerenciar arquivos binários em um repositório Git não é uma boa prática.

## História

O GitHub Copilot for Business foi introduzido na sua equipe. Os engenheiros estão felizes por terem seu tempo de trabalho reduzido. A equipe parece ter duplicado de tamanho com a ajuda da IA. Por outro lado, o problema é que a IA só pode fazer o que os engenheiros instruíram. Além disso, como a IA não entende o contexto que os engenheiros têm, eles precisam digitar grandes quantidades de linguagem natural para transmitir mais contexto à IA. Como resultado, aumentou a necessidade de converter os documentos fornecidos pelo PM em Markdown ou CSV, para que a IA possa lê-los, em vez de simplesmente copiar e colar o texto.

"Seria ótimo se tudo já estivesse escrito em CSV ou Markdown desde o início!"

## Contexto

Muitos projetos são gerenciados com documentação em formatos como PowerPoint ou Excel. As pessoas que não são engenheiras estão se comunicando em locais que não são o GitHub e as decisões finais não estão sendo salvas no repositório. Embora os documentos sejam resumidos em um formato que a IA possa ler, eles não são gerenciados em um único local.

## Solução

A equipe deve se esforçar para criar documentação em formatos de texto, como Markdown ou CSV. Os documentos que contêm contexto que deve ser entregue aos engenheiros e à IA devem ser salvos no Git como documentação. O repositório deve ser facilmente acessível a partir de fora do espaço de trabalho usando Git Submodule, entre outros. Se necessário, copie o texto do arquivo para o campo de comentários e passe-o para a IA como um prompt.

## Exemplo Conhecido

* Preparar a definição de tabela em formato CSV ou Markdown e associá-la à criação de arquivos de migração e à criação de interfaces.
* Converter definições de infraestrutura descritas em linguagem natural em arquivos de configuração de infraestrutura como código, como o Terraform.
* Converter documentos de casos de teste em arquivos de teste. Isso é especialmente eficaz para testes de API com padrões definidos. Isso torna o desenvolvimento orientado a testes mais fácil.

## Contexto Resultante

* Os engenheiros podem criar mais código com menos esforço, o que leva à redução de custos.
* Os proprietários de projetos e os gerentes de produtos também podem obter resultados mais rapidamente dos engenheiros.
* Os membros que normalmente não escrevem código também podem colaborar usando o GitHub, tornando-se mais acostumados a julgar o contexto que os engenheiros precisam e o contexto que deve ser fornecido à IA, permitindo que eles usem a IA de forma eficaz para o desenvolvimento adequado.
* Como as alterações na documentação são registradas, é possível rastrear o que foi alterado, quando e por quem, além do código, aumentando o controle geral.
* Não haverá mais discrepâncias entre documentação e implementação.

## Observação

* Atualmente, o GitHub Copilot só pode ler determinados tipos de arquivos. No caso de estar escrevendo Python, o código em Python no tab aberto é lido e passado como um prompt. Portanto, copie e cole a parte necessária da documentação amigável para IA em um campo de comentário em um arquivo .py.
* Nem todos os documentos são adequados para serem armazenados em um repositório. Salvar muitos documentos desnecessários no repositório pode levar a uma queda no desempenho de pesquisa. Tente escrever principalmente em Markdown para texto que está próximo à implementação.
* O número de tokens que podem ser passados para a IA é limitado. Tente resumir cada seção da documentação de forma concisa e evite muitas dependências entre as seções.
