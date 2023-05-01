# Documentación nativa de AI

La utilización de tecnologías de inteligencia artificial (IA), como GitHub Copilot, puede afectar a la arquitectura y, en última instancia, cambiar el trabajo de los ingenieros en el equipo de desarrollo.
En este documento se describe el impacto potencial que puede tener el enfoque nativo de IA en el desarrollo.

## El contexto lo es todo

Cuando se habla de tecnologías de IA, como las que representa GitHub Copilot, hay muchos campos a considerar en cuanto al entorno y al proceso de desarrollo.
Para lograr una mayor velocidad en el desarrollo, los equipos de desarrollo deben ser más conscientes del contexto.
Algo a tener en cuenta es qué contexto técnico y empresarial está presente en el programa.
Esto no es un tema nuevo, ya que se ha dicho desde hace mucho tiempo, pero con la aparición de la IA, es importante considerar nuevamente estos dos contextos al trabajar juntos.
Estos contextos pueden afectar la arquitectura y la carrera del ingeniero.

Además, cada contexto tiene áreas de alto y bajo nivel de complejidad.
En el caso de la programación, puede que escribir un código simple que realice una tarea que siempre llegue al mismo resultado con solo presionar la tecla Tab según lo propuesto por GitHub Copilot sea suficiente.
Pero en las áreas que requieren un mayor nivel de complejidad, presionar la tecla Tab no generará nada.
Estas áreas son aquellas que requieren experiencia y conocimiento en áreas técnicas específicas, por lo que no se pueden aprender fácilmente.

### Contexto técnico

Para considerar el contexto técnico, pensemos en varios lenguajes de programación.
Algunos lenguajes, como Python, tienen una forma común de expresar una sola cosa, mientras que otros, como Ruby, tienen una variedad de formas de expresar la misma cosa.
Además, el alcance también es un problema.
Hay lenguajes como BASIC que tienen un alcance global básico, mientras que otros tienen un alcance más limitado.
El mecanismo de referencia y préstamo de Rust es un ejemplo típico que incluye un contexto técnico de alto nivel.
Además, en el nivel del marco de trabajo, el contexto se puede superponer en varias capas.

### Contexto empresarial

Lo mismo ocurre con el dominio empresarial.
Tomemos el lenguaje de base de datos SQL como ejemplo.
La IA es buena en trabajos simples, y es apta para implementaciones que simplemente definen el acceso a la base de datos para una aplicación simple.
Sin embargo, si se trata de una base de datos compleja y enorme, puede ser difícil confiar en que el código generado por la IA no afecte a otros procesos.
Es posible que se necesite comprender la arquitectura general y tener cierto conocimiento sobre la lógica real.
Lo mismo ocurre con las pruebas; la IA es buena en escribir pruebas según los escenarios proporcionados, pero es difícil para ella considerar los escenarios de prueba exhaustivos.
Es fácil escribir pruebas de API para funciones CRUD simples, pero es difícil para la IA escribir pruebas para aplicaciones más complejas que tienen condiciones de autorización complicadas, por ejemplo.

## Arquitectura nativa de AI

¿Cuál es el contexto presente en la arquitectura de las funciones/aplicaciones que administra?
Si hay muchos contextos involucrados en la arquitectura, es posible que la velocidad de desarrollo con la ayuda de la IA disminuya.
Esto se debe a que hay un límite en el contexto que el modelo de lenguaje natural puede comprender y, en general, los humanos no pueden proporcionar toda la información en un formato que la IA pueda leer.
Aunque parte de la razón es que hay un límite en el número de tokens que se pueden proporcionar, también se debe al hecho de que los humanos no pueden proporcionar toda la información en un formato legible para la IA.
En cierto sentido, la IA puede funcionar indefinidamente siempre que se le proporcione una serie continua de entradas, pero el tiempo que los humanos pueden dar indicaciones a la IA es limitado.
Por lo tanto, en lugar de proporcionar a la IA un amplio contexto, puede ser mejor considerar dividir los servicios en componentes más simples y fáciles de probar.

