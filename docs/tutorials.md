# Tutorial: Uso del método RK4

Este tutorial muestra cómo implementar el método de Runge-Kutta de cuarto orden (RK4) para resolver una ecuación diferencial dada por:

\begin{align}
	\frac{dy}{dt} = -i[O, y(t)],
\end{align}

con la condición inicial \( y(t_0) = y_0 \).

## Implementación del método RK4

### Paso 1: Definición de la función `dyn_generator`

Primero, se define la función que representa la dinámica del sistema. Esta función tomará como entrada el operador \( O \) y el estado actual \( y(t) \).


