# Documentação AI Native

O uso de tecnologias de IA, como o GitHub Copilot, pode mudar o trabalho dos engenheiros dentro de equipes de desenvolvimento e, por fim, afetar a arquitetura.
Este documento explica o impacto potencial dos métodos de desenvolvimento AI Native.

## Contexto é tudo

Existem várias áreas a serem consideradas quando se trata do uso de tecnologias de IA, como o GitHub Copilot, em um ambiente de desenvolvimento ou processo de desenvolvimento.
As equipes de desenvolvimento precisam estar mais conscientes do contexto para acelerar ainda mais o desenvolvimento.
É importante considerar quais contextos técnicos e de negócios estão incluídos no seu programa.
Embora isso não seja um novo tópico, uma vez que foi dito há muito tempo, agora que a IA está disponível e pode impulsionar a colaboração dos desenvolvedores, vale a pena reconsiderar esses dois contextos.
Esses contextos afetam a arquitetura e a carreira do engenheiro.

Além disso, cada contexto possui áreas de alto e baixo contexto.
Por exemplo, na codificação, escrever processos simples que qualquer pessoa pode escrever pressionando a tecla Tab pode ser suficiente em relação às sugestões do GitHub Copilot.
Por outro lado, em áreas que requerem alto contexto, simplesmente pressionar a tecla Tab não produzirá nada.
Essa área requer conhecimento em áreas específicas de experiência ou tecnologia e não é fácil de dominar.

### Contexto técnico

Para considerar o contexto técnico, vamos pensar em algumas linguagens de programação.
Algumas linguagens, como o Python, têm uma maneira comum de expressar as coisas quando se escreve algo, enquanto outras, como o Ruby, oferecem várias maneiras de expressar uma coisa.
Além disso, o escopo também é uma questão.
Algumas linguagens, como o BASIC, têm um escopo global como padrão, enquanto outras têm um escopo estreito.
A mecânica de referência e empréstimo no Rust é um exemplo típico que inclui alto contexto técnico.
Além disso, o contexto pode ser empilhado em vários níveis em nível de estrutura.

### Contexto de negócios

O mesmo vale para o domínio empresarial.
Vamos pensar na linguagem de banco de dados SQL.
A IA é boa em trabalhos simples e é adequada para implementações que replicam expressões estereotipadas do SQL.
Se você estiver definindo acesso ao banco de dados para uma aplicação simples, precisará de menos contexto.
No entanto, se você estiver lidando com um grande banco de dados complexo, será difícil ter confiança de que o código gerado pela IA não afetará outras operações.
Você pode precisar entender a arquitetura geral e ter algum conhecimento sobre a lógica real.
O mesmo vale para testes - a IA é boa em escrever testes de acordo com cenários dados, mas é difícil pensar em cenários abrangentes de teste.
Os testes para APIs REST que têm funções simples de CRUD podem ser facilmente escritos pela IA, mas é difícil para a IA escrever testes para aplicativos com condições de autorização complexas.

## Arquitetura AI Native

Quão complexo é o contexto em sua arquitetura de aplicativo/servi ção? Se houver muito contexto, o uso de IA para acelerar o desenvolvimento pode ser reduzido.
Isso ocorre porque o contexto que o LLM (Large Language Model) pode entender é limitado e não podemos fornecer simultaneamente uma grande quantidade de contexto para a IA.
Isso se deve à limitação do número máximo de tokens fornecidos e, geralmente, porque os humanos não podem fornecer todas as informações como texto em formato legível por IA.
De certa forma, a IA pode trabalhar indefinidamente se o prompt for continuamente fornecido.
Por outro lado, o tempo que os humanos podem fornecer um prompt para a IA é limitado.
Nesse caso, o gargalo do desenvolvimento é o ser humano.
Portanto, deve-se considerar reduzir o contexto que a IA precisa ter, dividindo os serviços em unidades testáveis ​​e simples.

Dividir em unidades menores e ter uma relação mais fraca entre elas é uma boa ideia.
No entanto, o que estou mencionando não se refere a microserviços no contexto do Kubernetes.
Qualquer design que você considere, incluindo a separação em nível de biblioteca ou SOA, é aceitável.
O importante é dividir os componentes em unidades simples e testáveis.
Quanto mais contexto um aplicativo tiver, menos suporte a IA será necessário.

Em relação ao tamanho apropriado do programa, às vezes ocorrem guerras religiosas e o uso de IA no desenvolvimento ainda está começando e não há uma resposta precisa.
No entanto, considerando a maximização da produtividade do engenheiro e o crescimento mais rápido do produto, é recomendável que você considere um método de desenvolvimento ou arquitetura com base no GitHub Copilot.

No entanto, não devemos perder de vista que a arquitetura de TI não deve ser pensada com o objetivo de "maximizar a produtividade do engenheiro".
A engenharia é apenas um meio de alcançar o resultado final.

Espero que todos participem ativamente dessas discussões neste campo.

## Perspectivas de carreira como engenheiro

Até agora, discutimos a possibilidade de a IA trazer mudanças na arquitetura e cultura de desenvolvimento. Aqui, é importante focar também na carreira de engenharia, não apenas para o próprio engenheiro, mas também para gerentes e pessoas encarregadas de construir organizações.

Em última análise, os engenheiros precisam considerar se desejam ser engenheiros com conhecimento amplo de diversos produtos de negócios ou se desejam ser engenheiros tecnicamente avançados. No entanto, o problema é que existem áreas de baixo e alto contexto em ambos os casos.

