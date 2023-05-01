# Documentazione AI-Native

L'utilizzo di tecnologie AI come GitHub Copilot può cambiare il lavoro degli ingegneri all'interno del team di sviluppo e alla fine può influire sull'architettura stessa.
In questo documento spiegheremo gli effetti potenziali dei metodi di sviluppo AI-Native.

## Il contesto è tutto

L'utilizzo di tecnologie AI come GitHub Copilot può essere applicato in vari campi, come l'ambiente di sviluppo o il processo di sviluppo.
I team di sviluppo devono ora essere più attenti al contesto per aumentare la velocità di sviluppo.
È importante prestare attenzione al contesto tecnico e aziendale all'interno del tuo programma.
Questo concetto non è nuovo, ma con l'avvento dell'AI, è importante considerare ancora una volta questi due contesti in relazione.
Questi contesti influenzeranno l'architettura e la carriera dell'ingegnere.

Inoltre, sia il contesto tecnico che quello aziendale possono essere suddivisi in aree ad alto e basso contesto.
Ad esempio, nella scrittura del codice, la creazione di processi come quelli che possono essere proposti da GitHub Copilot, come scrivere ripetutamente attività semplici che possono essere raggiunte premendo semplicemente il tasto tab, può essere sufficiente.
Al contrario, nelle aree che richiedono un alto livello di contesto, premere il tasto tab non porterà a nulla.
Queste aree richiedono esperienza e conoscenze specifiche in un determinato campo tecnologico e non possono essere acquisite facilmente.

### Contesto tecnico

Per comprendere il contesto tecnico, prendiamo in considerazione alcuni linguaggi di programmazione.
Ci sono linguaggi come Python in cui l'espressione per scrivere una cosa è abbastanza standardizzata, mentre altri come Ruby consentono di scrivere una cosa in molti modi diversi.
Inoltre, la portata è un'altra questione.
Ci sono linguaggi come BASIC in cui la portata globale è la norma, mentre altri hanno una portata molto più ristretta.
Ad esempio, il meccanismo di riferimento e prestito in Rust è un esempio tipico di contesto tecnico ad alto livello.
Inoltre, il contesto può essere ulteriormente stratificato a livello di framework.

### Contesto aziendale

Lo stesso vale per il dominio aziendale.
Prendiamo in considerazione il linguaggio SQL, utilizzato per i database.
L'AI è brava nelle attività ripetitive e nella creazione di espressioni standardizzate come quelle di SQL.
Se si definisce l'accesso al database per un'applicazione semplice, il contesto può essere ridotto.
Tuttavia, se si sta gestendo un grande database complicato, è difficile avere fiducia che il codice generato dall'AI non influenzi le altre attività.
In questo caso, è necessario comprendere l'architettura complessiva e avere una conoscenza adeguata della logica effettiva.
Lo stesso vale per i test: l'AI è brava a scrivere test basati su scenari specifici, ma è difficile che scriva scenari di test completi e complessi per un'applicazione che ha requisiti di autorizzazione complicati.

## Architettura AI-Native

Quanto contesto è presente nell'architettura della tua applicazione?
Se ci sono molti contesti nell'architettura, l'utilizzo dell'AI potrebbe rallentare la velocità di sviluppo.
Questo perché ci sono limiti al contesto che l'LLM può capire e non è possibile fornire contemporaneamente molte informazioni all'AI.
Questo è dovuto anche al limite di token che può essere fornito, ma anche al fatto che non tutte le informazioni possono essere presentate in un formato leggibile dall'AI.
L'AI può funzionare in modo illimitato se viene continuamente fornito un prompt, ma il tempo che l'essere umano può dedicare a fornire prompt all'AI è limitato.
In questo caso, l'essere umano diventa il collo di bottiglia nello sviluppo.
È importante quindi considerare di dividere il contesto della tua applicazione in unità semplici e testabili, in modo che l'AI possa scrivere il codice corretto anche con meno contesto.

La suddivisione dei servizi in piccole unità con relazioni poco strette è una buona idea.
Tuttavia, non sto dicendo che bisogna adottare i microservizi nel contesto di Kubernetes.
Puoi adottare qualsiasi progettazione che ritieni opportuna, inclusi SOA o la separazione a livello di libreria.
L'importante è dividere i componenti in unità semplici e testabili.
Più contesto ha l'applicazione, meno sarà facile ottenere il supporto dell'AI.

