import numpy as np
import matplotlib.pyplot as plt

# Definición del operador O
oOper = np.array([[0, 1], [1, 0]])
print("Operador O:")
print(oOper)

# Estado inicial y(t_0) = y_0
yInit = np.array([[1, 0], [0, 0]])
print("Estado inicial y(t_0):")
print(yInit)

def dyn_generator(oper, state):
    """
    Calcula la dinámica del sistema dada un operador y un estado.

    Parámetros:
    oper (np.array): Matriz que representa el operador del sistema.
    state (np.array): Estado actual del sistema.

    Retorna:
    np.array: La tasa de cambio del estado.
    """
    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))

def rk4(func, oper, state, h):
    """
    Método de Runge-Kutta de cuarto orden.

    Parámetros:
    func (function): Función que calcula la dinámica del sistema.
    oper (np.array): Matriz que representa el operador del sistema.
    state (np.array): Estado actual del sistema.
    h (float): Tamaño del paso temporal.

    Retorna:
    np.array: El nuevo estado del sistema.
    """
    # Calcular los cuatro términos k1, k2, k3, y k4
    k1 = h * func(oper, state)
    k2 = h * func(oper, state + k1 / 2)
    k3 = h * func(oper, state + k2 / 2)
    k4 = h * func(oper, state + k3)

    # Calcular el nuevo estado usando la combinación ponderada de k1, k2, k3, y k4
    return state + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

# Definir el tiempo
times = np.linspace(0, 10.0, 100)

# Calcular el paso temporal
h = times[1] - times[0]
# Imprimir el paso temporal
print(f"El paso temporal h es: {h}")

# Crear copias para almacenar resultados
yCopy = yInit.copy()
stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)

# Rutina principal para la evolución temporal
for tt in range(times.size):
    # Guardar los valores de las entradas (0,0) y (1,1) en los arreglos definidos
    stateQuant00[tt] = yInit[0, 0]
    stateQuant11[tt] = yInit[1, 1]

    # Invocar rk4 operando sobre yInit
    yN = rk4(dyn_generator, oOper, yInit, h)

    # Asignar yN a yInit
    yInit = yN

    # Imprimir valores intermedios para debugging
    if tt % 10 == 0:  # Imprimir cada 10 pasos
        print(f"Tiempo: {times[tt]:.2f}, Estado:\n{yInit}")

# Graficar los resultados en una sola gráfica
plt.figure(figsize=(10, 6))
plt.plot(times, stateQuant00, label='Entrada (0,0)', color='blue')
plt.plot(times, stateQuant11, label='Entrada (1,1)', color='orange')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Evolución de las entradas (0,0) y (1,1)')
plt.legend()
plt.grid(True)
plt.savefig('grafico.png')
plt.show()
