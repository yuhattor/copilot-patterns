# Desarrollo con AI

La adopción de tecnologías de AI como GitHub Copilot puede potencialmente impactar la arquitectura de proyectos a medida que cambia el trabajo de los ingenieros dentro de los equipos de desarrollo.
Este documento discute las posibles implicaciones que los métodos de desarrollo AI-nativos pueden tener.

## El Contexto es Tdo

Las tecnologías de AI, representadas por GitHub Copilot, pueden entrar en entornos y procesos de desarrollo de diversas maneras.
Los equipos de desarrollo necesitan estar más conscientes del contexto para lograr una mayor velocidad de desarrollo.
Una cosa a tener en cuenta es el contexto técnico y empresarial incluido en su programa.
Si bien este no es un tema nuevo y se ha discutido antes, vale la pena considerar estos dos contextos nuevamente a la luz del impulso que los desarrolladores están recibiendo ahora a través de la cooperación de AI.
Estos contextos afectarán la arquitectura y las carreras de los ingenieros.

También hay áreas de alto y bajo contexto para cada contexto.
Por ejemplo, en la codificación, simplemente presionar la tecla de tabulación para aceptar las sugerencias de GitHub Copilot puede ser suficiente para tareas repetitivas o procesos de escritura que finalmente llevarían al mismo resultado sin importar quién los escribiera.
Por otro lado, no se obtendrá nada simplemente presionando la tecla de tabulación en áreas donde se requiere un alto contexto.
Estas áreas requieren experiencia y conocimiento de dominios técnicos específicos, lo que no se puede adquirir fácilmente.

### Contexto Técnico

Para considerar el contexto técnico, pensemos en algunos lenguajes de programación.
Algunos lenguajes, como Python, tienen cierto grado de comunidad en cómo expresan las cosas, mientras que otros, como Ruby, permiten diversas expresiones para la misma tarea.
La amplitud del alcance también es un problema.
Existen lenguajes como BASIC donde el alcance global es el predeterminado, y muchos otros con alcances más estrechos.
El mecanismo de referencia y préstamo de Rust, por ejemplo, es un caso típico que implica un alto contexto técnico.
A nivel de marco, el contexto se puede apilar en múltiples capas.

### Contexto Empresarial

Lo mismo ocurre en el ámbito empresarial.
Consideremos SQL, un lenguaje de base de datos.
La IA es excelente en tareas simples y es adecuada para implementar expresiones estándar de SQL.
Si está definiendo el acceso a la base de datos para una implementación de aplicación simple, puede hacerlo con menos contexto.
Sin embargo, cuando se trata de una base de datos grande, compleja y entrelazada, es difícil estar seguro de que el código generado por IA no afectará a otros procesos.
Es posible que sea necesario comprender la arquitectura general y tener cierto conocimiento de la lógica real.
Lo mismo se aplica a las pruebas: la IA es buena escribiendo pruebas junto con escenarios dados, pero puede ser difícil crear escenarios de prueba exhaustivos.
La IA puede escribir fácilmente pruebas de API para una API REST con características CRUD simples, pero escribir pruebas perfectas para una aplicación con condiciones de autorización complejas podría ser un desafío para la IA.

## Arquitectura AI-Native

¿Cuánto contexto existe en la arquitectura de las funciones/aplicaciones que gestionas?
Si hay mucho contexto en la arquitectura, la velocidad de desarrollo utilizando la IA podría disminuir.
Esto se debe a que los LLM solo pueden entender una cantidad limitada de contexto, y no es posible proporcionar una gran cantidad de contexto a la IA al mismo tiempo.
Esto se debe en parte al límite superior de tokens que se pueden proporcionar, pero también porque los humanos generalmente no pueden proporcionar toda la información en una forma que sea legible para la IA.
En cierto sentido, la IA puede trabajar indefinidamente siempre que se proporcionen continuamente promt.
Por otro lado, los humanos tienen tiempo limitado para proporcionar promt a la IA.
En ese caso, el cuello de botella en el desarrollo se convierte en humano.
Por lo tanto, vale la pena considerar la reducción del contexto de las funciones o aplicaciones para que la IA pueda escribir el programa correcto incluso sin que los humanos proporcionen tanto contexto como sea posible.

