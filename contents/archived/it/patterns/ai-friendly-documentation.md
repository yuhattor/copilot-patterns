# Documentazione amica dell'AI

## Descrizione

Non solo gli ingegneri che scrivono il codice, ma l'intero team può migliorare la produttività creando documentazione in un formato comprensibile all'AI.
Ad esempio, invece di scrivere la definizione della tabella del database in PowerPoint o Excel, si può scrivere in Markdown e gestirla tramite git come documentazione.

## Problema

Nello sviluppo del prodotto, sono necessari vari documenti come la definizione dei requisiti, la specifica di progettazione, il diagramma dell'architettura, la specifica della configurazione dell'infrastruttura, il documento dei casi di test, ecc.
In genere, i formati come PowerPoint o Excel sono preferiti, ma l'AI non può leggere questi documenti.
Inoltre, la gestione dei file binari in un repository Git non è una buona pratica.

## Storia

Il tuo team ha introdotto GitHub Copilot for Business.
Gli ingegneri sono felici di avere meno tempo di lavoro. Il team si sente come se avesse il doppio del numero di membri grazie all'AI.
Tuttavia, il problema è che l'AI può fare solo ciò che gli ingegneri gli indicano.
Inoltre, poiché l'AI non comprende il contesto che gli ingegneri hanno, gli ingegneri devono inserire molte parole naturali per trasmettere il contesto all'AI.
Di conseguenza, c'è un aumento del lavoro per convertire i testi forniti dal PM o le presentazioni PowerPoint o le complesse tabelle Excel create dal superiore in formato Markdown o CSV leggibili dall'AI.

"Sarebbe stato meglio se fossero stati scritti in CSV o Markdown fin dall'inizio!"

## Contesto

In molti progetti, la documentazione è gestita in formati come PowerPoint o Excel. Le persone non ingegneri comunicano altrove rispetto a GitHub e le decisioni finali non sono salvate nel repository. I documenti sono organizzati in un formato facile da leggere per l'AI, ma non sono gestiti in modo centralizzato.

## Soluzione

Il team cerca di creare documenti basati su testo come Markdown o CSV.
I documenti che devono essere forniti agli ingegneri e all'AI devono essere salvati nel repository Git.
Il repository deve essere facilmente accessibile dallo spazio di lavoro utilizzando strumenti come Git Submodule.
Se necessario, il testo dei file può essere copiato nei commenti e fornito come prompt all'AI.

## Esempi noti

* Prepara la definizione della tabella in formato CSV o Markdown e associarla alla creazione del file di migrazione o all'interfaccia.
* Converti la definizione dell'infrastruttura riassunta in linguaggio naturale in file di configurazione dell'infrastructure as code come Terraform.
* Converti il documento dei casi di test in file di test. Questo è particolarmente efficace per i test di API e simili a modelli. Ciò rende più facile lo sviluppo basato sui test.

## Contesto risultante

* Gli ingegneri possono creare più codice con meno sforzo, riducendo le ore di lavoro.
* I proprietari del progetto e i project manager possono ottenere risultati più rapidamente dagli ingegneri.
* I membri che non scrivono codice possono abituarsi a valutare il contesto necessario per gli ingegneri e l'AI e possono contribuire alla collaborazione utilizzando GitHub, consentendo un'implementazione appropriata dell'AI.
* Grazie alla tracciabilità dei cambiamenti nei documenti, è possibile tenere traccia di chi ha apportato quali modifiche in quale momento e quando sono state prese le decisioni, non solo per il codice ma anche per la documentazione.
* Non c'è discrepanza tra documentazione e implementazione.

## Note

* Attualmente, GitHub Copilot legge solo alcuni tipi di file. Se si sta scrivendo in Python, ad esempio, solo il codice Python aperto nella scheda viene letto e fornito come prompt. Pertanto, copiare il testo necessario dalla documentazione amica dell'AI e incollarlo nei commenti del file .py è una soluzione pratica.
* Questo modello non è sempre efficace per tutti i tipi di documenti. Una cattiva gestione della documentazione può portare a una grande quantità di documenti inutili nel repository, riducendo le prestazioni di ricerca. Cerca di scrivere la maggior parte del testo in formato Markdown per i documenti più vicini all'implementazione.
* C'è un limite al numero di token che si possono fornire all'AI. Cerca di sintetizzare le sezioni di ogni documento in modo chiaro e sintetico, senza troppe dipendenze tra le frasi.
