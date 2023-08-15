# Documentation adaptée à l'IA

## Description

En créant de la documentation sous forme lisible par l'IA, l'équipe entière peut augmenter sa productivité. Ce type de documentation peut être compris non seulement par les ingénieurs qui écrivent le code, mais également par les systèmes d'IA. Par exemple, la définition d'une table de base de données peut être écrite en Markdown et gérée via Git en tant que documentation.

## Problème

Dans le cadre du développement de produits, différents documents sont nécessaires, tels que les cahiers des charges, les documents de conception, les schémas d'architecture, les spécifications de configuration d'infrastructure, les documents de cas de test, etc. En général, les formats tels que PowerPoint ou Excel sont préférés, mais ils ne peuvent pas être lus par l'IA. De plus, la gestion de fichiers binaires dans un référentiel Git n'est pas une bonne pratique.

## Histoire

Votre équipe a commencé à utiliser GitHub Copilot for Business. Les ingénieurs sont ravis de la réduction du temps de travail. Ils ont l'impression que l'aide de l'IA a doublé l'effectif de l'équipe. Cependant, l'IA ne peut réaliser que ce que les ingénieurs ont spécifié, sans comprendre le contexte qui les entoure. Pour transmettre suffisamment de contexte à l'IA, les ingénieurs doivent saisir de grandes quantités de langage naturel. Cela a conduit à une augmentation du travail de conversion des documents en PowerPoint, Excel et autres formats complexes en Markdown ou en CSV, qui peuvent être lus par l'IA.

« Si seulement tout avait été écrit en CSV ou en Markdown dès le départ ! »

## Contexte

Dans de nombreux projets, la documentation est gérée sous des formats tels que PowerPoint ou Excel. Les personnes autres que les ingénieurs communiquent en dehors de GitHub, et les décisions finales ne sont pas enregistrées dans le référentiel. Bien que la documentation soit présentée sous une forme lisible par l'IA, elle n'est pas gérée de manière centralisée.

## Solution

L'équipe s'efforce de créer des documents textuels tels que Markdown ou CSV. Les documents contenant le contexte nécessaire pour les ingénieurs et l'IA doivent être stockés dans un référentiel Git. Le référentiel peut être appelé à partir de l'espace de travail à l'aide de Git Submodule ou de technologies similaires. Si nécessaire, le texte des fichiers peut être copié dans les champs de commentaires pour être transmis à l'IA.

## Instance connue

* Préparation des fichiers de définition de table en CSV ou en Markdown, pour être associés aux fichiers de migration ou à la création d'interfaces.
* Conversion des définitions d'infrastructure rédigées en langage naturel en fichiers de configuration d'Infrastructure as Code, tels que Terraform.
* Conversion des documents de cas de test en fichiers de test. Cela est particulièrement efficace pour les tests d'API standardisés. Cela facilite le développement piloté par les tests.

## Contexte résultant

* Les ingénieurs peuvent écrire plus de code avec moins d'efforts, réduisant ainsi le temps de développement.
* Les propriétaires de projet et les gestionnaires de produits peuvent obtenir des résultats plus rapidement auprès des ingénieurs.
* Les membres qui n'écrivent pas normalement de code peuvent apprendre à juger du contexte nécessaire pour les ingénieurs et l'IA, en utilisant GitHub pour collaborer. Cela permet un développement approprié avec l'aide de l'IA.
* Les modifications apportées à la documentation sont enregistrées, ce qui permet de suivre les décisions et les modifications apportées à l'ensemble du projet, et pas seulement au code.
* La documentation est en phase avec la mise en œuvre.

## Note

* Actuellement, GitHub Copilot ne lit qu'un nombre limité de fichiers. Si vous écrivez du code Python, Copilot ne lira que le code Python dans l'onglet ouvert et vous pourrez lui donner des instructions en langage naturel. Par conséquent, copiez et collez les sections de documentation pertinentes dans le champ de commentaire du fichier .py.
* Cette méthode n'est pas toujours la meilleure pour tous les documents. Une mauvaise évaluation des documents à stocker peut entraîner la création de nombreuses documentations inutiles dans le référentiel, ce qui peut réduire les performances de recherche. Essayez de privilégier l'écriture en Markdown pour les sections plus proches de la mise en œuvre.
* Le nombre de tokens que l'IA peut recevoir est limité. Essayez de résumer chaque section de texte de manière concise, sans trop de dépendances avec les autres sections.
