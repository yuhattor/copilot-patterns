# Répertoire de contexte

Alias: Répertoire de snippet pour inclusion

## Description

En collectant le contexte de l'ensemble du code dans le répertoire de contexte du dépôt, il est plus facile de fournir un contexte précis à GitHub Copilot pendant le développement.

## Problème

* Propositions imprécises
  GitHub Copilot peut proposer des suggestions imprécises en ne pouvant pas obtenir le contexte de l'ensemble du code, ce qui peut entraîner une baisse de la qualité du code ou une augmentation du temps que les développeurs passent à effectuer des modifications ou des ajustements.
* Baisse d'efficacité
  Si les développeurs ne laissent pas les fichiers pertinents ouverts dans des onglets adjacents, GitHub Copilot ne peut pas obtenir les informations à partir de ces fichiers. Cela peut entraîner des suggestions imprécises et obliger les développeurs à rechercher et à référencer manuellement les fichiers pertinents tout en écrivant du code, ce qui peut réduire leur productivité.
* Perte de cohérence du code
  Si GitHub Copilot ne peut pas obtenir le contexte de l'ensemble du code, les suggestions de code peuvent ne pas être cohérentes avec le code existant. Cela peut avoir un impact négatif sur la lisibilité et la maintenabilité du code et ralentir la vitesse de développement de l'équipe.

## Histoire

Un jour, un ingénieur de l'équipe de projet a décidé d'utiliser GitHub Copilot pour développer une nouvelle fonctionnalité. Elle était très intéressée par GitHub Copilot et pensait qu'il pourrait l'aider à écrire du code plus rapidement.

Cependant, au fil du développement, elle a remarqué que les suggestions de code proposées par GitHub Copilot étaient parfois imprécises. Malgré cela, elle a continué à corriger manuellement les suggestions et à poursuivre son développement, mais elle a fini par se fatiguer de cette tâche. En outre, d'autres membres de l'équipe ont également signalé que les suggestions de code proposées par GitHub Copilot manquaient de cohérence.

Elle s'est alors demandé pourquoi GitHub Copilot ne proposait pas de suggestions précises et, lorsqu'elle a commencé à enquêter, elle a découvert que cela était dû au fait qu'elle n'avait pas correctement ouvert les fichiers pertinents. D'autre part, il n'est pas réaliste de laisser tous les fichiers ouverts, et elle a réalisé que le modèle Codex utilisé par GitHub Copilot a une limite de jetons qu'il peut transmettre.

Elle a donc décidé d'introduire le modèle de répertoire de contexte. En laissant les fichiers pertinents ouverts, elle espère que GitHub Copilot pourra fournir des suggestions plus précises.

## Contexte

GitHub Copilot, un produit représentatif des outils d'assistance à la programmation basés sur l'IA, propose des suggestions en fonction des informations sur les fichiers actuellement ouverts ou des fichiers avec la même extension ouverte dans des onglets. Les extensions de fichiers pour les snippets inclus sont appelées "inclusions de snippets".

Par conséquent, il est nécessaire d'ouvrir le nombre approprié de fichiers pertinents dans des onglets adjacents pour permettre à GitHub Copilot de fournir une complétion de code efficace. Les extensions de fichiers pour les snippets inclus sont appelées "inclusions de snippets". Les extensions de fichiers pour les snippets inclus sont appelées "inclusions de snippets".

## Solution

1. Créez un répertoire de contexte
Créez un répertoire contenant des fichiers supplémentaires, tels que des règles ou du contexte que vous souhaitez que GitHub Copilot apprenne.
2. Fermez les fichiers qui ne sont pas liés au développement en cours
3. Ouvrez les fichiers pertinents pour le développement actuel dans des onglets dans VSCode
Bien que GitHub Copilot ne dispose pas actuellement de la fonctionnalité de collecte du contexte de l'ensemble du code, il peut lire les fichiers actuels et les fichiers ouverts dans l'éditeur. En laissant les fichiers pertinents ouverts, GitHub Copilot peut fournir des suggestions plus précises.

## Contexte résultant

L'utilisation du répertoire de contexte permet à GitHub Copilot de fournir des suggestions plus précises. En laissant les fichiers pertinents ouverts dans des onglets adjacents, vous pouvez obtenir une complétion de code efficace.

## Remarque

* Les fichiers que GitHub Copilot lit sont limités. Si vous écrivez en Python, il est préférable que les fichiers de snippet et les fichiers de référence soient également en Python.
* Si nécessaire, vous pouvez ajouter ces répertoires à .gitignore pour ne pas les envoyer lors d'un push.
* En outre, vous pouvez utiliser Git Submodule pour extraire le répertoire de contexte en tant qu'entité distincte.