Es una buena idea dividir las funciones de los servicios en unidades más pequeñas y con relaciones poco frecuentes.
Sin embargo, lo que estoy sugiriendo no es hacer microservicios en el contexto de Kubernetes.
No importa qué diseño se considere, que incluya la separación en SOA o nivel de biblioteca.
Lo importante es dividir los componentes en unidades simples y fáciles de probar.
Cuanto más contexto tenga la aplicación, menos será el apoyo de la IA.

El tamaño apropiado de los programas es un tema que a veces provoca discusiones apasionadas, y todavía no hay una respuesta precisa para el uso de la IA en el desarrollo.
Sin embargo, si se desea maximizar la productividad del ingeniero y hacer crecer el producto en el menor tiempo posible, es recomendable considerar un enfoque de desarrollo y arquitectura basado en GitHub Copilot.

Sin embargo, es importante tener en cuenta que la arquitectura de TI no debería ser diseñada con el único propósito de maximizar la productividad del ingeniero.
La ingeniería siempre debe considerarse como un medio para lograr un objetivo final.

Espero que participen activamente en las discusiones en este campo.

## Perspectivas de carrera como ingeniero

Hasta ahora hemos hablado sobre la posibilidad de que la inteligencia artificial cambie la arquitectura y la cultura de desarrollo. Es importante también considerar la carrera en ingeniería, no solo para los ingenieros en sí, sino también para los gerentes y personas en posiciones de construcción de organizaciones.

En última instancia, los ingenieros deben considerar si desean convertirse en ingenieros con conocimientos amplios de productos comerciales o en ingenieros técnicamente avanzados. Sin embargo, el problema es que tanto en estas dos áreas existen dominios de bajo contexto y alto contexto.

Por ejemplo, en la codificación, puede ser suficiente simplemente presionar la tecla TAB para aceptar las sugerencias de GitHub Copilot para escribir procesos que son simples y se repiten en el trabajo, y que finalmente llegan a la misma solución, independientemente de quién los escriba.
Por otro lado, las áreas que requieren especificaciones de contexto técnico o de contexto comercial son áreas que requieren un alto contexto. Estas áreas requieren experiencia y conocimientos específicos en áreas tecnológicas determinadas, por lo que no son fáciles de adquirir. Si el conocimiento se encuentra en línea, todavía se puede poner al día, pero si se trata de un área de conocimiento específica cerrada en una organización, que además no está documentada o cuesta mucho obtener información, será difícil ponerse al día.

Esto no se limita a la codificación, pero la IA tiende a fortalecer a las personas con experiencia y conocimientos. Esto significa que los expertos pueden perder el trabajo de los recién llegados. Si se deja así, los recién llegados no podrán hacer trabajos importantes en la organización ni mejorar sus habilidades. Se espera que las habilidades de los expertos aumenten aún más y que la organización tenga dificultades para mantenerlos, y también será difícil mantener a los recién llegados haciendo trabajos aburridos y limitados en el tiempo que los expertos no pueden hacer.

Entonces, ¿qué hacer? Una de las respuestas es recopilar información técnica y comercial sobre el producto y la organización en forma de documentos con contexto y criarlos internamente. Si muchas personas participan en la creación de esta documentación y se produce una colaboración, la base de datos de conocimientos corporativos se desarrollará. Ahora es el momento de fomentar la colaboración interna similar a la de código abierto.

## Lista de verificación

- [ ] ¿Qué contexto hay en su proyecto o producto? Ordenemos el contexto.
- [ ] ¿Es ese contexto exclusivo para algunas personas? ¿Se comparte en equipo?
- [ ] ¿Hay mucho código en su proyecto o producto que la IA puede entender incluso en contextos de baja complejidad? ¿Qué pasa si hay mucho código de alto contexto? ¿Cómo lo convierte en código fácil de escribir para la IA?
- [ ] ¿Está fomentando la colaboración interna? Si no es así, pensemos en acciones para mejorar la comunicación y el intercambio de conocimientos dentro y entre los equipos.
- [ ] ¿Se ha discutido el camino de la carrera de los ingenieros de su equipo en la era de la IA? Discutamos si se desea fortalecer áreas tecnológicas, comerciales, etc.
- [ ] ¿Está considerando el impacto de la IA en las carreras de los ingenieros? ¿Cómo puede preparar a los ingenieros para trabajar con la IA y aprovechar al máximo su potencial?
