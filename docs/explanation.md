# Método RK4

## Descripción del Método

El método de Runge-Kutta de cuarto orden (RK4) es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDO) de la forma:

\begin{align}
	\frac{dy}{dt} = f(t, y)
\end{align}

con la condición inicial:

\begin{align}
	y(t_0) = y_0.
\end{align}

Este método es ampliamente utilizado debido a su precisión y facilidad de implementación. A diferencia de los métodos de orden inferior, como el método de Euler, el método RK4 ofrece una mejor aproximación al comportamiento del sistema, lo que lo hace adecuado para una amplia gama de aplicaciones.

## Esquema del Método

El esquema del método RK4 se basa en el cálculo de cuatro pendientes intermedias, que son evaluadas en diferentes puntos dentro del intervalo de integración. El algoritmo se puede resumir en los siguientes pasos:

- **Cálculo de las pendientes**:

   \begin{align}
   k_1 = f(t_n, y_n)
   \end{align}

   \begin{align}
   k_2 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_1\right)
   \end{align}

   \begin{align}
   k_3 = f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} k_2\right)
   \end{align}

   \begin{align}
   k_4 = f(t_n + h, y_n + h k_3)
   \end{align}

   donde \( h \) es el tamaño del paso y \( t_n \) y \( y_n \) son el tiempo y el estado del sistema en el paso \( n \).

- **Actualización del valor de \( y \)**:

   \begin{align}
   y_{n+1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)
   \end{align}

- **Iteración**: Se repiten los pasos anteriores para cada intervalo de tiempo hasta alcanzar el tiempo deseado.

## Aplicación del Método RK4

El método RK4 se utiliza frecuentemente en simulaciones numéricas donde se requiere resolver sistemas dinámicos complejos. En el contexto del problema planteado, se aplica específicamente para resolver la ecuación:

\begin{align}
\frac{dy}{dt} = -i[O, y(t)],
\end{align}

donde no existe dependencia temporal explícita en la función \( f(t, y) \).

### Ventajas del Método RK4

- **Precisión**: El RK4 es un método de cuarto orden, lo que significa que su error de truncamiento es significativamente menor que el de métodos de orden inferior.
- **Flexibilidad**: Puede ser aplicado a una amplia variedad de ecuaciones diferenciales, incluyendo aquellas que no son lineales.

### Consideraciones

- **Costo Computacional**: Aunque RK4 es más preciso, también es más costoso computacionalmente que métodos de orden inferior, ya que requiere múltiples evaluaciones de la función en cada paso.
- **Tamaño del Paso**: La elección del tamaño del paso \( h \) es crucial para el rendimiento del método; un paso demasiado grande puede llevar a resultados inexactos, mientras que un paso demasiado pequeño puede resultar en un tiempo de cálculo innecesariamente largo.

## Conclusión

El método RK4 es una herramienta poderosa para la resolución de problemas de valor inicial en ecuaciones diferenciales. Su implementación adecuada permite obtener resultados precisos y confiables en simulaciones numéricas, facilitando la comprensión de sistemas dinámicos complejos.

