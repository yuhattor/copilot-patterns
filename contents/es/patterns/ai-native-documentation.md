# Documentación Nativa de IA

## Descripción

Crear documentación en un formato que pueda ser entendido por la IA, no solo por los ingenieros que escriben código, puede mejorar la productividad general del equipo.
Por ejemplo, en lugar de escribir definiciones de tablas de bases de datos en PowerPoint, se pueden escribir en Markdown y administrar en Git como documentación.

## Problema

Se necesitan varios documentos para el desarrollo de productos, como definiciones de requisitos, documentos de diseño, diagramas de resumen de arquitectura, especificaciones de configuración de infraestructura y documentos de casos de prueba.
Generalmente, se prefieren formatos como PowerPoint y Excel, pero la IA no puede leer esos documentos.
Además, administrar archivos binarios en un repositorio Git no es una buena práctica.

## Historia

Su equipo ha introducido GitHub Copilot para Empresas.
Los ingenieros están contentos de que se esté reduciendo su tiempo de trabajo.
El equipo siente que ha duplicado su tamaño con la ayuda de la IA.
Sin embargo, el problema es que la IA solo puede hacer lo que el ingeniero le indica que haga.
Además, como la IA no entiende el contexto que posee el ingeniero, este debe ingresar una gran cantidad de lenguaje natural para transmitir el contexto a la IA.
Como resultado, ha habido un aumento en tareas como copiar y pegar texto proporcionado por el PM o convertir diapositivas de PowerPoint y archivos de Excel complejos en formato Markdown o CSV que la IA pueda leer.

"¡Sería genial si estuvieran escritos en CSV o Markdown desde el principio!"

## Contexto

En muchos proyectos, la documentación se administra en formatos como PowerPoint y Excel.
Las personas que no son ingenieros se comunican en lugares que no son GitHub y la decisión final no se guarda en el repositorio.
Los documentos se resumen en una forma que es fácil para que la IA los lea, pero no se administran de manera centralizada.

## Solución

El equipo se esfuerza por crear documentos basados en texto como Markdown y CSV.
Los documentos que finalmente deben entregarse a los ingenieros y la IA que contienen el contexto se guardan en un repositorio de Git.
Los ingenieros proporcionan contexto a la IA llamando a ese repositorio en el espacio de trabajo actual utilizando mecanismos como git submodule y abriendo el archivo con una pestaña.

## Ejemplo Conocido

* Prepare archivos de definición de tabla en formato CSV o Markdown y asícielos a los archivos de migración o creación de interfaz.
* Convierta las definiciones de infraestructura resumidas en lenguaje natural a archivos de configuración para la infraestructura como código, como Terraform.
* Convierta documentos de casos de prueba en archivos de prueba.
Esto es más efectivo para aquellos que tienen ciertos patrones como pruebas de API.
Esto hace que el desarrollo impulsado por pruebas sea más fácil.

## Contexto Resultante

* Los ingenieros pueden crear más código con menos esfuerzo, lo que se traduce en una reducción de horas-hombre.
* Los propietarios del proyecto y los gerentes de producto pueden recibir entregables de los ingenieros más rápido.
* Incluso los miembros que normalmente no escriben código pueden acostumbrarse a determinar el contexto requerido por los ingenieros y la IA colaborando mediante GitHub, lo que permite un desarrollo adecuado con IA.
* Como se registran los historiales de cambios en los documentos, se vuelve posible realizar un seguimiento de todo lo que no sea código, como quién hizo qué cambios en qué momento y cuándo se tomaron decisiones.
* Se elimina la brecha entre documentos y su implementación.

## Nota

* Actualmente, los archivos que GitHub Copilot puede leer son limitados.
Es recomendable que si estás escribiendo en Python, sea código Python.
Por lo tanto, es una buena idea copiar un archivo Markdown y convertirlo en un documento de Python con comentarios y usarlo como referencia.
* Este patrón no es efectivo para todos los documentos.
Si se comete un error al decidir la estructura del repositorio o qué documentos almacenar, puede generarse un gran número de documentos innecesarios en el repositorio, y el rendimiento de búsqueda puede empeorar.
* El número de tokens que se pueden pasar a la IA es limitado.
Trata de mantener cada sección de cada oración concisa para que no tenga demasiadas dependencias con las oraciones circundantes.
