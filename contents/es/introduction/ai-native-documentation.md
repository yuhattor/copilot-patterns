# Documentación AI Native: Legibilidad de Documentos de AI

Actualmente, hay mucho revuelo en torno a una herramienta de desarrollo llamada GitHub Copilot, que cuenta con funcionalidad asistida por IA.
Existe la idea equivocada de que esta herramienta es solo para ingenieros, pero esto es parcialmente verdadero y parcialmente incorrecto.
De hecho, GitHub Copilot tiene una capacidad increíble para transformar la forma en que trabajan los ingenieros.
Sin embargo, a medida que cambian los métodos de trabajo de los ingenieros, las organizaciones también deben adaptarse.
Si está en una posición de PM o PO, este es un tema importante para usted también, ya que se espera que los ingenieros de su equipo funcionen al máximo rendimiento, implementando sus requisitos definidos lo más rápido posible.
En el futuro, incluso si no es un ingeniero, deberá crear documentación **legible por AI** para permitir que los ingenieros de su equipo colaboren con AI.

## Cultura de Documentación y Desarrollo AI Native

En los últimos años, la tecnología de IA ha avanzado rápidamente, con modelos como LLM (Large Language Model) ganando atención.
GitHub, una plataforma de desarrollo de código abierto, también se ha aventurado en el campo del desarrollo de IA.
Un ejemplo principal de esto es "GitHub Copilot".
Curiosamente, el desarrollo asistido por IA y el desarrollo de código abierto comparten un terreno común en términos de colaboración.
Específicamente, ambos métodos implican trabajar con formatos basados en documentos como Markdown.
Los formatos como Markdown están diseñados para representar información estructurada y son más fáciles de analizar para la IA que los archivos de PowerPoint o Excel.
Como resultado, contribuyen a la mejora de la calidad del código generado por IA.

La IA prefiere archivos CSV simples en lugar de complejas hojas de cálculo de Excel llenas de metadatos.
Supongamos que, como PM, enumera los requisitos del cliente y recopila la información necesaria para una base de datos.
Si los requisitos están escritos en un archivo CSV o resumidos en Markdown, los ingenieros pueden convertirlos fácilmente en código.
Sin embargo, si compila la información en un documento de Excel adaptado a sus preferencias, los ingenieros deben copiar, formatear y luego convertirlo en código.
¿Cuál enfoque es mejor?

Además, en el desarrollo de código abierto, la calidad de la documentación puede estar directamente relacionada con el éxito de un proyecto.
Los proyectos de código abierto están abiertos a cualquiera, y una documentación adecuadamente mantenida permite que los nuevos desarrolladores se unan más fácilmente.
Por lo tanto, la documentación es muy valorada en el desarrollo de código abierto.
Del mismo modo, en el desarrollo de IA, una cultura de documentación bien establecida puede llevar a un desarrollo más eficiente y de mayor calidad.
Incluso si no es un ingeniero, su lenguaje natural escrito en Markdown puede contribuir significativamente a la salida final, que es el código.
Esto podría ser código que representa la lógica empresarial, definiciones de tablas o incluso escenarios de prueba.
¿Está su equipo de desarrollo preparado para incluir AI? ¿Se han preparado documentos legibles por AI? Si la respuesta es no, debe comenzar a crear un equipo de desarrollo que esté cómodo para que AI participe.

## Desarrollo AI Native y Estrategia InnerSource

Hemos estado discutiendo el desarrollo de código abierto, pero también existe un concepto similar llamado InnerSource.
InnerSource es un enfoque que adopta las mejores prácticas del desarrollo de software de código abierto dentro de organizaciones que desarrollan software no de código abierto o propietario.
Su objetivo es promover la colaboración en toda la organización y romper los silos organizativos.

InnerSource es cada vez más importante para las empresas para evitar reinventar la rueda, optimizar el desarrollo para reducir costos y crear nuevo valor a través de la colaboración.

Como se menciona en la página de desarrollo AI Native, la IA tiende a mejorar a los humanos experimentados.
Las personas mayores o experimentadas dentro de una organización que entienden la arquitectura se mejoran, mientras que a otros se les asignan tareas más simples.
Sin embargo, dado que la IA se entrena principalmente con conocimientos de internet, no puede acceder a dominios propietarios, conocimientos cerrados dentro de las organizaciones o información no publicada.
Por lo tanto, si esta información no está documentada o compartida adecuadamente dentro de la organización, se plantea un problema.
Este problema significa que no solo los ingenieros no pueden acceder a la información, sino que la IA, como GitHub Copilot, tampoco puede acceder a ella.

