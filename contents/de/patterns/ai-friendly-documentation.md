# AI-freundliche Dokumentation

## Beschreibung

Durch das Erstellen von Dokumentationen im Format, das von KI verstanden werden kann, kann das Team insgesamt produktiver werden, nicht nur die Ingenieure, die Code schreiben. Als Beispiel könnte die Definition einer Datenbanktabelle als Markdown-Dokumentation verwaltet werden, anstatt in PowerPoint oder Excel, und als Dokumentation in Git verwaltet werden.

## Problem

In der Produktentwicklung sind verschiedene Dokumente wie Anforderungsdefinitionen, Entwurfsdokumente, Architekturübersichten, Infrastrukturkonfigurationsspezifikationen, Testfalldokumente usw. erforderlich. Im Allgemeinen bevorzugen Menschen Formate wie PowerPoint oder Excel, aber KI kann diese Dokumente nicht lesen. Es ist auch keine bewährte Methode, binäre Dateien in Git-Repositories zu verwalten.

## Geschichte

In Ihrem Team wurde GitHub Copilot for Business eingeführt. Die Ingenieure sind begeistert, dass die Arbeitszeit verkürzt wird. Das Team fühlt sich, als ob es durch die Hilfe von KI verdoppelt worden wäre. Allerdings kann die KI nur das tun, was die Ingenieure ihr vorgeben. Da die KI den Kontext, den die Ingenieure haben, nicht versteht, müssen sie viel natürliche Sprache eingeben, um ihr mehr Kontext zu vermitteln. Deshalb müssen sie häufig Texte, die ihnen vom Projektmanager gegeben wurden, kopieren und einfügen oder PowerPoint-Folien und komplexe Excel-Formate in Markdown oder CSV-Formate konvertieren, die von der KI gelesen werden können.

"Wäre es nicht einfacher, wenn alles von Anfang an in CSV oder Markdown geschrieben wäre?"

## Kontext

In vielen Projekten werden Dokumente wie PowerPoint oder Excel für die Dokumentation verwendet. Andere Personen als die Ingenieure kommunizieren an anderen Orten als GitHub, und endgültige Entscheidungen werden nicht im Repository gespeichert. Die Dokumentation ist für die KI leicht lesbar, aber nicht zentral verwaltet.

## Lösung

Das Team sollte sich bemühen, textbasierte Dokumente wie Markdown oder CSV zu erstellen. Das Dokument, das den Kontext enthält, der schließlich an die Ingenieure und KI übergeben werden soll, sollte im Git-Repository gespeichert werden. Das Repository sollte so eingerichtet werden, dass es leicht von externen Quellen in den Workspace importiert werden kann, z. B. unter Verwendung von Git-Submodulen. Wenn nötig, kann der Text des Dokuments in den Kommentarbereich kopiert und als Prompt an die KI übergeben werden.

## Bekanntes Beispiel

* Die Tabellendefinition sollte als CSV- oder Markdown-Datei vorbereitet und mit der Erstellung der Migration-Datei oder der Interface verknüpft werden.
* Die in natürlicher Sprache zusammengefasste Infrastrukturdefinition sollte in Konfigurationsdateien für Infrastructure as Code wie Terraform umgewandelt werden.
* Die Testfalldokumentation sollte in Testdateien konvertiert werden. Für bestimmte Muster wie API-Tests ist dies effektiver und erleichtert die Testgetriebene Entwicklung.

## Ergebnis

* Die Ingenieure können mit weniger Aufwand mehr Code erstellen, was zu einer Verringerung der Arbeitsbelastung führt.
* Projektbesitzer und Produktmanager können schneller Ergebnisse von den Ingenieuren erhalten.
* Mitglieder, die normalerweise keinen Code schreiben, können durch die Zusammenarbeit mit GitHub lernen, wie sie den Kontext bereitstellen und die richtige Entwicklung mit Hilfe von KI durchführen können.
* Da Änderungen an Dokumentationen verfolgt werden, ist es möglich, das Entscheidungsdatum und die Personen, die Änderungen vorgenommen haben, auch für Dokumentationen zu verfolgen.
* Es gibt keine Diskrepanz zwischen Dokumentation und Implementierung.

## Hinweis

* Derzeit kann GitHub Copilot nur bestimmte Arten von Dateien lesen. Wenn Sie beispielsweise Python schreiben, wird nur der Python-Code in den geöffneten Registerkarten von Copilot gelesen und an die Prompt übergeben. Daher sollten Sie die benötigten Abschnitte aus der KI-freundlichen Dokumentation kopieren und in den Kommentarbereich der ```.py```-Datei einfügen.
* Dieser Ansatz ist nicht für alle Arten von Dokumentationen geeignet. Wenn Sie die falsche Entscheidung treffen, welche Dokumente zu speichern sind, kann dies zu einer großen Anzahl unnötiger Dokumente im Repository und einer schlechteren Suchleistung führen. Es ist ratsam, Implementierungsnahen Text vorzuziehen, um in Markdown zu schreiben.
* Es gibt eine Begrenzung für die Anzahl der Token, die an die KI übergeben werden können. Versuchen Sie also, jeden Abschnitt des Dokuments prägnant zusammenzufassen, damit er so wenig wie möglich von anderen Abschnitten abhängt.
