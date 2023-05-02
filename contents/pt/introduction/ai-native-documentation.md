# Documentação Nativa de AI: Legibilidade de Documentos de AI

Atualmente, há muito burburinho em torno de uma ferramenta de desenvolvimento chamada GitHub Copilot, que vem com funcionalidade assistida por AI.
Há uma concepção errada de que essa ferramenta é apenas para engenheiros.
Embora isso seja parcialmente verdadeiro, também é parcialmente incorreto.
De fato, o GitHub Copilot tem uma incrível habilidade de transformar a maneira como os engenheiros trabalham.
No entanto, à medida que os métodos de trabalho dos engenheiros mudam, as organizações também devem se adaptar.
Se você estiver em uma posição de PM ou PO, esse é um problema importante para você também.
Já que se espera que os engenheiros de sua equipe executem seu melhor trabalho, implementando rapidamente seus requisitos definidos.
Daqui para frente, mesmo que você não seja um engenheiro, será necessário criar documentação **legível por AI** para permitir que os engenheiros de sua equipe colaborem com AI.

## Cultura de Documentação e Desenvolvimento Nativo de AI

Nos últimos anos, a tecnologia de AI avançou rapidamente, com modelos como LLM (Large Language Model) ganhando atenção.
O GitHub, uma plataforma de desenvolvimento de código aberto, também se aventurou no campo do desenvolvimento de AI.
Um exemplo disso é o "GitHub Copilot".
Curiosamente, o desenvolvimento assistido por AI e o desenvolvimento de código aberto compartilham uma base comum em termos de colaboração.
Especificamente, ambos os métodos envolvem trabalhar com formatos baseados em documentos, como o Markdown.
Formatos como o Markdown são projetados para representar informações estruturadas e são mais fáceis para a AI analisar do que arquivos do PowerPoint ou do Excel.
Consequentemente, eles contribuem para a melhoria da qualidade do código gerado pela AI.

A AI prefere arquivos CSV simples a planilhas complexas do Excel preenchidas com metadados.
Suponha que você, como PM, liste os requisitos do cliente e reúna as informações necessárias para um banco de dados.
Se os requisitos estiverem escritos em um arquivo CSV ou resumidos em Markdown, os engenheiros podem facilmente convertê-los em código.
No entanto, se você compilar as informações em um documento do Excel personalizado para suas preferências, os engenheiros devem primeiro copiá-las, formatá-las e depois convertê-las em código.
Qual abordagem é melhor?

Além disso, no desenvolvimento de código aberto, a qualidade da documentação pode estar diretamente relacionada ao sucesso de um projeto.
Projetos de código aberto estão abertos a qualquer pessoa e a documentação adequadamente mantida permite que novos desenvolvedores se integrem de maneira mais suave.
Portanto, a documentação é altamente valorizada no desenvolvimento de código aberto.
Da mesma forma, no desenvolvimento de AI, uma cultura de documentação bem estabelecida pode levar a um desenvolvimento mais eficiente e de maior qualidade.
Mesmo que você não seja um engenheiro, sua linguagem natural escrita em Markdown pode contribuir significativamente para a saída final, que é o código.
Isso poderia ser um código que representa a lógica de negócios, definições de tabela ou até mesmo cenários de teste.
Sua equipe de desenvolvimento está pronta para incluir AI?
Os documentos legíveis por AI estão preparados?
Se a resposta for não, você deve começar a criar uma equipe de desenvolvimento que esteja confortável para a AI participar.

## Desenvolvimento Nativo de AI e Estratégia InnerSource

Discutimos o desenvolvimento de código aberto, mas também há um conceito semelhante chamado InnerSource.
InnerSource é uma abordagem que adota as melhores práticas de desenvolvimento de software de código aberto em organizações que desenvolvem software não de código aberto ou proprietário.
Seu objetivo é promover a colaboração entre fronteiras organizacionais e quebrar silos organizacionais.

InnerSource está se tornando cada vez mais importante para as empresas evitarem reinventar a roda, otimizarem o desenvolvimento para reduzir custos e criarem novo valor por meio da colaboração.

Como mencionado na página de desenvolvimento nativo de AI, a AI tende a aprimorar humanos experientes.
Indivíduos seniores ou experientes dentro de uma organização que entendem a arquitetura são impulsionados, enquanto outros são designados para tarefas mais simples.

No entanto, como a AI é principalmente treinada em conhecimentos da internet, ela não pode acessar domínios proprietários, conhecimentos fechados dentro de organizações ou informações não publicadas.
Portanto, se essas informações não forem documentadas ou compartilhadas adequadamente dentro da organização, isso representa um problema.
Isso significa que não apenas os engenheiros não podem acessar as informações, mas a AI, como o GitHub Copilot, também não pode acessá-las.

