# Documentation natif à l'IA

L'utilisation de technologies d'IA telles que GitHub Copilot peut changer la façon dont les ingénieurs travaillent au sein des équipes de développement, avec une influence potentielle sur l'architecture finale.
Ce document explique les impacts potentiels des méthodes de développement natives à l'IA.

## Le contexte est tout

Lorsque les technologies d'IA telles que GitHub Copilot sont introduites dans l'environnement de développement et les processus de développement, il existe de nombreux domaines à considérer.
Les équipes de développement doivent être plus conscientes du contexte pour accélérer le développement.
Il est important de comprendre le contexte technique et le contexte commercial inclus dans votre programme.
Bien que ce ne soit pas un nouveau sujet, avec l'arrivée de l'IA et la coopération des développeurs, il est maintenant précieux de réfléchir à nouveau à ces deux contextes.
Ces contextes ont une influence sur l'architecture et la carrière de l'ingénieur.

De plus, chaque contexte a des domaines à haut et à faible contexte.
Par exemple, lors de la codification, écrire du code qui répète une tâche simple ou qui finit par aboutir à une certaine manipulation, peu importe qui l'écrit, peut être suffisant pour simplement appuyer sur la touche Tab comme le propose GitHub Copilot.
En revanche, dans les domaines qui nécessitent un contexte élevé, appuyer sur la touche Tab ne produira rien.
Ces domaines exigent une expérience et une connaissance spécifique dans les domaines techniques, et ne sont pas faciles à apprendre.

### Contexte technique

Pour comprendre le contexte technique, examinons quelques langages de programmation.
Certains langages ont une expression commune pour écrire une chose, comme Python, tandis que d'autres, comme Ruby, permettent plusieurs expressions pour écrire une seule chose.
La portée peut également être un problème.
Certains langages ont une portée globale de base, comme BASIC, tandis que d'autres ont une portée plus restreinte.
Le mécanisme de référence et d'emprunt dans Rust est un exemple typique de contexte technique élevé.
De plus, au niveau des frameworks, ce contexte peut s'empiler en plusieurs niveaux.

### Contexte commercial

C'est également le cas pour le domaine commercial.
Prenons l'exemple du langage de base de données SQL.
L'IA est douée pour les tâches simples et convient parfaitement à la mise en œuvre de l'expression standard de SQL.
Si vous devez simplement définir l'accès à la base de données dans une implémentation d'application simple, vous pouvez vous en sortir avec peu de contexte.
Cependant, pour traiter une énorme base de données complexe et imbriquée, il peut être difficile pour l'IA de générer du code qui n'affecte pas d'autres processus.
Vous pourriez avoir besoin de comprendre l'architecture globale et avoir une certaine connaissance de la logique réelle.
Il en va de même pour les tests, l'IA est douée pour écrire des tests basés sur des scénarios donnés, mais il peut être difficile de concevoir des scénarios complets de tests.
Il est facile d'écrire des tests API pour des fonctions CRUD simples, mais il est difficile pour l'IA d'écrire des tests pour des applications complexes avec des conditions d'autorisation complexes, par exemple.

## Architecture native à l'IA

Maintenant, quelle est l'étendue du contexte dans l'architecture de votre fonctionnalité/application que vous gérez ?
Si l'architecture contient beaucoup de contexte, il est possible que l'utilisation de l'IA pour accélérer le développement diminue.
C'est parce que le contexte compréhensible par LLM est limité et qu'il n'est pas possible de fournir simultanément une grande quantité de contexte à l'IA.
Cela est également dû au fait que les humains ne peuvent pas fournir toutes les informations sous une forme lisible par l'IA.
D'une certaine manière, l'IA peut travailler indéfiniment tant que des indices lui sont fournis.
Cependant, le temps que les humains peuvent fournir des indices à l'IA est limité.
Dans ce cas, le goulot d'étranglement dans le développement devient humain.
Il est donc important de réduire le contexte des fonctionnalités et applications afin que l'IA puisse écrire le bon programme sans avoir besoin de fournir un large contexte.