La dimensione appropriata del programma viene spesso discussa come se fosse una questione di fede e l'utilizzo dell'AI nello sviluppo è ancora in fase iniziale e non esiste una risposta precisa.
Tuttavia, se si vuole massimizzare la produttività degli ingegneri e far crescere il prodotto il più rapidamente possibile, è opportuno considerare un metodo di sviluppo e architettura basati su GitHub Copilot nel tuo team.

Ma è importante ricordare che l'architettura IT non dovrebbe essere pensata esclusivamente per massimizzare la produttività degli ingegneri.
L'ingegneria dovrebbe essere considerata un mezzo per raggiungere gli obiettivi finali.

Speriamo che tutti partecipino attivamente a questa discussione.

## Prospettive di carriera come ingegnere

Finora abbiamo esaminato la possibilità che l'IA possa portare cambiamenti nell'architettura e nella cultura dello sviluppo. È importante anche considerare la carriera dell'ingegnere. Ciò riguarda non solo l'ingegnere stesso, ma anche le persone che si trovano nella posizione di manager o di costruire l'organizzazione.

Alla fine, l'ingegnere deve decidere se vuole diventare un ingegnere con conoscenze ampie sui prodotti commerciali o un ingegnere tecnicamente avanzato. Tuttavia, il problema è che in entrambe queste aree ci sono aree a basso e alto contesto.

Ad esempio, quando si scrive il codice, potrebbe essere sufficiente premere il tasto Tab rispetto alla proposta di GitHub Copilot per scrivere processi come quelli in cui si ripete semplicemente un lavoro semplice o qualsiasi persona alla fine raggiunge il processo. Al contrario, le sezioni che richiedono contesti tecnici o commerciali specifici richiedono un alto contesto. Poiché queste aree richiedono esperienza e conoscenza di aree tecniche specifiche, non sono facilmente acquisibili. Se le conoscenze sono disponibili su Internet, è possibile recuperare il ritardo, ma se si tratta di conoscenze specifiche per un'organizzazione e inoltre non sono documentate o richiedono un costo molto elevato per l'acquisizione di informazioni, diventa difficile recuperare il ritardo.

Ciò non riguarda solo la scrittura del codice, ma l'IA tende a rafforzare le persone con conoscenze ed esperienze approfondite. Questo significa che i professionisti esperti potrebbero perdere il lavoro a favore dei nuovi arrivati. Se questo viene lasciato in sospeso, i nuovi arrivati ​​non potranno svolgere un lavoro importante nell'organizzazione e non potranno nemmeno crescere professionalmente. Le competenze degli esperti continuerebbero a crescere e diventerebbe difficile per l'organizzazione mantenere queste persone, mentre diventerebbe difficile mantenere i nuovi arrivati ​​che svolgono solo lavori noiosi che gli esperti non possono fare per questioni di tempo.

Quindi, quale è la soluzione? Una delle risposte è raccogliere le informazioni tecniche e commerciali del prodotto o dell'organizzazione come documenti di contesto e coltivare queste informazioni all'interno dell'organizzazione. Se molte persone partecipano alla creazione di questi documenti, si creerà un database di conoscenza dell'azienda. È ora il momento di promuovere la collaborazione interna simile all'open source.

## Checklist

- [ ] Quali contesti ci sono nel tuo progetto o prodotto? Cerca di organizzare il contesto.
- [ ] Questo contesto è riservato solo a poche persone o è condiviso dal team?
- [ ] Ci sono molti codici nel tuo progetto o prodotto che possono essere compresi dall'IA a basso contesto? Se ci sono molti codici a contesto elevato, come convertirli in codice facile da scr ivere per l'IA?
- [ ] Stai incoraggiando la collaborazione interna? Se no, pensa ad azioni per migliorare la comunicazione e la condivisione delle conoscenze tra i membri del team o tra i team.
- [ ] Hai discusso del percorso di carriera dell'ingegnere del tuo team nell'era dell'IA? Discuti se si desidera rafforzare le competenze tecniche o commerciali, o in altri settori.
