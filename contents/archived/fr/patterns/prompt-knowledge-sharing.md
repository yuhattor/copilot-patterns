# Prompt Partage de connaissances

{% hint style="info" %}
Ce document est encore en cours de validation. Nous espérons des discussions actives sur la [question GitHub](https://github.com/AI-Native-Development/patterns/issues/8).
{% endhint %}

## Description

Il est important de partager des prompts pour générer du code et de les utiliser comme ressources pour que les membres de l'équipe puissent apprendre.

## Problème

En travaillant avec l'IA, telle que GitHub Copilot, nous pouvons écrire un code de haute qualité, mais ce qui est considéré comme un bon code pour la lecture de code par des ingénieurs avancés est une autre histoire. Il peut être difficile pour les ingénieurs de collaborer dans des domaines spécifiques lorsque le code est excessivement abrégé ou représenté par des expressions linguistiques spécifiques.

## Histoire

Vous cherchez des prompts pour maîtriser GitHub Copilot. En travaillant sur une fonctionnalité, vous avez collaboré avec GitHub Copilot pour produire un excellent code après des essais et des erreurs. Un ingénieur de l'équipe qui était assis à côté de vous a dit : "Vous écrivez toujours de cette façon ! Je commence à comprendre comment vous produisez toujours un excellent code."

Vous avez réalisé que les prompts que vous avez utilisés pour atteindre le meilleur résultat possible et le processus d'essai et d'erreur en lui-même sont des ressources importantes pour que les membres de l'équipe apprennent. Vous avez également découvert le problème que les prompts ne sont pas inclus dans les fichiers de production, et vous avez commencé à réfléchir à la meilleure façon de les partager.

## Contexte

GitHub Copilot est installé, mais chaque ingénieur l'utilise individuellement sans partager sa méthode. En outre, les prompts utilisés par chaque ingénieur avec GitHub Copilot ne sont pas partagés.

## Solution

Examinez la méthode de partage des prompts et la manière de les commenter en équipe et établissez des règles. Il est souhaitable que les prompts soient des commentaires qui fonctionnent également comme documents pour éviter qu'ils ne soient trop bruyants.

Les modèles suivants sont envisageables pour le partage des prompts :

* Ajouter directement aux fichiers
  Les prompts peuvent être laissés dans les fichiers pour que l'équipe puisse apprendre à partir des prompts des autres membres. Il est important de laisser les prompts dans un équilibre approprié pour qu'ils ne deviennent pas un bruit inutile. Il est également possible de convertir une partie des prompts en documents ou en commentaires explicatifs. En outre, les prompts peuvent être revus avec le code pour améliorer la formation des ingénieurs.
* Documentation passive
  Les commentaires, y compris certains prompts, peuvent être inclus dans les demandes de tirage ou les commentaires des problèmes. Cela améliorera la lisibilité des fichiers contenant du code, mais il ne sera pas possible de consulter les prompts de référence dans l'éditeur.
* Programmation en groupe
  Au lieu de laisser les prompts dans les fichiers ou les demandes de tirage/problèmes, organisez des sessions de programmation en groupe pour que les ingénieurs puissent expérimenter l'environnement de développement des ingénieurs expérimentés. Il est important de partager les enseignements tirés de ces sessions sous forme de documents distincts.

## Contexte résultant

Les compétences de toute l'équipe s'améliorent et l'apprentissage efficace est favorisé grâce au partage de prompts. La lisibilité du code s'améliore également, et la compréhension du code devient plus facile grâce aux commentaires qui fonctionnent comme des documents plutôt qu'à des niveaux de prompts.
