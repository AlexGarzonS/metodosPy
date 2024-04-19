import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def newtonRaphson(x0, tol, n):
    """
    Implementación del método de Newton-Raphson para encontrar raíces de una función.
    
    Parámetros:
        - x0: Aproximación inicial.
        - tol: Tolerancia para la convergencia.
        - n: Número máximo de iteraciones permitidas.
    
    Retorna:
        - Lista de aproximaciones de las raíces.
    """
    x = sp.symbols('x') # crea variable
    f_str = input('Digite la función: ')
    f = sp.sympify(f_str)
    df = sp.diff(f, x) 
    f = sp.lambdify(x, f)
    df = sp.lambdify(x, df)
    approximations = []

    for k in range(n):
        x1 = x0 - f(x0) / df(x0)
        approximations.append(x1)
        if abs(x1 - x0) < tol:
            print('x', k+1, '=', x1, 'es la raíz')
            return approximations
        x0 = x1
        print('x', k+1, '=', x1)

    return approximations

# Llamada a la función para obtener las aproximaciones
approximations = newtonRaphson(np.pi, 0.001, 10)

# Gráfico de convergencia
plt.figure(figsize=(10, 6))
plt.plot(approximations, range(1, len(approximations) + 1), marker='o', color='blue') # Intercambio de coordenadas x e y
plt.title('Convergencia del Método de Newton-Raphson')
plt.ylabel('Iteración')
plt.xlabel('Aproximación de la raíz')
plt.grid(True)
plt.show()