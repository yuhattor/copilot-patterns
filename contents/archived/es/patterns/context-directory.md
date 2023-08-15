# Directorio de contexto

Alias: Directorio de fragmentos de inclusión de fragmentos de código

## Descripción

El directorio de contexto en el repositorio recopila el contexto de todo el código base para facilitar a GitHub Copilot el paso de un contexto preciso durante el desarrollo.

## Problema

* Sugerencias inexactas
  GitHub Copilot puede realizar sugerencias inexactas al no poder obtener el contexto completo del código base. Esto puede disminuir la calidad del código o aumentar el tiempo que los desarrolladores dedican a realizar ajustes y correcciones.
* Disminución de la eficiencia
  Si los desarrolladores no mantienen abiertos los archivos relacionados en pestañas adyacentes, GitHub Copilot no puede obtener información de estos archivos. Como resultado, las sugerencias pueden ser inexactas y los desarrolladores tienen que buscar y consultar manualmente los archivos relacionados mientras escriben código. Esto puede disminuir la productividad de los desarrolladores.
* Pérdida de coherencia en el código
  Si no se puede obtener el contexto completo del código base, las sugerencias de código que GitHub Copilot propone pueden no ser coherentes con el código existente. Esto puede afectar la legibilidad y mantenibilidad del código, lo que puede disminuir la velocidad de desarrollo del equipo.

## Historia

Un día, un ingeniero del equipo de un proyecto decidió utilizar GitHub Copilot para desarrollar una nueva función. Tenía un gran interés en GitHub Copilot y pensaba que le ayudaría a escribir código rápidamente.

Sin embargo, a medida que avanzaba el desarrollo, notó que las sugerencias de código que GitHub Copilot ofrecía a veces eran inexactas. A pesar de esto, continuó corrigiéndolas manualmente y avanzando en el desarrollo, pero con el tiempo se cansó de ese trabajo. Además, otros miembros del equipo también señalaron que las sugerencias de código propuestas por GitHub Copilot carecían de coherencia.

Ella se preguntó por qué GitHub Copilot no hacía sugerencias precisas y comenzó a investigar. Descubrió que la razón por la que era parte de las sugerencias inexactas era que no había mantenido abiertos los archivos relacionados correctamente. Por otro lado, mantener todos los archivos abiertos no es práctico y, además, GitHub Copilot solo envía datos de pestañas adyacentes como tokens debido al modelo Codex que se utiliza en GitHub Copilot, que tiene un límite en la cantidad de tokens que se pueden pasar.

Entonces decidió implementar el patrón de directorio de contexto. Esperaba que mantener abiertos los archivos relacionados permitiera que GitHub Copilot hiciera sugerencias más precisas.

## Contexto

GitHub Copilot, un producto representativo de las herramientas de asistencia de codificación de IA, actualmente ofrece sugerencias en función de la información del archivo que está actualmente abierto o de los archivos con la misma extensión que están abiertos en pestañas.

La cantidad de tokens que se pueden pasar al modelo Codex utilizado en GitHub Copilot es limitada. Por lo tanto, las extensiones de GitHub Copilot, como VS Code, no envían toda la información de los archivos abiertos como información de referencia al servidor de GitHub Copilot, sino que priorizan el envío de archivos con alta similitud en información. La inclusión de fragmentos de código se llama "inclusión de fragmentos de código". Por lo tanto, es necesario mantener abiertas en pestañas adyacentes solo un número adecuado de archivos relacionados.

## Solución

1. Cree un directorio de contexto.
Cree un directorio donde pueda almacenar los archivos que desea que GitHub Copilot recuerde como contexto o reglas auxiliares.
2. Cierre los archivos que no están relacionados con lo que está desarrollando actualmente.
3. Mantenga abiertos los archivos relacionados con lo que está desarrollando actualmente en pestañas de VSCode.
Actualmente, GitHub Copilot no puede obtener todo el contexto del código base, pero puede leer el archivo actual y los archivos abiertos en el editor. Mantener abiertas las pestañas de archivos relacionados permitirá que GitHub Copilot haga sugerencias más precisas.

## Contexto resultante

El uso del directorio de contexto permitirá que GitHub Copilot ofrezca sugerencias más precisas. Mantener abiertas las pestañas de los archivos relacionados permitirá obtener una mejor ayuda en la escritura de código.

## Nota

* Actualmente, los archivos que GitHub Copilot lee son limitados. Si está escribiendo en Python, es deseable que los archivos de fragmentos y los archivos de referencia sean también código de Python.
* Si es necesario, puede agregar estos directorios a .gitignore para que no se envíe su contenido.
* Además, puede utilizar Git Submodule para separar el directorio de contexto como un directorio diferente.