Diviser le service en petits niveaux avec des relations lâches est une bonne idée.
Cependant, ce que je veux souligner, ce n'est pas de dire que les microservices dans le contexte de Kubernetes sont la solution.
Tout design, y compris la séparation à niveau de SOA ou de bibliothèque, est acceptable.
L'important est de diviser les composants en unités simples et testables.
Plus une application a de contexte, moins il est probable qu'elle bénéficie du soutien de l'IA.

La taille appropriée d'un programme est parfois le sujet de débats religieux, et le développement avec l'IA ne fait que commencer, il n'y a donc pas de réponse précise.
Cependant, si vous considérez la maximisation de la productivité des ingénieurs et la croissance la plus rapide possible du produit, il est bon que votre équipe envisage une méthode et une architecture de développement basées sur GitHub Copilot.

Cependant, il est important de ne pas oublier que l'architecture informatique ne doit pas être conçue pour maximiser la production des ingénieurs, mais plutôt comme un moyen d'atteindre les objectifs finaux.

Nous espérons que vous participerez activement aux discussions dans ce domaine.

## Perspectives de carrière en tant qu'ingénieur

Jusqu'à présent, nous avons évoqué la possibilité que l'IA apporte des changements à l'architecture et à la culture de développement. Il est maintenant important de se concentrer sur la carrière en ingénierie, non seulement pour les ingénieurs eux-mêmes, mais aussi pour les gestionnaires et les personnes en charge de la construction d'organisations.

En fin de compte, les ingénieurs doivent réfléchir à la façon de devenir des ingénieurs ayant une connaissance approfondie de divers produits commerciaux ou d'ingénieurs techniquement avancés. Cependant, le problème est qu'il existe des domaines à faible contexte et à haut contexte dans ces deux domaines.

Par exemple, en matière de codage, écrire un traitement tel que la répétition de tâches simples ou la rédaction d'un traitement qui est finalement atteint par n'importe qui peut être aussi simple que d'appuyer sur la touche Tab lorsque GitHub Copilot le propose. En revanche, les domaines spécifiés dans les sections de contexte technique ou commercial sont des domaines nécessitant un contexte élevé. Ces domaines nécessitent de l'expérience et des connaissances spécifiques dans des domaines techniques particuliers et ne sont donc pas faciles à maîtriser. Si les connaissances sont disponibles sur Internet, il est encore possible de les rattraper, mais si elles sont confinées à une organisation particulière et ne sont pas documentées, ou si l'accès à l'information est très coûteux, il peut être difficile de les rattraper.

Cela ne concerne pas seulement le codage, mais l'IA a tendance à renforcer les personnes ayant une connaissance et une expérience approfondies. Cela signifie que les professionnels expérimentés risquent de perdre leur emploi au profit des débutants. Si cela est laissé sans surveillance, les débutants ne seront pas en mesure de faire un travail important au sein de l'organisation et ne pourront pas non plus développer leurs compétences. Les compétences des professionnels expérimentés continueront de croître, ce qui rendra leur maintien au sein de l'organisation difficile, et il sera également difficile de maintenir les débutants qui ne font que des tâches ennuyeuses que les professionnels expérimentés ne peuvent pas faire en raison de contraintes de temps.

Alors, que faut-il faire ? L'une des réponses est de rassembler les informations techniques et commerciales du produit ou de l'organisation sous forme de documents contextuels et de les cultiver en interne. Lorsque de nombreuses personnes participent à la création de cette documentation, cela entraîne une co-création et une base de données de connaissances d'entreprise est créée. Il est maintenant temps de créer un environnement de collaboration interne similaire à l'open source.

## Liste de contrôle

- [ ] Quels sont les contextes de votre projet ou produit ? Organisez les contextes.
- [ ] Ce contexte est-il exclusif à certaines personnes ? Est-il partagé par l'équipe ?
- [ ] Votre code dans votre projet ou produit est-il principalement à faible contexte et compréhensible par l'IA ? Si vous avez beaucoup de code à fort contexte, comment le transformerez-vous en code facile à écrire pour l'IA ?
- [ ] Encouragez-vous la collaboration interne ? Si ce n'est pas le cas, réfléchissez à des actions pour améliorer la communication et le partage de connaissances au sein de l'équipe et entre les équipes.
- [ ] Avez-vous discuté de la trajectoire de carrière en IA de votre équipe d'ingénieurs ? Discutez des domaines à renforcer, tels que les domaines techniques et commerciaux.
