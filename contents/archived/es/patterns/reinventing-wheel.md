# Reinventar la Rueda

## Descripción

"Reinventar la rueda" se considera a menudo ineficiente y es importante utilizar recursos de código abierto o aumentar los recursos compartidos en una organización.
Sin embargo, depender del código alojado por alguien desconocido puede causar problemas de mantenimiento.
En casos en los que es necesario depender de una gran dependencia como una biblioteca o un marco, puede ser preferible reinventar la rueda.

Este patrón está inspirado en una publicación de blog de Matt Rickard sobre [tener un GitHub Copilot](https://matt-rickard.com/having-a-copilot).

> Prefiere copiar un poco a depender de un poco
> En lugar de vender en left-pad como una dependencia, usa GitHub Copilot para generar la función.
Hay beneficios al usar bibliotecas genéricas probadas en la batalla, pero también beneficios al traer un código simple en el árbol.

## Problema

¿Has oído hablar del problema de left-pad?
En 2016, una biblioteca llamada left-pad fue eliminada de npm, lo que hizo que las famosas bibliotecas que dependen de ella se rompieran.
Left-pad es una biblioteca JavaScript simple que rellena el lado izquierdo de una cadena con un número especificado de caracteres o espacios si no se especifican caracteres.
Es una implementación simple con solo alrededor de 10 líneas de código excluyendo las líneas en blanco.

Existen muchos enfoques para evitar reinventar la rueda, como la fuente interna y el intercambio de propiedad de código en XP.
Sin embargo, también es importante considerar el código externo que tiene un impacto significativo.
Cuando el alcance del código proporcionado es muy limitado, puede ser mejor mantenerlo interno en lugar de depender de dependencias externas.

## Contexto

GitHub Copilot es experto en generar código simple.
Si bien algunos argumentan que es mejor evitar las dependencias por completo, eso se aplica a las dependencias que tienen relaciones interdependientes en la lógica empresarial y la implementación.
Para las funciones sin estado o aquellas que solo dependen de un lado, es posible crearlas utilizando GitHub Copilot.

## Solución

El tamaño de las dependencias puede determinar si es necesario reinventar la rueda.
Si una dependencia es pequeña y tiene un impacto limitado, puede ser beneficioso reinventar la rueda.
El problema de left-pad es un ejemplo de esto.
