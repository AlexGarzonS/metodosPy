import numpy as np
import matplotlib.pyplot as plt

# Función encargada de la operación matemática
def puntofijo(gx, a, tolera, iteramax):
    i = 1
    b = gx(a)
    tramo = abs(b - a)

    iteraciones = [(a, b)]

    while tramo >= tolera and i <= iteramax:
        a = b
        b = gx(a)
        tramo = abs(b - a)

        iteraciones.append((a, b))

        i += 1
    respuesta = b

    if i >= iteramax:
        respuesta = np.nan
    return respuesta, iteraciones

# Definir funciones f(x) y g(x)
fx = lambda x: np.exp(-x) - x
gx = lambda x: np.exp(-x)

# Inputs
a = float(input("Por favor, introduce la semilla (punto inicial): "))
tolera = float(input("Por favor, introduce la tolerancia: "))
num_iteraciones_a_imprimir = int(input("Por favor, introduce el número de iteraciones que deseadas imprimir: "))

# Ejecución y extracción de datos
respuesta, iteraciones = puntofijo(gx, a, tolera, num_iteraciones_a_imprimir)

# Longitud de las iteraciones
valoriteraciones = len(iteraciones)

# Definir valores de x para las funciones
xi = np.linspace(a - 1, a + 1, 100)  # Ajuste del rango de valores de x para f(x)
fi = fx(xi)
gi = gx(xi)

# Gráfico de tela de araña
plt.figure(figsize=(8, 6))
for i in range(valoriteraciones):
    if i < len(iteraciones) - 1:
        plt.plot([iteraciones[i][0], iteraciones[i + 1][0]], [iteraciones[i][1], iteraciones[i][1]], color='black')
        plt.plot([iteraciones[i + 1][0], iteraciones[i + 1][0]], [iteraciones[i][1], iteraciones[i + 1][1]], color='black')
    print(f"Iteración {i + 1}: x = {iteraciones[i][0]}, gx(x) = {iteraciones[i][1]}")

# Graficar las funciones f(x) y g(x)
plt.plot(xi, fi, label='f(x)')
plt.plot(xi, gi, label='g(x)')
plt.plot(xi, xi, label='y = x', linestyle='--', color='gray')

plt.xlabel('x')
plt.ylabel('gx(x)')
plt.title('Gráfica de telaraña del método del punto fijo')
plt.grid(True)
plt.legend()
plt.show()

print("\nEl punto fijo encontrado es:", respuesta)
