# AI Native Dokumentation

Durch den Einsatz von AI-Technologien wie GitHub Copilot kann sich die Arbeit der Ingenieure im Entwicklungsteam ändern und letztendlich auch Auswirkungen auf die Architektur haben.
In diesem Dokument wird beschrieben, welche Auswirkungen die Entwicklungsmethoden von AI Native haben könnten.

## Der Kontext ist alles

Wenn AI-Technologien wie GitHub Copilot in die Entwicklungsumgebung und den Entwicklungsprozess integriert werden, gibt es viele verschiedene Bereiche zu berücksichtigen.
Entwicklerteams müssen den Kontext besser verstehen, um eine höhere Entwicklungsrate zu erreichen.
Es ist wichtig zu berücksichtigen, welche technischen und geschäftlichen Kontexte in Ihrem Programm vorhanden sind.
Dies war schon immer ein wichtiges Thema, aber mit der Einführung von AI, die Entwickler unterstützt, ist es noch wichtiger geworden, diese beiden Kontexte erneut zu betrachten.
Diese Kontexte können sich auf die Architektur und die Karriere des Ingenieurs auswirken.

Jeder Kontext kann Bereiche mit hohem oder niedrigem Kontext enthalten.
Zum Beispiel kann es bei der Codierung ausreichend sein, einfache Aufgaben auszuführen, die GitHub Copilot einfach vorschlägt und durch das Drücken der Tabulatortaste ausgeführt werden können.
In Bereichen mit hohem Kontext ist jedoch mehr Wissen und Erfahrung erforderlich, um erfolgreich zu sein.

### Technischer Kontext

Um den technischen Kontext zu verstehen, betrachten wir einige Programmiersprachen.
Einige Sprachen wie Python haben eine gemeinsame Syntax, um bestimmte Aufgaben auszuführen, während andere Sprachen wie Ruby mehrere Möglichkeiten haben, um die gleiche Aufgabe zu lösen.
Der Umfang des Scopes ist auch ein Problem.
Einige Sprachen haben einen globalen Scope wie BASIC, während andere Sprachen einen engeren Scope haben.
Zum Beispiel sind Referenzen und Ausleihungen in Rust ein typisches Beispiel für einen technischen Kontext mit hohem Kontext.
Auf Framework-Ebene kann dieser Kontext noch komplexer werden.

### Geschäftlicher Kontext

Gleiches gilt für den Geschäftsbereich.
Betrachten wir die SQL-Datenbanksprache.
AI ist gut darin, repetitive Aufgaben wie das Kopieren von Standardausdrücken zu automatisieren.
Wenn Sie jedoch eine komplexe, umfangreiche Datenbank bearbeiten müssen, kann es schwierig sein, darauf zu vertrauen, dass der von AI generierte Code keine Auswirkungen auf andere Prozesse hat.
Es ist wichtig, die Gesamtarchitektur zu verstehen und eine gewisse Kenntnis der Logik zu haben.
In Bezug auf Tests ist es für AI einfach, Tests basierend auf einem bestimmten Szenario zu schreiben, aber es kann schwierig sein, umfassende Testszenarien zu erstellen.
Es ist einfach, API-Tests für eine REST-API mit einfachen CRUD-Funktionen zu schreiben, aber es kann schwierig sein, Tests für Anwendungen zu schreiben, die komplexe Genehmigungsbedingungen haben.

## AI Native Architektur

Wie viel Kontext ist in der Architektur Ihrer Anwendung vorhanden?
Wenn es viele Kontexte in der Architektur gibt, kann die Verwendung von AI zur Entwicklung zu einer Verringerung der Entwicklungsrate führen.
Dies liegt daran, dass die Kontexte, die von LLM verstanden werden können, begrenzt sind und es nicht möglich ist, AI gleichzeitig eine große Menge an Kontexten zur Verfügung zu stellen.
Es gibt eine Obergrenze für die Anzahl der Token, die AI verarbeiten kann, und im Allgemeinen kann der Mensch nicht alle Informationen in einer für AI lesbaren Form bereitstellen.
AI kann unbegrenzt arbeiten, solange es mit Eingaben versorgt wird, aber die Zeit, in der der Mensch AI anweisen kann, ist begrenzt.
In diesem Fall wird der Engpass in der Entwicklung von Menschen verursacht.
Deshalb sollten Sie überlegen, die Kontexte von Funktionen und Anwendungen zu reduzieren, um sicherzustellen, dass AI trotzdem das richtige Programm schreiben kann, ohne von einem menschlichen Entwickler unterstützt zu werden.

Es ist eine gute Idee, Dienste auf kleinere Einheiten aufzuteilen und eine lose Verbindung herzustellen.
Ich spreche jedoch nicht von Mikroservices im Kontext von Kubernetes.
Jede Art von Design, einschließlich SOA oder Bibliotheksebene, ist akzeptabel.
Es ist wichtig, Komponenten in einfache und testbare Einheiten aufzuteilen.
Je mehr Kontexte eine Anwendung hat, desto schwieriger wird es, Unterstützung von AI zu erhalten.

