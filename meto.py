import numpy as np
import matplotlib.pyplot as plt

# Función a ser evaluada
def fx(x):
    return x**3 + 4*(x**2) - 10

# Algoritmo de la posición falsa
def posicion_falsa(f, a, b, tolerancia=1e-6, max_iter=100):
    iteraciones = []
    fa, fb = f(a), f(b)
    for _ in range(max_iter):
        c = b - fb * (a - b) / (fa - fb)
        fc = f(c)
        iteraciones.append([a, c, b, fa, fc, fb, abs(b - a)])
        cambio = np.sign(fa) * np.sign(fc)
        if cambio > 0:
            a, fa = c, fc
        else:
            b, fb = c, fc
        if abs(b - a) < tolerancia:
            break
    return np.array(iteraciones)

# Encontrar raíces con el método de la posición falsa
a, b = 1, 2
tolerancia = 0.0001
iteraciones = posicion_falsa(fx, a, b, tolerancia)

# Encontrar el máximo de la función
x_values = np.linspace(0, 3, 1000)
y_values = fx(x_values)
max_idx = np.argmax(y_values)
max_x, max_y = x_values[max_idx], y_values[max_idx]

# Graficar la función y las iteraciones del método de la posición falsa
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = x^3 + 4x^2 - 10')
plt.scatter(iteraciones[:, 1], fx(iteraciones[:, 1]), color='red', label='Puntos c')
for i in range(len(iteraciones)):
    plt.plot([iteraciones[i, 1], iteraciones[i, 1]], [0, fx(iteraciones[i, 1])], color='blue', linestyle='--')
    plt.plot([iteraciones[i, 1], max_x], [fx(iteraciones[i, 1]), max_y], color='green', linestyle='--')
plt.axhline(0, color='black', linewidth=0.5)  # Eje x
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de la Posición Falsa para $f(x) = x^3 + 4x^2 - 10$')
plt.grid(True)
plt.legend()
plt.show()