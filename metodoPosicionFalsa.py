import numpy as np
import matplotlib.pyplot as plt

# Función a ser evaluada
fx = lambda x: x**3 + 4*(x**2) - 10

# Definir el rango de x para la gráfica
x_values = np.linspace(0, 3, 400)
y_values = fx(x_values)

# Valores iniciales y tolerancia
a = 1
b = 2
tolera = 0.0001

# Algoritmo de la posición falsa
tabla = []
tramo = abs(b - a)
fa = fx(a)
fb = fx(b)

while not(tramo <= tolera):
    c = b - fb*(a - b)/(fa - fb)
    fc = fx(c)
    tabla.append([a, c, b, fa, fc, fb, tramo])
    cambio = np.sign(fa) * np.sign(fc)
    if cambio > 0:
        tramo = abs(c - a)
        a = c
        fa = fc
    else:
        tramo = abs(b - c)
        b = c
        fb = fc

tabla = np.array(tabla)
c = tabla[-1, 1]

tabla = np.array(tabla) # establece un array de la tabla
ntabla = len(tabla) #se toma la cantidad de valores en la tabla

# SALIDA
np.set_printoptions(precision=9) # indica cuantos decimales usara
for i in range(0,ntabla,1):
    print('iteración:  ',i)
    print('[a,c,b]:    ', tabla[i,0:3])
    print('[fa,fc,fb]: ', tabla[i,3:6])
    print('[tramo]:    ', tabla[i,6])

print('raiz:  ',c)
print('error: ',tramo)

# Gráfica de la función y puntos evaluados
# Gráfica de la función y puntos evaluados
plt.figure(figsize=(10, 6))

# Gráfica de la función
plt.plot(x_values, y_values, label='f(x) = x^3 + 4x^2 - 10')

# Puntos evaluados y encontrados
plt.scatter(tabla[:, 0], fx(tabla[:, 0]), color='red', label='A evaluar')
plt.scatter(tabla[:, 1], fx(tabla[:, 1]), color='green', label='Punto encontrado')

# Líneas representando el intervalo de búsqueda y los puntos
for i in range(len(tabla)):
    plt.plot([tabla[i, 0], tabla[i, 2]], [fx(tabla[i, 0]), fx(tabla[i, 2])], color='orange', linestyle='--', linewidth=1)  # Intervalo de búsqueda
    plt.plot([tabla[i, 0], tabla[i, 1], tabla[i, 2]], [fx(tabla[i, 0]), fx(tabla[i, 1]), fx(tabla[i, 2])], color='blue', linewidth=1)  # Conexión de puntos

# Etiquetas y título
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de la Posición Falsa')
plt.legend()
plt.grid(True)
plt.show()