El conocimiento que no se puede obtener de internet es actualmente cada vez más importante y una competencia central de las empresas.
Hay una cita de un libro introductorio de InnerSource ["Getting Started with InnerSource"](https://innersourcecommons.org/learn/books/getting-started-with-innersource/) de O'Reilly que dice:

> InnerSource difiere del código abierto clásico al permanecer dentro de la vista y el control de una sola organización. La "apertura" del proyecto se extiende a través de muchos equipos dentro de la organización. Esto permite que la organización incorpore secretos comerciales diferenciados en el código sin temor a que se revelen a terceros, mientras se beneficia de la creatividad y las diversas perspectivas aportadas por las personas de toda la organización.

Muchas empresas se enfrentan a la elección de colaborar con IA o ser reemplazadas por IA.
Es fundamental consolidar la información interna que es la fuente de la ventaja competitiva de una organización y hacer que la IA la utilice.
Para lograr esto, la documentación con legibilidad de AI es indispensable.

En cuanto a InnerSource, ya existe una comunidad madura donde se comparten métodos para realizar la co-creación dentro de las organizaciones y crear documentación.
Acceda a esta comunidad y aproveche las iniciativas de InnerSource.
Al hacerlo, puede utilizar eficazmente el conocimiento y la información internos y aprovechar al máximo la colaboración con AI.

### Referencias de InnerSource

- [InnerSource Commons](https://innersourcecommons.org/): Página de la Fundación InnerSource Commons
- [InnerSource Patterns](https://patterns.innersourcecommons.org/): Colección de las mejores prácticas de InnerSource
- [Getting Started with InnerSource](https://innersourcecommons.org/learn/books/getting-started-with-innersource/): Libro introductorio de InnerSource de O'Reilly
- [Understanding the InnerSource Checklist](https://innersourcecommons.org/learn/books/understanding-the-innersource-checklist/): Guía práctica de InnerSource de O'Reilly

## Creación de documentación rica en contexto

A medida que el desarrollo de código abierto madura, emerge la colaboración entre países y zonas horarias.
Sin embargo, la distancia geográfica y las diferencias horarias a veces pueden dificultar la comunicación sincrónica.
Por ejemplo, mientras en Nueva York es de día, en Tokio es de noche, y no es deseable molestar a los colaboradores japoneses durante la noche o interferir con su tiempo en familia.
Por lo tanto, generalmente se prefiere la documentación basada en documentos escritos.
Esto podría ser algo como RFC o documentos de diseño, o comentarios escritos en problemas de GitHub.
Los documentos formados por comentarios en problemas y similares también se llaman documentación pasiva.
Estas son también formas de documentación.

Hay un pasaje en la lista de verificación de InnerSource publicada por O'Reilly que dice:

> La documentación pasiva es el registro de la documentación que creamos todos los días mientras nos comunicamos abiertamente. Es una excelente manera de sacar el conocimiento tribal de los silos y ponerlo en un formato que sea archivable y localizable. Como una ventaja adicional, generalmente se mantiene con el proyecto o el código que documenta, por lo tanto, está en una ubicación fácil de encontrar y relevante para el contexto.

Lo importante aquí es ponerlo adecuadamente en palabras, incluyendo el contexto.
Es difícil transmitir la comunicación no verbal, los matices y la atmósfera que se comunican a través de conversaciones asincrónicas a través de Zoom o cara a cara entre zonas horarias.

Considere el desarrollo con IA.
Por ejemplo, ¿participará GitHub Copilot en reuniones de Zoom? ¿Estará en la sala del equipo diciendo: "Hola, soy GitHub Copilot, hagamos una reunión rápida de verificación"? La respuesta es no.
Todo el contexto debe ser transmitido a la IA por escrito.
Esto también es necesario al crear documentación apropiada para la comunicación asincrónica, como en el desarrollo de código abierto.

Por supuesto, hay diferencias en la granularidad de la documentación entre el desarrollo de código abierto y el desarrollo asistido por IA.
Escribir "quiero arreglar este error" en los problemas de GitHub podría provocar que alguien piense en una solución, pero la IA no puede llegar tan lejos.
Sin embargo, definitivamente hay áreas donde la IA sobresale.
Si desea expresar la arquitectura en la nube como infraestructura como código, es mejor escribirlo en Mermaid o expresarlo en lenguaje natural en lugar de dibujarlo en PowerPoint.

El punto aquí no es que toda la comunicación deba ser documentada.
Usted y su equipo deben considerar qué nivel de documentación dejar, cómo y dónde dejarlo.

## La inteligencia artificial coordina el conocimiento organizacional

Con características como GitHub Copilot for Docs incluido en GitHub Copilot X, la IA puede crear la documentación perfecta para ti.
Los documentos que escribas también pueden convertirse en materiales de incorporación para la próxima persona.

En el pasado, recopilar información y crear materiales de incorporación para nuevos ingenieros era una tarea común, pero en el futuro, es probable que la IA asuma ese papel.
Puedes incrustar todo el conocimiento que poseas en documentos como la única fuente confiable de información.

Este enfoque también se puede ver explícitamente en la documentación de [Atlassian](https://www.atlassian.com/ja/work-management/knowledge-sharing/documentation/importance-of-documentation).
Leer su documentación teniendo en cuenta el desarrollo nativo de la IA puede conducir a nuevos descubrimientos.
Los documentos que escribas parecerán tener una personalidad a través de la IA.
Sin embargo, esto requiere suficiente documentación, como se mencionó anteriormente.

## La distancia entre el lenguaje natural y la implementación se acerca

Como habrás notado hasta ahora, la distancia entre el lenguaje natural y la implementación se está acortando mucho.
Como se mencionó anteriormente, desde una perspectiva educativa, si se continúa escribiendo indicaciones y código en un solo lugar, podría ser posible crear documentación en un solo archivo.
Este tipo de cambio es fascinante.

## Lista de verificación

- [ ] ¿Tiene tu equipo actualmente una cultura de documentación? Si es así, ¿cómo es? Si no es así, ¿qué lo impide?
- [ ] Considera qué tipo de documentación se necesita para que tu equipo colabore con la IA.
- [ ] ¿Hay una cultura de código abierto o de fuente interna en tu equipo?
- [ ] Comienza creando una cultura de documentación dentro de tu alcance.
¿En qué áreas puedes comenzar a escribir documentación en Markdown? Piénsalo.
