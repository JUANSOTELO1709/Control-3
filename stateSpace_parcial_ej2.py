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

# Parámetros del nuevo circuito
R1 = 5  # Ohmios
R2 = 10  # Ohmios
L = 0.01  # Henrios
C = 0.001  # Faradios
ei = 1  # Voltios

# Matrices del sistema
A = np.array([[0, 1/C],
              [1/L, -(R1 + R2)/L]])
B = np.array([[0],
              [1/L]])
C = np.array([[1, 0]])  # Salida: voltaje del capacitor
D = np.array([[0]])

# Definir tiempo
t1 = np.linspace(0, 3, 300)  # (Tinicio, Tfin, N° muestras)

# Ejecutar simulación
simular_espacio_estados(A, B, C, D, t1, ei)
