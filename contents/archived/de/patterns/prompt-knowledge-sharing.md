# Prompt Wissensaustausch

{% hint style="info" %}
Dieses Dokument befindet sich noch in der Überprüfung. Wir hoffen auf eine aktive Diskussion über [GitHub Issues](https://github.com/AI-Native-Development/patterns/issues/8).
{% endhint %}

## Beschreibung

Es ist wichtig, Prompts zum Erstellen von Code zu teilen und als Ressource für Teammitglieder zu nutzen, um zu lernen.

## Problem

Durch die Zusammenarbeit mit KI wie GitHub Copilot können hochwertige und leistungsstarke Codes erstellt werden. Für erfahrene Ingenieure ist jedoch die Frage, ob großartiger Code und leistungsstarker Code guter Code für das Lesen von Code sind, eine andere Frage.
Es besteht die Möglichkeit, dass die Zusammenarbeit von Ingenieuren in bestimmten Bereichen schwieriger wird, wenn der Code zu stark abgekürzt oder durch hochentwickelte sprachspezifische Ausdrücke dargestellt wird.

## Geschichte

Sie suchen nach Prompt, um GitHub Copilot voll auszunutzen. Als erfahrener Ingenieur haben Sie bei der Implementierung einer bestimmten Funktion durch Versuch und Irrtum großartigen Code mit GitHub Copilot erzeugt.
Ein Ingenieur aus dem gleichen Team, der dies neben Ihnen beobachtete, sagte: "Sie haben immer auf diese Weise geschrieben! Ich denke, ich verstehe jetzt, wie Sie immer großartigen Code erstellen."
Sie bemerkten, dass der Prompt, den Sie geschrieben haben, um zum besten Ergebnis zu gelangen, und der Prozess des Versuchens und Irrtums selbst wichtige Ressourcen sind, die Teammitglieder lernen können.
Gleichzeitig entdeckten Sie das Problem, dass der Prompt nicht in der Datei des Endprodukts enthalten war, und begannen darüber nachzudenken, wie er am besten geteilt werden kann.

## Kontext

GitHub Copilot wurde eingeführt, aber jeder Ingenieur verwendet ihn individuell und seine Verwendung wird nicht geteilt.
Darüber hinaus werden die von jedem Ingenieur in GitHub Copilot geschriebenen Prompts nicht geteilt.

## Lösung

Überlegen Sie im Team, wie Prompts geteilt und kommentiert werden sollen, und erstellen Sie Regeln. Es ist wünschenswert, dass der Kommentar als Dokument dient, um sicherzustellen, dass der Prompt nicht zum Rauschen wird.

Es gibt folgende Muster für das Teilen von Prompts:

* Direkt in die Datei schreiben
  Durch das Speichern von Prompts in der Datei für das Teamlernen können Teams von den Prompts anderer Mitglieder lernen. Es ist wichtig, den Prompt in einem angemessenen Gleichgewicht zu halten, um sicherzustellen, dass er nicht zum Rauschen wird. Es ist auch möglich, einen Teil davon in Dokumente oder erklärende Kommentare umzuwandeln. Durch das Überprüfen von Prompts während des Code-Reviews können Ingenieure besser geschult werden.
* Passive Dokumentation
  Enthält einige Prompts als Kommentare für Pull Requests oder Issues. Die Lesbarkeit der Datei mit dem Code verbessert sich, aber es ist nicht möglich, die Referenzprompts im Editor zu sehen.
* Mob-Programmierung
  Es werden keine Prompts in der Datei oder im PR/Issue hinterlassen, aber Mob-Programmiers-Sitzungen mit erfahrenen Ingenieuren werden abgehalten, um das Entwicklungsleben erfahrener Ingenieure zu erleben. Es ist wichtig, diese Erfahrung als separates Dokument zu teilen.

## Ergebnis

Das gesamte Team verbessert seine Fähigkeiten und effektives Lernen wird durch das Teilen von Prompts gefördert.
Die Lesbarkeit des Codes verbessert sich und das Verständnis des Codes wird durch Kommentare ermöglicht, die nicht auf dem Niveau des Prompts, sondern als Dokument funktionieren.
