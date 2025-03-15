import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, lsim

# Parámetros ajustados del circuito
CR1 = 1.0  # Resistencia asociada (Ohmios)
CR3 = 2.0  # Resistencia asociada (Ohmios)
G = 0.5    # Ganancia (unidad arbitraria)
ei = 1.0   # Entrada constante del sistema (Voltios)
L = 0.01   # Inductancia (Henrios)
R = 5.0    # Resistencia total (Ohmios)

# Ajuste de las matrices A, B, C, D
A = np.array([[-1 / (CR1 * CR3), ei / G],
              [1 / L, -R / L]])
B = np.array([[0],
              [1 / L]])
C = np.array([[1, 0]])  # Observamos solo el estado x1 como salida
D = np.array([[0]])

# Vector de tiempo para la simulación
t = np.linspace(0, 5, 500)  # Tiempo de 0 a 5 segundos con 500 puntos

# Entrada del sistema
u = np.ones_like(t)  # Entrada constante de valor 1

# Condiciones iniciales
x0 = np.array([0, 0])  # Estados iniciales

# Crear sistema en espacio de estados y simular
sistema = StateSpace(A, B, C, D)
t_out, y, x = lsim(sistema, U=u, T=t, X0=x0)

# Graficar los resultados
plt.figure(figsize=(12, 8))

# Graficar estados internos
plt.subplot(2, 1, 1)
plt.plot(t_out, x[:, 0], label="Estado x1 (Ejemplo: Voltaje en C)")
plt.plot(t_out, x[:, 1], label="Estado x2 (Ejemplo: Corriente en L)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Valor de los estados")
plt.title("Evolución de los Estados Internos")
plt.legend()
plt.grid()

# Graficar salida
plt.subplot(2, 1, 2)
plt.plot(t_out, y, label="Salida del Sistema (Ejemplo: Voltaje observado)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Valor de la salida")
plt.title("Respuesta de Salida del Sistema")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
