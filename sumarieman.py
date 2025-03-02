import sympy as sp
import numpy as np

# Definir la variable y la función
x, n, i = sp.symbols('x n i')
f = x**2 + 10  # Función dada

# Definir los límites de integración
a, b = -1, 3

# Paso de la partición
dx = (b - a) / n  

# Puntos de evaluación (suma de Riemann por la derecha)
x_i = a + i * dx  
f_xi = f.subs(x, x_i)  # Evaluar la función en x_i

# Expresión de la suma de Riemann
riemann_sum = sp.summation(f_xi * dx, (i, 1, n))

# Mostrar la expresión simbólica de la suma de Riemann
print("Suma de Riemann (simbólica):")
sp.pprint(riemann_sum)

# Aproximación numérica con n=10
n_value = 10
riemann_numeric = riemann_sum.subs(n, n_value).evalf()
print("\nAproximación numérica con n=10:", riemann_numeric)

# Calcular la integral definida (área exacta)
integral_exacta = sp.integrate(f, (x, a, b))

# Mostrar resultado exacto y aproximado
print("\nÁrea exacta bajo la curva:", integral_exacta, "≈", float(integral_exacta))