Por exemplo, na codificação, pode ser suficiente pressionar a tecla Tab para aceitar as sugestões do GitHub Copilot para escrever processos simples que se repetem ou que levam a uma conclusão, independentemente de quem o escreva. Por outro lado, as áreas especificadas em seções técnicas ou de contexto de negócios exigem um contexto mais alto. Essas áreas exigem conhecimento sobre experiência ou áreas de tecnologia específicas, e não são fáceis de adquirir. Se a informação está disponível na internet, ainda há uma chance de acompanhar, mas se é um conhecimento específico de uma organização e não foi documentado ou se a obtenção de informações tem um custo muito alto, a atualização pode ser difícil.

Isso não se limita à codificação, mas a IA tende a reforçar as pessoas com experiência e conhecimento. Isso significa que os iniciantes podem perder seus trabalhos para especialistas. Se isso não for resolvido, os iniciantes não poderão fazer trabalhos importantes na organização e não poderão esperar o crescimento de suas habilidades. É provável que as habilidades dos especialistas aumentem ainda mais, tornando mais difícil para a organização mantê-los. Também é difícil manter iniciantes que estão apenas fazendo trabalhos entediantes que os especialistas não conseguem fazer devido a restrições de tempo.

Então, o que fazer? Uma resposta é reunir informações técnicas e de negócios sobre produtos e organizações como documentos com contexto e cultivá-los internamente. Quando muitas pessoas participam da criação desses documentos, a colaboração acontece e um banco de dados de conhecimento é criado para a empresa. É hora de promover a colaboração interna semelhante ao código aberto.

## Lista de verificação

- [ ] Quais são os contextos do seu projeto ou produto? Vamos organizá-los.
- [ ] Esse contexto é exclusivo para algumas pessoas? É compartilhado pela equipe?
- [ ] Seu código em seu projeto ou produto pode ser compreendido pela IA, mesmo em baixo contexto? Se houver muito código em contexto, como você o transformará em código fácil de ser escrito pela IA?
- [ ] Você está promovendo a colaboração interna? Se não, pense em ações para melhorar a comunicação e o compartilhamento de conhecimento dentro e entre equipes.
- [ ] Sua equipe discutiu as perspectivas de carreira dos engenheiros em tempos de IA? Vamos discutir se queremos fortalecer áreas técnicas ou de negócios.

## Prospettive di carriera come ingegnere

Finora abbiamo toccato il tema delle potenziali modifiche che l'AI potrebbe apportare all'architettura e alla cultura dello sviluppo. Ora è importante rivolgere l'attenzione anche alla carriera dell'ingegnere. Questo vale non solo per gli ingegneri stessi, ma anche per coloro che si trovano a gestire o a creare organizzazioni.

Alla fine, gli ingegneri devono decidere se mirare a diventare ingegneri con competenze in un'ampia gamma di prodotti commerciali, o puntare a diventare ingegneri altamente tecnici. Tuttavia, il problema è che in entrambi i casi esistono settori a basso e alto contesto.

Per esempio, nella codifica, scrivere processi semplici, come quelli che possono essere scritti solo premendo il tasto TAB rispetto alle proposte di GitHub Copilot, potrebbe essere sufficiente. D'altra parte, le sezioni tecniche o commerciali specifiche richiedono un alto contesto. Questi settori richiedono esperienza e conoscenze su specifiche aree tecnologiche, e non sono facili da apprendere. Se le informazioni non sono disponibili su Internet o se l'accesso a tali informazioni richiede costi molto elevati, può essere difficile tenere il passo.

Ciò non si applica solo alla codifica, ma l'AI tende ad amplificare le conoscenze ed esperienze delle persone più esperte. Ciò significa che i professionisti più esperti rischiano di perdere il loro lavoro a favore dei nuovi arrivati. Se questo viene lasciato inalterato, i novizi non saranno in grado di svolgere lavori importanti all'interno dell'organizzazione e non potranno sviluppare le proprie abilità. Nel frattempo, le abilità degli esperti continueranno a migliorare, diventando difficile per l'organizzazione mantenere queste persone e ancorare i novizi a lavori noiosi e limitati nel tempo.

Quindi, quale potrebbe essere la soluzione? Una risposta è quella di raccogliere le informazioni tecniche e commerciali relative ai prodotti o alle organizzazioni in documenti contenenti il contesto, promuovendo la collaborazione interna tra i membri del team. Quando molte persone partecipano alla creazione di questi documenti, si verifica la collaborazione, e l'organizzazione costruisce un database di conoscenze. È giunto il momento di promuovere la collaborazione interna simile all'open source.

## Checklist

- [ ] Quali contesti ci sono nel tuo progetto o prodotto? Organizza questi contesti.
- [ ] Questo contesto è riservato solo ad alcune persone o condiviso in team?
- [ ] Il codice nel tuo progetto o prodotto è facilmente comprensibile dall'AI a basso contesto o contiene codice ad alto contesto? Se è presente del codice ad alto contesto, come si può trasformarlo in codice più facilmente scritto dall'AI?
- [ ] Stai promuovendo la collaborazione interna? Se no, pensa ad azioni per migliorare la comunicazione e la condivisione di conoscenze tra i membri del team o tra i team stessi.
- [ ] Hai discusso del percorso di carriera degli ingegneri del tuo team nell'era dell'AI? Discuti se si desidera rafforzare le aree tecniche o commerciali.
