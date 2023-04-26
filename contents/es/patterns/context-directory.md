# Directorio de Contexto

También conocido como: Inclusión de fragmentos de código

## Descripción

Se crea una carpeta de contexto en el repositorio, donde se guarda todo el contexto del código, para permitir que GitHub Copilot ofrezca sugerencias precisas.

## Problema

* Sugerencias inexactas:
GitHub Copilot realiza sugerencias basadas en la información del archivo abierto y otros archivos relacionados. Si GitHub Copilot no puede obtener el contexto de todo el código, las sugerencias pueden ser inexactas. Esto puede llevar a una menor calidad de código y aumentar el tiempo que los desarrolladores necesitan para hacer correcciones y ajustes.
* Disminución de la eficiencia:
Si los desarrolladores no mantienen los archivos relacionados abiertos en pestañas adyacentes, GitHub Copilot no puede obtener información de esos archivos. Como resultado, las sugerencias pueden ser inexactas y los desarrolladores pueden tener que buscar y hacer referencia manualmente a los archivos relacionados mientras codifican. Esto puede disminuir la productividad de los desarrolladores.
* Pérdida de la consistencia del código:
Si GitHub Copilot no puede obtener el contexto de todo el código, el código sugerido puede ser inconsistente con el código existente. Esto puede afectar negativamente la legibilidad y mantenibilidad del código y ralentizar la velocidad de desarrollo de todo el equipo.

## Historia

Un día, una ingeniera de nivel intermedio en el equipo del proyecto decidió desarrollar una nueva funcionalidad usando GitHub Copilot. Estaba fascinada con GitHub Copilot y creía que le ayudaría a escribir código rápidamente.

Sin embargo, a medida que avanzaba el desarrollo, notó que el código sugerido por GitHub Copilot a veces era inexacto. Aun así, lo corrigió manualmente y continuó el desarrollo, pero gradualmente se cansó de la tarea. Además, otros miembros del equipo señalaron que el código sugerido por GitHub Copilot carecía de consistencia.

Se preguntó por qué GitHub Copilot no hacía sugerencias precisas y comenzó a investigar, descubriendo que una de las razones de las sugerencias inexactas era que los archivos relacionados no estaban abiertos adecuadamente. Sin embargo, mantener todos los archivos abiertos no es práctico y GitHub Copilot solo envía datos de las pestañas adyacentes, por lo que no tiene sentido mantener muchos archivos abiertos. Además, se dio cuenta de que existe un límite en el número de tokens que se pueden pasar como parte del modelo Codex utilizado por GitHub Copilot.

Por lo tanto, decidió introducir el patrón de directorio de contexto. Al mantener abiertos los archivos relacionados, espera que GitHub Copilot pueda hacer sugerencias más precisas.

## Solución

1. Crear un directorio de contexto:
Cree un directorio donde usted o su equipo puedan recopilar archivos que deseen utilizar para ayudar a proporcionar contexto y reglas para GitHub Copilot.
2. Mantener abiertas las pestañas de archivos relacionados en VSCode:
Actualmente, GitHub Copilot no tiene una función para obtener el contexto de toda la base de código, pero puede leer el archivo actual y todos los archivos abiertos en el IDE. Mantener abiertas las pestañas de archivos relacionados permite a GitHub Copilot hacer sugerencias más precisas.

Puede escribir estos directorios en .gitignore si no desea enviar su contenido.
También puede utilizar los Submódulos de Git para separar el directorio de contexto de los demás.

## Contexto Resultante

El uso del patrón de directorio de contexto permite que GitHub Copilot proporcione sugerencias más precisas. Al mantener abiertas las pestañas de archivos relacionados, puede obtener una finalización de código efectiva.

## Nota

* Actualmente, GitHub Copilot tiene objetivos de lectura de archivo limitados. Al escribir en Python, es recomendable que los archivos de fragmentos y los archivos de referencia de destino también sean código Python.
