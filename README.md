# Simulación de un Sistema en Espacio de Estados

![Image](https://github.com/user-attachments/assets/ef89cd9c-94e5-4bac-a624-f97d124e29c4)


Este proyecto implementa una simulación de un sistema en espacio de estados utilizando Python y las bibliotecas `numpy`, `matplotlib` y `scipy`. La simulación representa la evolución de los estados de un sistema de segundo orden (RLC) en el tiempo.

## Descripción del Código

El script contiene una función principal:

### `simular_espacio_estados(A, B, C, D, t1, ut, x0=None)`
Esta función realiza lo siguiente:
1. Crea un sistema en espacio de estados con las matrices `A`, `B`, `C`, `D`.
2. Define la condición inicial `x0` (por defecto, es un vector de ceros).
3. Genera una entrada tipo paso `u` con amplitud `ut`.
4. Simula la respuesta del sistema usando `lsim` de `scipy.signal`.
5. Grafica la evolución de los estados en el tiempo.

### Parámetros
- `A`, `B`, `C`, `D`: Matrices del sistema en espacio de estados.
- `t1`: Vector de tiempo.
- `ut`: Amplitud de la entrada escalón.
- `x0`: Condición inicial opcional (por defecto, vector de ceros).

## Ejemplo de Uso

El código define un sistema RLC con:
- `R1 = 10 Ω`
- `L1 = 2 H`
- `C1 = 0.01 F`
- Entrada `ei = 1 V`

Las matrices del sistema son:
```python
A = np.array([[0, 1/C1],
              [-1/L1, -R1/L1]])
B = np.array([[0],
              [1/L1]])
C = np.array([[1, 1]])
D = np.array([[0]])
```
# Requisitos
Asegúrate de tener instaladas las siguientes bibliotecas:
```python
pip install numpy matplotlib scipy

```

## Para la ejecucion
Para ejecutar el script:
```python

python statespace.py
```
Este código permite analizar el comportamiento de un sistema dinámico definido en espacio de estados y visualizar su evolución en el tiempo.