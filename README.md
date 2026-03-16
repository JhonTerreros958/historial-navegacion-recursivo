## Historial de Navegación Recursivo

## Descripción

Este proyecto simula el botón **"Atrás"** de un navegador web utilizando **recursividad** y una estructura tipo **pila (stack)**.

El programa elimina páginas del historial una por una, como lo haría un navegador cuando el usuario retrocede en su navegación.

## Funcionamiento

La función `retroceder(historial, pasos)` recibe:

> **historial**: una lista con las páginas visitadas.
> **pasos**: número de páginas que se desea retroceder.

El algoritmo elimina páginas del historial hasta que se cumpla una de estas condiciones:

1. Se alcanzan los pasos indicados.
2. El historial queda vacío.
3. Se encuentra una página con **"Error 404"**, en cuyo caso el retroceso se detiene inmediatamente.

## Ejemplo de historial

[
"google.com",
"uniminuto.edu",
"Error 404: Campus Virtual",
"github.com",
"stackoverflow.com"
]

## Lenguaje utilizado

Python

## Autor

Jhon Alexander Terreros vargas
