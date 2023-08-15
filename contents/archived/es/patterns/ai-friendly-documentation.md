# Documentación amigable con la IA

## Descripción

Al crear documentación en un formato comprensible para la IA, no solo los ingenieros que escriben código, sino también todo el equipo, pueden mejorar la productividad en general. Un ejemplo de esto es escribir la definición de una tabla de base de datos en Markdown y gestionarla como documentación en git, en lugar de usar PowerPoint o Excel.

## Problema

En el desarrollo de productos se necesitan varios tipos de documentación, como especificaciones de requisitos, documentos de diseño, diagramas de arquitectura, especificaciones de configuración de infraestructura, documentos de casos de prueba, etc. Por lo general, se prefieren formatos como PowerPoint o Excel, pero la IA no puede leer esos documentos. Además, no es una buena práctica gestionar archivos binarios en un repositorio Git.

## Historia

Su equipo ha implementado GitHub Copilot for Business. Los ingenieros están encantados de ahorrar tiempo en su trabajo y sienten que el equipo ha crecido en tamaño gracias a la ayuda de la IA. Sin embargo, la IA solo puede hacer lo que se le indica y no puede entender el contexto que los ingenieros tienen. Por lo tanto, los ingenieros necesitan escribir grandes cantidades de lenguaje natural para dar contexto a la IA. Como resultado, ha habido un aumento en la cantidad de trabajo que implica copiar y pegar el texto proporcionado por el PM, convertir los complejos formatos de PowerPoint y Excel que los superiores han creado en formatos legibles por la IA, como Markdown o CSV.

"¡Sería mejor si todo estuviera escrito en CSV o Markdown desde el principio!"

## Contexto

En muchos proyectos, la documentación se gestiona en formatos como PowerPoint o Excel. Las personas que no son ingenieros están comunicándose fuera de GitHub, y las decisiones finales no se están guardando en el repositorio. La documentación se estructura de manera que la IA pueda leerla, pero no está gestionada centralmente.

## Solución

El equipo debe esforzarse por crear documentos de texto, como Markdown o CSV. Los documentos que contienen el contexto necesario para que los ingenieros y la IA los utilicen deben guardarse en un repositorio de Git. Este repositorio debe ser fácil de llamar desde el espacio de trabajo utilizando cosas como Git Submodule. Si es necesario, el texto de un archivo puede copiarse en el área de comentarios y proporcionarse como indicación a la IA.

## Ejemplos conocidos

- Prepare la definición de una tabla en formato CSV o Markdown y asóciela con un archivo de migración o una interfaz.
- Convierta las definiciones de infraestructura resumidas en lenguaje natural en archivos de configuración de infraestructura como código, como Terraform.
- Convierta los documentos de casos de prueba en archivos de prueba. Esto funciona de manera más efectiva para los documentos con patrones claros, como las pruebas de API. Esto hace que el desarrollo dirigido por pruebas sea más fácil.

## Contexto resultante

- Los ingenieros pueden crear más código con menos esfuerzo, lo que conduce a la reducción de horas de trabajo.
- Los dueños y gerentes del proyecto pueden obtener resultados de los ingenieros más rápidamente.
- Los miembros que no escriben código regularmente pueden acostumbrarse a proporcionar el contexto que los ingenieros necesitan y que se debe proporcionar a la IA para el desarrollo adecuado, mediante la colaboración con GitHub. 
- Debido a que los cambios en la documentación quedan registrados, es posible rastrear todo el proceso de decisión, incluyendo quién hizo qué cambio y cuándo, no solo en el código, sino en todo el proyecto.
- No habrá discrepancias entre la documentación y la implementación.

## Notas

- Actualmente, GitHub Copilot tiene limitaciones en los tipos de archivo que puede leer. Si está escribiendo código en Python, el código en Python en la pestaña abierta se leerá y se pasará al cuadro de diálogo. Por lo tanto, para utilizar la documentación amigable con la IA, copie el texto necesario de la documentación en Markdown y péguelo en el cuadro de comentarios del archivo `.py`.
- No todos los documentos son adecuados para ser guardados en el repositorio. Si se equivoca en la elección de qué documentos almacenar, puede llenar el repositorio con documentos innecesarios, lo que reduce el rendimiento de la búsqueda. Intente escribir en Markdown los documentos que están más cerca de la implementación.
- Hay un límite en el número de tokens que se pueden pasar a la IA. Trate de resumir cada sección de un documento y no hacer que dependan demasiado del texto que los rodea.
