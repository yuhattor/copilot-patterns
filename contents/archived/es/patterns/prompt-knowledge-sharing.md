# Prompt Compartir conocimientos

{% hint style="info" %}
Este documento aún se encuentra en proceso de verificación. Esperamos tener discusiones activas en el [issue de GitHub](https://github.com/AI-Native-Development/docs/issues/8).
{% endhint %}

## Descripción

Compartir prompts para generar código y utilizarlos como recursos para el aprendizaje de los miembros del equipo es importante.

## Problema

Trabajar con IA, como en el caso de GitHub Copilot, permite generar código de alta calidad, pero esto no garantiza que sea código fácil de leer y con buen rendimiento para los ingenieros senior. Cuando se utilizan códigos altamente simplificados o expresiones lingüísticas específicas del lenguaje de programación, la colaboración de los ingenieros en áreas específicas puede volverse difícil.

## Historia

Estás buscando qué prompts escribir para aprovechar GitHub Copilot al máximo. Como ingeniero senior, logras generar un código impresionante en colaboración con GitHub Copilot después de muchas pruebas y errores en la implementación de una función. Un ingeniero del mismo equipo que estaba mirando desde el asiento de al lado dijo: "¡Siempre escribes así! Me doy cuenta de cómo logras generar código impresionante todo el tiempo."

Te das cuenta de que los prompts que utilizaste para llegar al mejor resultado y el proceso de prueba y error son recursos importantes para que los miembros del equipo puedan aprender. Al mismo tiempo, descubres el problema de que los prompts no están incluidos en los archivos del producto y comienzas a pensar en cómo compartirlos.

## Contexto

GitHub Copilot ha sido implementado, pero no hay una forma compartida de utilizarlo entre los ingenieros. Además, los prompts que cada ingeniero utiliza en GitHub Copilot no se comparten.

## Solución

El equipo debe considerar cómo compartir prompts y cómo escribir comentarios. Es recomendable utilizar comentarios que funcionen como documentos para que los prompts no se conviertan en ruido.

Se pueden considerar los siguientes patrones para compartir prompts:

* Escribir directamente en el archivo:
Dejar los prompts en el archivo para que el equipo pueda aprender de ellos. Es importante dejar una cantidad adecuada de prompts para que no se conviertan en ruido. También se pueden convertir algunos prompts en comentarios de documentos o explicaciones. Además, los prompts pueden ser revisados durante la revisión del código, lo que puede mejorar la capacitación de los ingenieros.
* Documentación pasiva:
Incluir algunos prompts en los comentarios de las solicitudes de extracción o problemas. Esto mejorará la legibilidad de los archivos de código, pero no se podrá hacer referencia a los prompts en el editor.
* Programación en equipo:
No dejar los prompts en los archivos o PR/Issues, sino organizar una sesión de programación en equipo con ingenieros senior para experimentar con el desarrollo. Es importante compartir lo que se aprendió durante esta sesión como un documento separado.

## Contexto resultante

El nivel de habilidad de todo el equipo mejora y se promueve un aprendizaje efectivo a través del intercambio de prompts. La legibilidad del código mejora y, gracias a los comentarios que funcionan como documentos en lugar de simplemente prompts, se facilita la comprensión del código.
