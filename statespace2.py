import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lsim, StateSpace

def simular_espacio_estados(A, B, C, D, t1, ut, x0=None):
    # Crear el sistema en espacio de estados
    sistema = StateSpace(A, B, C, D)
    
    # Definir condición inicial si no se proporciona
    if x0 is None:
        x0 = np.zeros(A.shape[0])
    
    # Definir entrada tipo paso
    u = np.ones_like(t1) * ut
    # Simular la respuesta del sistema
    t_out, y, x = lsim(sistema, U=u, T=t1, X0=x0)
    # Graficar los estados
    plt.figure(figsize=(10, 6))
    for i in range(x.shape[1]):
        plt.plot(t_out, x[:, i], label=f'Estado {i+1}')
    # Configurar etiquetas y título del gráfico
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Estados')
    plt.title('Evolución de los estados en el tiempo')
    plt.legend()
    plt.grid()
    plt.show()
    
    return t_out, x, y

# Definición de matrices del sistema con los nuevos parámetros
R1 = 10
L1 = 2
C1 = 0.01
ei = 1

A = np.array([[0, 1],
              [-1/(L1*C1), -R1/L1]])
B = np.array([[0],
              [1/(L1*C1)]])
C = np.array([[1, 0]])
# C = np.array([[0, R1*C1]])  # Alternativa para salida VR
D = np.array([[0]])

# Definir tiempo
t1 = np.linspace(0, 3, 300)  # (Tinicio, Tfin, N° muestras)

# Ejecutar simulación
simular_espacio_estados(A, B, C, D, t1, ei)
