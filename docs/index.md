# Documentación del método RK4 en la resolución de problemas dinámicos

## Introducción

En este documento se presenta la documentación del método de Runge-Kutta de cuarto orden (RK4), utilizado para resolver problemas dinámicos de valor inicial. Un problema de valor inicial se describe mediante la ecuación diferencial

\[
\frac{dy}{dt} = f(t, y)
\]

con la condición inicial

\[
y(t_0) = y_0.
\]

Este método es particularmente útil en el campo de las matemáticas aplicadas, donde se requiere un enfoque numérico para la resolución de ecuaciones diferenciales.

## Contexto

La ecuación presentada describe cómo un estado \( y \) del sistema cambia con respecto al tiempo \( t \). En este caso, \( y \) puede representarse mediante diferentes objetos matemáticos, incluyendo cantidades escalares y matrices que representan un operador lineal.

Este documento está basado en el código implementado en el repositorio de GitHub [FisicaComputacional](https://github.com/mbrenesn/FisicaComputacional/blob/main/Tema_03/dynamics.ipynb), donde se resolvió específicamente el caso donde \( f(t, y) = -i[O, y(t)] \). Este problema es relevante debido a que no existe dependencia temporal explícita en la función \( f(t, y) \).

A través de esta documentación, se espera proporcionar una comprensión clara del método RK4, su implementación, y ejemplos de uso práctico, junto con los resultados obtenidos.

