from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

xi = np.array([  3,   5,   7,   9])
yi = np.array([2.5, 1.5, 2.0, 1.8])

# spline "not a knot" sin extrapolación
y_1 = CubicSpline(xi,yi,extrapolate=False)

plt.figure(figsize = (4, 3))           # Tamaño de figura
plt.rcParams.update({'font.size': 10}) # Tamaño de fuente

x = np.linspace(2,10,100) # arreglo para graficar

plt.plot(xi, yi, 'ok')     # graficamos los xi, yi
plt.plot(x, y_1(x), '-b')  # graficamos la función

plt.title('Interpolación spline')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()