Die Größe des Programms ist manchmal Gegenstand von religiösen Diskussionen und die Verwendung von AI in der Entwicklung hat gerade erst begonnen, daher gibt es keine genaue Antwort.
Wenn Sie jedoch die Produktivität der Ingenieure maximieren und das Produkt so schnell wie möglich entwickeln möchten, sollten Sie eine Entwicklungsmethode oder -architektur in Betracht ziehen, die auf GitHub Copilot basiert.

Was Sie jedoch nicht vergessen sollten, ist, dass die IT-Architektur nicht darauf ausgerichtet sein sollte, die Produktivität der Entwickler zu maximieren.
Engineering sollte immer als Mittel zur Erreichung des Endziels angesehen werden.

Ich hoffe, dass Sie aktiv an Diskussionen in diesem Bereich teilnehmen werden.

## Aussichten für eine Karriere als Ingenieur

Bisher haben wir uns mit der Möglichkeit befasst, dass KI Veränderungen in der Architektur und Entwicklungskultur bewirken kann. Hier ist es wichtig, auch auf die Karriere im Ingenieurwesen zu achten. Dies gilt nicht nur für Ingenieure selbst, sondern auch für Manager und Personen, die Positionen im Aufbau von Organisationen innehaben.

Letztendlich müssen Ingenieure darüber nachdenken, ob sie ein breites Wissen über Geschäftsprodukte anstreben oder sich auf technisch anspruchsvolle Ingenieure konzentrieren möchten. Doch das Problem besteht darin, dass es in beiden Bereichen Bereiche mit niedrigem und hohem Kontext gibt.

Beispielsweise könnte es ausreichen, bei der Codierung einfache Aufgaben zu wiederholen oder Prozesse zu schreiben, bei denen es am Ende darauf ankommt, wer sie schreibt, und dafür einfach die von GitHub Copilot vorgeschlagenen Vorschläge durch das Drücken der Tab-Taste zu verwenden. Auf der anderen Seite erfordern die in den technischen und geschäftlichen Kontextbereichen angegebenen Bereiche einen hohen Kontext. Dies sind Bereiche, in denen Erfahrung und spezifisches Wissen in technischen Bereichen gefragt sind und die nicht einfach zu erlernen sind. Wenn das Wissen im Internet verfügbar ist, kann es noch eingeholt werden. Wenn es sich jedoch um einen spezifischen Wissensbereich handelt, der auf eine bestimmte Organisation beschränkt ist und nicht dokumentiert ist oder dessen Beschaffung sehr kostenintensiv ist, kann das Aufholen schwierig sein.

Dies gilt nicht nur für die Codierung, sondern KI tendiert auch dazu, Menschen mit umfassendem Wissen und Erfahrung zu stärken. Dies bedeutet, dass Experten ihre Arbeit verlieren können. Wenn dies nicht behoben wird, können neue Mitarbeiter wichtige Aufgaben in der Organisation nicht übernehmen und das Wachstum ihrer Fähigkeiten bleibt aus. Die Fähigkeiten der Experten steigen weiter an, und es wird schwieriger, sie als Organisation zu halten. Es wird auch schwieriger, Neulinge, die nur langweilige Aufgaben erledigen, die von erfahrenen Mitarbeitern aufgrund von Zeitbeschränkungen nicht durchgeführt werden können, an das Unternehmen zu binden.

Was ist also zu tun? Eine Möglichkeit besteht darin, technische und geschäftliche Informationen zu Produkten oder Organisationen als Dokumente mit Kontext zusammenzufassen und intern zu entwickeln. Wenn viele Menschen an der Erstellung dieser Dokumentation beteiligt sind und eine Zusammenarbeit stattfindet, entsteht eine Wissensdatenbank für das Unternehmen. Jetzt ist es an der Zeit, eine Art interne Zusammenarbeit ähnlich wie bei Open-Source-Projekten zu fördern.

## Checkliste

- [ ] Welchen Kontext hat Ihr Projekt oder Produkt? Versuchen Sie, den Kontext zu organisieren.
- [ ] Wird dieser Kontext nur von einigen wenigen Personen monopolisiert oder wird er im Team geteilt?
- [ ] Kann die KI Ihren Code in einem niedrigen Kontext verstehen oder haben Sie hauptsächlich Kontext-Code? Wenn ja, wie können Sie den Code in einen leichter schreibbaren Code umwandeln?
- [ ] Förd ern Sie die interne Zusammenarbeit in Ihrem Unternehmen? Wenn nicht, überlegen Sie, wie Sie die Kommunikation und den Wissensaustausch innerhalb und zwischen Teams verbessern können.
- [ ] Wurden Diskussionen über Karrierewege im AI-Zeitalter Ihrer Ingenieure geführt? Sprechen Sie darüber, ob Sie Bereiche wie technische und geschäftliche Aspekte stärken möchten.
