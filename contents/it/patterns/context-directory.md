# Contesto Directory

Alias: Directory di snippet per l'inclusione degli snippet

## Descrizione

Raccogliere il contesto di tutto il codice nella directory di contesto all'interno del repository, semplifica il passaggio di contesto preciso a GitHub Copilot durante lo sviluppo.

## Problema

* Proposte imprecise
  GitHub Copilot potrebbe fare proposte imprecise in quanto non è in grado di ottenere il contesto dell'intero codice base, questo potrebbe portare a una riduzione della qualità del codice o ad un aumento del tempo necessario per le correzioni e gli aggiustamenti da parte degli sviluppatori.
* Riduzione dell'efficienza
  Se gli sviluppatori non mantengono aperti i file correlati nella scheda adiacente, GitHub Copilot non è in grado di ottenere informazioni da quei file. Questo può portare ad imprecisioni nelle proposte e ad un aumento del tempo necessario per scrivere il codice mentre gli sviluppatori cercano manualmente i file correlati. Questo potrebbe ridurre la produttività degli sviluppatori.
* Perdita di coerenza del codice
  Se il contesto dell'intero codice base non può essere ottenuto, il codice proposto da GitHub Copilot potrebbe non essere coerente con il codice esistente. Ciò potrebbe influire negativamente sulla leggibilità e manutenibilità del codice, rallentando la velocità di sviluppo dell'intero team.

## Storia

Un giorno, un ingegnere del team di progetto ha deciso di sviluppare una nuova funzionalità utilizzando GitHub Copilot. Era entusiasta di utilizzare GitHub Copilot e pensava che potesse aiutarla a scrivere codice più rapidamente.

Tuttavia, durante lo sviluppo, ha notato che a volte il codice proposto da GitHub Copilot non era preciso. Nonostante ciò, ha continuato a correggere manualmente il codice e ad avanzare nello sviluppo, ma alla fine è diventata sempre più stanca di questo lavoro. Inoltre, altri membri del team hanno fatto notare che il codice proposto da GitHub Copilot mancava di coerenza.

Ha iniziato a chiedersi perché GitHub Copilot non facesse proposte precise e, in seguito ad una ricerca, ha scoperto che il motivo era perché non aveva aperto correttamente i file correlati. Tuttavia, mantenere aperti tutti i file non era realistico e, considerando il modello Codex utilizzato da GitHub Copilot, ha capito che c'era un limite al numero di token che potevano essere passati.

Così ha deciso di introdurre il pattern della directory di contesto. Si aspettava che mantenendo aperti i file correlati, GitHub Copilot potesse fare proposte più precise.

## Contesto

Il prodotto principale degli strumenti di assistenza alla codifica AI, GitHub Copilot, fa proposte in base alle informazioni del file attualmente aperto o dei file con lo stesso suffisso aperti in una scheda.
Le estensioni di GitHub Copilot, come VS Code, non inviano tutte le informazioni sui file aperti al server di GitHub Copilot per suggerire, invece, ma inviano solo i file che sono simili a quelli attualmente aperti. Includere uno snippet viene chiamato "snippet inclusion".
Pertanto, è necessario mantenere aperti solo un numero appropriato di file correlati nella scheda adiacente. Aprire troppi o troppo pochi file potrebbe essere controproducente.

## Soluzione

1. Creare una directory di contesto
Creare una directory in cui mettere tutti i file che si desidera utilizzare per aiutare GitHub Copilot a comprendere il contesto o le regole del codice da apprendere, sia a livello individuale che di squadra.
2. Chiudere i file non pertinenti allo sviluppo in corso
3. Mantenere aperti i file pertinenti allo sviluppo attuale in una scheda di VS Code
Al momento, GitHub Copilot non ha la capacità di acquisire il contesto dell'intero codice base, ma è in grado di leggere il file attualmente aperto e i file aperti nell'editor. Mantenere aperti i file correlati in una scheda di VS Code aiuta GitHub Copilot a fare proposte più precise.

## Contesto risultante

L'utilizzo della directory di contesto consente a GitHub Copilot di fare proposte più precise. Mantenere aperti i file correlati nella scheda adiacente consente di ottenere un completamento del codice più efficace.

## Nota

* Attualmente, GitHub Copilot legge solo un numero limitato di file. Se si sta scrivendo in Python, è auspicabile che i file di snippet e i file di riferimento siano anche codice Python.
* Se necessario, è possibile aggiungere queste directory al file .gitignore per evitare di inviare il contenuto alla repository.
* Inoltre, è possibile utilizzare i Git Submodule per estrarre la directory di contesto come una repository separata.