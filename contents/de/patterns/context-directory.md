# Kontext-Verzeichnis

Alias: Verzeichnis für Snippet-Einschlüsse

## Beschreibung

Durch Sammeln des Kontexts des gesamten Codebasis im Kontext-Verzeichnis im Repository können Entwickler während der Entwicklung GitHub Copilot einen genauen Kontext übergeben.

## Problem

* Ungenaue Vorschläge
  GitHub Copilot kann den Kontext der gesamten Codebasis nicht erfassen und kann daher ungenaue Vorschläge machen. Dies kann die Codequalität verringern oder dazu führen, dass Entwickler mehr Zeit für Korrekturen oder Anpassungen aufwenden müssen.
* Effizienzverlust
  Wenn Entwickler verwandte Dateien nicht in benachbarten Tabs offen halten, kann GitHub Copilot keine Informationen aus diesen Dateien abrufen. Dies führt zu ungenauen Vorschlägen und erfordert, dass Entwickler manuell nach verwandten Dateien suchen und diese während des Schreibens von Code referenzieren. Dies kann die Produktivität von Entwicklern beeinträchtigen.
* Verlust der Codekonsistenz
  Wenn der Kontext der gesamten Codebasis nicht erfasst werden kann, können die von GitHub Copilot vorgeschlagenen Code-Beispiele inkonsistent mit dem vorhandenen Code sein. Dies kann die Lesbarkeit und Wartbarkeit des Codes beeinträchtigen und die Entwicklungsgeschwindigkeit des Teams insgesamt verlangsamen.

## Geschichte

Eines Tages entschied sich ein Entwickler im Projektteam, GitHub Copilot zu verwenden, um eine neue Funktion zu entwickeln. Sie war begeistert von GitHub Copilot und dachte, dass sie damit schnell Code schreiben könnte.

Allerdings bemerkte sie im Laufe der Entwicklung, dass die von GitHub Copilot vorgeschlagenen Code-Beispiele manchmal ungenau waren. Trotzdem korrigierte sie diese manuell und arbeitete weiter, aber allmählich wurde sie müde von dieser Arbeit. Außerdem bemerkten auch andere Teammitglieder, dass die von GitHub Copilot vorgeschlagenen Code-Beispiele inkonsistent waren.

Sie fragte sich, warum GitHub Copilot keine genauen Vorschläge macht und begann zu recherchieren. Dabei stellte sie fest, dass ein Grund dafür war, dass sie verwandte Dateien nicht korrekt geöffnet hatte und daher nicht alle relevanten Informationen an GitHub Copilot übertragen wurden. Auf der anderen Seite ist es jedoch auch nicht realistisch, alle Dateien geöffnet zu halten, und sie erkannte auch, dass es bei dem von GitHub Copilot verwendeten Modell, Codex, eine Begrenzung für die Anzahl der Token gibt, die übergeben werden können.

Daher beschloss sie, das Kontext-Verzeichnismuster einzuführen. Durch Offenhalten verwandter Dateien kann GitHub Copilot genauere Vorschläge machen.

## Kontext

GitHub Copilot, das bekannte Produkt für AI-Code-Unterstützungswerkzeuge, macht Vorschläge auf der Grundlage von Informationen aus der aktuellen Datei oder aus anderen Dateien mit der gleichen Erweiterung, die in einem geöffneten Tab in VS Code angezeigt werden. Die Anzahl der Tokens, die dem von GitHub Copilot verwendeten Codex-Modell übergeben werden können, ist begrenzt. Daher send en GitHub Copilot-Erweiterungen wie VS Code nicht alle Informationen aus allen geöffneten Dateien als Referenzinformationen an den GitHub Copilot-Server. Stattdessen werden nur die relevanten Dateien mit hoher Ähnlichkeit priorisiert und als Teil der Sendungsdaten enthalten, einschließlich Snippets, die als "Snippet-Einschlüsse" bezeichnet werden.

Daher müssen nur die relevanten Tabs mit verwandten Dateien geöffnet bleiben, um effektive Code-Vervollständigung zu erhalten. Es sollten weder zu wenige noch zu viele Tabs geöffnet sein.

## Lösung

1. Erstellen Sie ein Kontext-Verzeichnis
Erstellen Sie ein Verzeichnis, in dem Sie Dateien sammeln, die Sie GitHub Copilot als Kontext oder Regel beibringen möchten, und die Sie als unterstützende Dateien verwenden möchten.
2. Schließen Sie Dateien, die nicht mit der aktuellen Entwicklung zusammenhängen
3. Halten Sie in VSCode Tabs mit Dateien geöffnet, die mit der aktuellen Entwicklung zusammenhängen
GitHub Copilot verfügt derzeit nicht über eine Funktion zum Erfassen des Kontexts der gesamten Codebasis. Stattdessen kann es jedoch die aktuellen Dateien und die in VSCode geöffneten Dateien lesen. Wenn verwandte Dateien in geöffneten Tabs gehalten werden, kann GitHub Copilot genauere Vorschläge machen.

## Ergebnis

Die Verwendung des Kontext-Verzeichnisses ermöglicht es GitHub Copilot, genauere Vorschläge zu machen. Durch das Offenhalten von Tabs mit verwandten Dateien erhalten Sie eine effektive Code-Vervollständigung.

## Hinweis

* Derzeit liest GitHub Copilot nur bestimmte Dateien. Wenn Sie beispielsweise Python schreiben, sollten die Snippet-Dateien und Referenzdateien auch Python-Code enthalten.
* Wenn Sie möchten, können Sie diese Verzeichnisse in .gitignore aufnehmen, um sicherzustellen, dass der Inhalt nicht gepusht wird.
* Sie können auch Git-Submodule verwenden, um das Kontext-Verzeichnis als separate Einheit zu extrahieren.