Dividir los servicios en niveles más pequeños y hacerlos poco relacionados es una buena idea.
Sin embargo, lo que me refiero no necesariamente a usar microservicios en el contexto de Kubernetes.
Cualquier diseño que se te ocurra, incluida la separación del nivel de la biblioteca y SOA, está bien.
Lo importante es dividir los componentes en unidades simples y probables.
Cuanto más contexto tenga una aplicación, más difícil será obtener el soporte de la IA.

A veces hay guerras religiosas sobre el tamaño adecuado de los programas para manejar, y el desarrollo asistido por IA está recién comenzando, por lo que no hay una respuesta exacta.
Sin embargo, considerando maximizar la productividad de los ingenieros y hacer crecer los productos en el menor tiempo posible, podría ser una buena idea que su equipo considere los métodos de desarrollo y la arquitectura basados en GitHub Copilot.

Sin embargo, por otro lado, no se debe confundir la arquitectura de TI con el propósito de "maximizar la producción de ingenieros".
La ingeniería existe como un medio para lograr algo.

Espero que todos participen activamente en las discusiones en este campo.

## Perspectivas de carrera como ingeniero

Hasta ahora, se ha hablado del potencial de la IA para provocar cambios en la arquitectura y la cultura de desarrollo.
También es importante considerar la carrera de los ingenieros.
Este es un punto a considerar no solo para los propios ingenieros, sino también para los gerentes y aquellos en posiciones para construir organizaciones.

En última instancia, los ingenieros deben considerar si deben apuntar a ingenieros con una amplia gama de conocimientos del negocio y del producto o ingenieros altamente técnicos.
Sin embargo, el problema es que hay áreas de bajo y alto contexto en ambos.

Por ejemplo, en la codificación, simplemente presionar la tecla Tab para aceptar las sugerencias de GitHub Copilot puede ser suficiente para tareas repetitivas simples o para escribir procesos que finalmente llegarán al mismo resultado, independientemente de quién los escriba.
Por otro lado, las áreas especificadas en las secciones de contexto técnico y de negocio requieren un alto contexto.
Esta área es un campo donde se requiere experiencia y conocimiento de áreas tecnológicas específicas, por lo que no es algo que se pueda adquirir fácilmente.
Si es conocimiento disponible en Internet, aún hay una forma de ponerse al día, pero por otro lado, si es un área de conocimiento cerrado en una organización específica, y no está documentado o el costo de obtener información es extremadamente alto, es difícil ponerse al día.

Esto no se limita a la codificación, pero la IA tiende a fortalecer a los humanos con conocimientos y experiencia ricos.
Esto significa que los miembros senior perderán los trabajos de los recién llegados.
Si no se controla, los recién llegados no podrán hacer un trabajo importante en la organización y no podrán esperar un crecimiento de habilidades.
Las habilidades senior aumentarán aún más, lo que hará que sea difícil para la organización mantenerlas, y también será difícil mantener a los recién llegados que solo están haciendo un trabajo aburrido que los seniors no pueden hacer debido a limitaciones de tiempo.

Entonces, ¿qué se debe hacer? Una respuesta es compilar información técnica y empresarial en productos y organizaciones en documentos que contengan contexto y fomentarlos internamente.
A medida que más personas participan en la creación de estas documentaciones y se produce la co-creación, se forma una base de conocimiento para la empresa.
Ahora es el momento de crear una atmósfera de colaboración interna similar al código abierto.

## Lista de verificación

- [ ] ¿Qué contexto tiene tu proyecto o producto? Trata de organizar el contexto.
- [ ] ¿El contexto es exclusivo de algunas personas o se comparte dentro del equipo?
- [ ] ¿En tu proyecto o producto hay mucho código que la IA pueda entender incluso con poco contexto? Si hay mucho código de alto contexto, ¿cómo planeas convertirlo en código fácilmente interpretable por la IA?
- [ ] ¿Estás promoviendo la colaboración interna? Si no, considera acciones para mejorar la comunicación y el intercambio de conocimientos dentro y entre equipos.
- [ ] ¿Has discutido las trayectorias profesionales de los ingenieros de tu equipo en la era de la IA? Habla sobre si quieren fortalecer sus áreas técnicas y de negocios.