O conhecimento que não pode ser obtido da internet está se tornando cada vez mais importante e é uma competência central das empresas.
Existe uma citação de um livro introdutório InnerSource ["Getting Started with InnerSource"](https://innersourcecommons.org/learn/books/getting-started-with-innersource/) de O'Reilly:

> InnerSource difere do código aberto clássico, permanecendo dentro da visão e do controle de uma única organização. A "abertura" do projeto se estende por muitas equipes dentro da organização. Isso permite que a organização incorpore segredos comerciais diferenciados no código sem medo de que sejam revelados a terceiros, enquanto se beneficia da criatividade e perspectivas diversas contribuídas por pessoas em toda a organização.

Muitas empresas enfrentam a escolha de colaborar com AI ou serem substituídas por ela.
É essencial agregar as informações internas que são a fonte da vantagem competitiva de uma organização e tê-las utilizadas pela AI.
Para isso, a documentação com legibilidade por AI é indispensável.

Com relação ao InnerSource, já existe uma comunidade madura onde são compartilhados métodos para a realização de co-criação dentro das organizações e a criação de documentação.
Acesse esta comunidade e aproveite as iniciativas InnerSource.
Dessa forma, você pode utilizar efetivamente o conhecimento e as informações internas e aproveitar ao máximo a colaboração com AI.

### Referências InnerSource

- [InnerSource Commons](https://innersourcecommons.org/): página da Fundação InnerSource Commons
- [InnerSource Patterns](https://patterns.innersourcecommons.org/): Coleção das melhores práticas InnerSource
- [Getting Started with InnerSource](https://innersourcecommons.org/learn/books/getting-started-with-innersource/): Livro introdutório InnerSource da O'Reilly
- [Understanding the InnerSource Checklist](https://innersourcecommons.org/learn/books/understanding-the-innersource-checklist/): Guia prático InnerSource da O'Reilly

## Criando Documentação Rica em Contexto

Conforme o desenvolvimento de código aberto amadurece, a colaboração entre países e fusos horários surge.
No entanto, a distância geográfica e as diferenças de horário às vezes tornam a comunicação síncrona difícil.
Por exemplo, o horário diurno em Nova York é o horário noturno em Tóquio, e é indesejável perturbar os colaboradores baseados no Japão à noite ou interferir no tempo em família.
Portanto, geralmente é preferível a documentação baseada em documentos escritos.
Isso poderia ser algo como RFCs ou documentos de design, ou comentários escritos em Issues do GitHub.
Documentos formados por comentários em Issues e similares também são chamados de [documentação passiva](https://www.oreilly.com/library/view/understanding-the-innersource/9781491986899/ch04.html).
Estes também são formas de documentação.

Existe um trecho em [Understanding the InnerSource Checklist](https://innersourcecommons.org/ja/learn/books/getting-started-with-innersource/) publicado pela O'Reilly que diz o seguinte:

> A documentação passiva é o registro da documentação que criamos todos os dias enquanto comunicamos abertamente. É uma ótima maneira de retirar o conhecimento tribal de silos e colocá-lo em um formato arquivável e encontrável. Como uma vantagem adicional, ela é mantida tipicamente com o projeto ou o código que documenta, portanto, está em um local fácil de encontrar e relevante para o contexto.

O que é importante aqui é colocá-lo adequadamente em palavras, incluindo o contexto.
É difícil transmitir comunicação não verbal, nuances e atmosfera que são comunicados por meio do Zoom ou conversas cara a cara de forma assíncrona em fusos horários diferentes.

Considere desenvolver com AI.
Por exemplo, o GitHub Copilot participará de reuniões no Zoom.
Está na sala da equipe dizendo: "Ei, eu sou o GitHub Copilot, vamos ter uma reunião rápida de check-in".
A resposta é não.
Todo o contexto deve ser transmitido à AI por escrito.
Isso também é necessário ao criar documentação apropriada para comunicação assíncrona, como no desenvolvimento de código aberto.

É claro que há diferenças na granularidade da documentação entre o desenvolvimento de código aberto e o desenvolvimento assistido por AI.
Escrever "Eu quero consertar esse bug" no Issues do GitHub pode levar alguém a pensar em uma solução, mas a AI não pode ir tão longe.
No entanto, há definitivamente áreas em que a AI se destaca.
Se você deseja expressar a arquitetura em nuvem como Infraestrutura como Código, é melhor escrevê-la em Mermaid ou expressá-la em linguagem natural em vez de desenhá-la em PowerPoint.

O ponto aqui não é que toda a comunicação precisa ser documentada.
Você e sua equipe precisam considerar qual nível de documentação deixar, como e onde deixá-la.

## Coordenação da inteligência artificial do conhecimento organizacional

Com recursos como o GitHub Copilot for Docs incluído no GitHub Copilot X, a inteligência artificial pode criar a documentação perfeita para você.
Os documentos que você escreve também podem se tornar materiais de integração para a próxima pessoa.

No passado, coletar informações e criar materiais de integração para novos engenheiros era uma tarefa comum, mas no futuro, a inteligência artificial provavelmente assumirá esse papel.
Você pode incorporar todo o conhecimento que possui em documentos como a única fonte confiável de informações.

Essa abordagem também pode ser vista explicitamente na documentação da [Atlassian](https://www.atlassian.com/ja/work-management/knowledge-sharing/documentation/importance-of-documentation).
Ler sua documentação com o desenvolvimento nativo de IA em mente pode levar a novas descobertas.
Os documentos que você escreve terão personalidade através da IA.
No entanto, isso requer documentação suficiente, como mencionado anteriormente.

## A Distância Entre a Linguagem Natural e a Implementação se Torna Mais Próxima

Como você pode ter percebido até agora, a distância entre a linguagem natural e a implementação está ficando muito mais próxima.
Como mencionado anteriormente, do ponto de vista educacional, se a escrita de prompts e código em um só lugar continuar, pode ser possível criar documentação em um único arquivo.
Esse tipo de mudança é fascinante.

## Lista de verificação

- [ ] Sua equipe atualmente possui uma cultura de documentação. Se sim, como é. Se não, o que está impedindo?
- [ ] Considere que tipo de documentação é necessária para sua equipe colaborar com IA.
- [ ] Há uma cultura de código aberto ou código interno em sua equipe?
- [ ] Comece criando uma cultura de documentação dentro de seu escopo. Em que áreas você pode começar a escrever documentação em Markdown. Pense nisso.
