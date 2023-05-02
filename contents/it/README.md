# Guida allo sviluppo AI-Native

Benvenuto nella Guida allo sviluppo AI-Native!
Questo documento è gestito dalla comunità di sviluppo AI-Native.
In questo documento, abbiamo raccolto le migliori pratiche per lo sviluppo AI-Native utilizzando strumenti come GitHub Copilot in un formato specifico, in modo da poterle facilmente comprendere, valutare e applicare alla tua situazione.
Alcune sono raggruppate insieme e chiamate pattern.
Saremmo entusiasti se poteste dare una stella al nostro [repository di GitHub](https://github.com/AI-Native-Development/docs) o contribuire in qualsiasi modo, per quanto piccolo. Lavoriamo insieme per aprire la strada allo sviluppo nativo dell'AI!

<img align="right" src="../../top.png" title="AI Native Development Guide" width="30%">

Alcuni di questi pattern sono stati provati ed efficaci in ambienti individuali, ma altri sono basati su idee e non sono ancora stati testati per l'efficacia in ambienti di squadra.
Sentiti libero di lasciare commenti su GitHub Issues.
Aspettiamo con ansia varie discussioni e la condivisione di conoscenze sullo sviluppo AI-Native.

In questa introduzione, spiegheremo cosa è lo sviluppo AI-Native e cosa sono i pattern.
Se stai già praticando lo sviluppo AI-Native nella tua azienda e desideri contribuire alla stesura di questo documento, accogliamo con favore il tuo contributo!

Attualmente supportiamo le seguenti lingue: [Inglese 🇺🇸](https://ai-native-development.gitbook.io/docs/), [Tedesco 🇩🇪](https://ai-native-development.gitbook.io/docs/v/de/), [Spagnolo 🇪🇸](https://ai-native-development.gitbook.io/docs/v/es/), [Francese 🇫🇷](https://ai-native-development.gitbook.io/docs/v/fr/), [Italiano 🇮🇹](https://ai-native-development.gitbook.io/docs/v/it/), [Giapponese 🇯🇵](https://ai-native-development.gitbook.io/docs/v/ja/), [Portoghese 🇵🇹](https://ai-native-development.gitbook.io/docs/v/pt/), e [Cinese 🇨🇳](https://ai-native-development.gitbook.io/docs/v/zh/).

{% hint style="info" %}
Questo documento "Guida allo sviluppo AI-Native" non è ancora nella sua versione finale e potrebbe contenere link non funzionanti, errori di battitura e altri errori.
Il tuo aiuto nel migliorarlo è molto apprezzato.
Per favore, vedi come puoi contribuire a questo documento.
{% endhint %}

## Cosa è lo sviluppo AI-Native

Lo sviluppo AI-Native è un approccio per accelerare lo sviluppo del software incorporando un processo di sviluppo e una cultura basati sulla collaborazione con l'AI.
Nello sviluppo AI-Native, le tecnologie dell'AI come GitHub Copilot e ChatGPT vengono utilizzate per semplificare significativamente i processi tradizionali di sviluppo del software e creare soluzioni innovative.

* Completamento rapido del codice e suggerimenti: gli strumenti di AI generano e suggeriscono automaticamente frammenti di codice e funzioni pertinenti in base al codice inserito dagli sviluppatori.
Ciò consente agli sviluppatori di scrivere rapidamente codice e evitare errori comuni di codifica e bug.
* Consulenza in linguaggio naturale: gli strumenti di AI possono generare codice e suggerire soluzioni in risposta a domande ed istruzioni in linguaggio naturale.
Ciò consente agli sviluppatori di comunicare facilmente l'intento e la funzionalità del proprio programma.

D'altra parte, è necessario menzionare che lo stile di sviluppo cambia significativamente rispetto ai metodi tradizionali con l'introduzione dello sviluppo AI-Native.
Mentre molti vantaggi possono essere ottenuti utilizzando tecnologie dell'AI, gli sviluppatori e le squadre devono essere consapevoli dei seguenti punti per adattarsi a questi cambiamenti.

* Apprendimento e adattamento: per utilizzare efficacemente gli strument i di AI e le tecnologie, gli sviluppatori devono apprendere ed adattarsi al loro utilizzo e alle loro caratteristiche.
Questo include non solo la padronanza delle operazioni di base e delle migliori pratiche degli strumenti, ma anche la comprensione di come incorporarli nel processo di sviluppo e come collaborare con la squadra.
* Cambiamenti nello stile di comunicazione: nello sviluppo AI-Native, gli sviluppatori devono passare da una comunicazione centrata sul codice tradizionale a una comunicazione utilizzando il linguaggio naturale.
Ciò richiede agli sviluppatori di acquisire nuove competenze per comunicare chiaramente l'intento e i requisiti di un progetto.
La documentazione deve essere fornita in un formato che sia facile per l'AI da leggere, passando dai formati tradizionali come PowerPoint ed Excel a tipi di file come il Markdown.
* Ruoli e responsabilità all'interno della squadra: con l'introduzione dello sviluppo AI-Native, i ruoli e le responsabilità degli sviluppatori e delle squadre possono essere ridefiniti.
Ciò richiede agli sviluppatori di essere flessibili nelle loro aree di competenza e ruoli, e di rafforzare la collaborazione all'interno della squadra.
Gli sviluppatori dovranno concentrarsi maggiormente sulla risoluzione avanzata dei problemi e sulla decisione strategica, poiché i compiti diventano automatizzati attraverso l'uso degli strumenti di AI.

Incorporando l'AI in modo appropriato nello sviluppo, gli sviluppatori e le squadre possono migliorare la qualità e l'efficienza dei loro prodotti/progetti.
Speriamo che questa guida ti serva come punto di partenza per entrare nel mondo dello sviluppo AI-Native.

## Cosa sono i Pattern

I pattern sono un modo di descrivere soluzioni ripetibili ai problemi all'interno di un contesto specifico.
Nello sviluppo AI-Native, i pattern forniscono idee su come gli sviluppatori e le squadre possono utilizzare l'AI per raggiungere lo sviluppo rapido del prodotto.
I pattern sono divisi in sezioni principali come titolo, descrizione del problema, contesto, fattori influenzanti e soluzioni.
Il formato del pattern è utile per descrivere soluzioni provate ma può anche essere utilizzato durante la fase di brainstorming per nuove soluzioni per i pattern che non sono ancora stati stabiliti.
Ciò perché la struttura dei pattern fornisce un quadro per pensare ai problemi in modo strutturato.

Molti pattern sono ancora nei loro primi stadi in questa fase.
Ti incoraggiamo a provarli e a fornire un feedback.
Inoltre, se scopri un nuovo pattern, faccelo sapere tramite GitHub Issues.
Aspettiamo con ansia il tuo contributo!

## LICENZA

![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)

La Guida allo sviluppo AI-Native è concessa in licenza con [Attribuzione - Condividi allo stesso modo 4.0 Internazionale](http://creativecommons