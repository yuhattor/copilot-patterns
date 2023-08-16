# Prompt Condivisione della conoscenza

{% hint style="info" %}
Questo documento è ancora in fase di verifica. Ci aspettiamo una discussione attiva sulla questione su GitHub Issue (https://github.com/AI-Native-Development/patterns/issues/8).
{% endhint %}

## Descrizione

È importante condividere i prompt per la generazione di codice e utilizzarli come risorse per l'apprendimento dei membri del team.

## Problema

Lavorare con l'AI come GitHub Copilot per sviluppare del codice di alta qualità può aiutare, ma per gli ingegneri esperti, un buon codice o un codice performante non è necessariamente un buon codice da leggere. La collaborazione degli ingegneri in un'area specifica potrebbe diventare difficile quando il programma è rappresentato con codice altamente abbreviato o espressioni linguistiche avanzate.

## Storia

Stai cercando di capire quali prompt scrivere per padroneggiare GitHub Copilot. Mentre implementi una funzionalità, come ingegnere esperto, dopo molti tentativi riesci a produrre un codice eccellente collaborando con GitHub Copilot. Un ingegnere del tuo stesso team seduto accanto a te ti dice: "Eri sempre così bravo a scrivere così! Ora capisco un po' come fai a produrre sempre del codice eccellente."

Hai realizzato che il prompt che hai usato per raggiungere il miglior risultato possibile e il processo di tentativi ed errori sono importanti risorse per l'apprendimento dei membri del team. Hai anche scoperto il problema di non avere prompt nel file di output e hai cominciato a pensare a come condividerli.

## Contesto

GitHub Copilot è stato introdotto, ma ogni ingegnere lo usa individualmente e non c'è condivisione di come utilizzarlo. Inoltre, i prompt scritti da ciascun ingegnere su GitHub Copilot non sono condivisi.

## Soluzione

Il team dovrebbe esaminare come condividere i prompt e come scrivere i commenti, stabilendo regole. I prompt dovrebbero diventare commenti che fungono da documenti per non creare rumore.

Ecco alcuni modi per condividere i prompt:

* Scrivere direttamente sui file
  Scrivere i prompt sui file che il team può imparare da altri membri del team. È importante bilanciare i prompt per non creare rumore e convertire una parte dei prompt in documenti o commenti esplicativi. Durante la revisione del codice, è possibile esaminare anche i prompt e promuovere lo sviluppo degli ingegneri.
* Documentazione passiva
  Includere alcuni prompt nei commenti di pull request o issue. Ciò migliorerà la leggibilità dei file contenenti codice, ma non sarà possibile accedere ai prompt di riferimento nell'editor.
* Programmazione in mob
  Organizzare sessioni di programmazione in mob per far vivere ai membri del team l'esperienza di sviluppo degli ingegneri esperti senza lasciare prompt nei file o nelle PR/Issues. È importante condividere ciò che si impara come documento separato.

## Contesto

In questo modo, l'intero team migliorerà le proprie competenze e la condivisione dei prompt favorirà l'apprendimento efficace. La leggibilità del codice aumenterà e la comprensione del codice sarà facilitata grazie ai commenti che fungono da documentazione, piuttosto che da prompt.
