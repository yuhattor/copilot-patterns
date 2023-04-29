# Prompt Compartilhamento de Conhecimento

{% hint style="info" %}
Este documento ainda está em processo de verificação. Esperamos que você discuta ativamente isso em nosso [GitHub Issue](https://github.com/AI-Native-Development/docs/issues/8).
{% endhint %}

## Descrição

Compartilhar prompts para gerar código e utilizá-los como recursos de aprendizado para membros da equipe é importante.

## Problema

Desenvolver com a ajuda da IA, como o GitHub Copilot, pode gerar um código de alta qualidade, mas para um engenheiro experiente, um bom código ou um código de alto desempenho pode não ser um bom código para leitura de código. Se o programa for representado por código excessivamente abreviado ou expressões avançadas específicas da linguagem, a colaboração entre engenheiros em áreas específicas pode se tornar difícil.

## História

Você está procurando por prompts que possam ajudá-lo a dominar o GitHub Copilot. Como um engenheiro experiente, você colaborou com o GitHub Copilot em um recurso específico e, após tentativas e erros, criou um código excelente. Um engenheiro da mesma equipe que estava sentado ao lado viu isso e disse: "Então você sempre escreveu assim! Agora entendi como você sempre produz código excelente".

Você percebeu que o prompt que o levou ao melhor resultado e o processo de tentativa e erro podem ser recursos importantes para os membros da equipe aprenderem. Ao mesmo tempo, descobriu o problema de que os prompts não estão incluídos nos arquivos de produção e começou a pensar em como compartilhá-los.

## Contexto

O GitHub Copilot foi introduzido, mas a forma como cada engenheiro o usa ainda não é compartilhada entre todos. Além disso, os prompts escritos por cada engenheiro no GitHub Copilot não são compartilhados.

## Solução

A equipe deve discutir como compartilhar prompts e como escrever comentários, e estabelecer regras. Para evitar que os prompts se tornem um ruído, é desejável que eles sejam escritos como comentários que também funcionam como documentos.

Existem os seguintes padrões para compartilhar prompts:

* Escreva diretamente no arquivo
  Deixe os prompts nos arquivos para que a equipe possa aprendê-los a partir de outros prompts dos membros da equipe. É importante manter um equilíbrio adequado para que os prompts não se tornem ruído. Além disso, é possível converter parte dos prompts em comentários de documentação ou explicação. Você também pode revisar prompts durante a revisão de código para promover o crescimento dos engenheiros.
* Documentação passiva
  Inclua alguns prompts como comentários em pull requests ou comentários de problemas. Isso tornará os arquivos de código mais legíveis, mas não será possível consultar os prompts de referência dentro do editor.
* Programação em grupo
  Realize uma sessão de programação em grupo para experimentar o ambiente de desenvolvimento do engenheiro experiente sem deixar os prompts nos arquivos ou nos comentários do PR/Issues. É importante compartilhar o que foi aprendido aqui como um documento separado.

## Resultado do Contexto

As habilidades de toda a equipe melhorarão e a aprendizagem eficaz será promovida por meio da partilha de prompts. A legibilidade do código melhorará e a compreensão do código será facilitada pelos comentários que funcionam como documentos, em vez de apenas prompts.
