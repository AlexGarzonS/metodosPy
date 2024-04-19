import matplotlib.pyplot as plt
import numpy as np

# datos tabulados
xi = [0, 1, 2] # xi
yi = [1, 3, 2] # yi

x0 = 1.5# valor x para determinar
y0 = np.interp(x0, xi, yi) # interpolamos y(x) en x0 = 1.5

# datos tabulados
xi = [0, 1, 2] # xi
yi = [1, 3, 2] # yi

y = lambda x: np.interp(x, xi, yi) # función de interpolación lineal

x = np.array([0.3, 0.5, 0.8]) # arreglo de datos 

plt.figure(figsize = (4, 3))           # Tamaño de figura
plt.rcParams.update({'font.size': 10}) # Tamaño de fuente

# generamos datos para graficar y función de interpolación
x = np.linspace(0,2.0,100)             # 100 puntos entre 0 y 2

plt.plot(x, y(x), '-b', label='$y(x)$')             # graficamos la función
plt.plot(xi, yi, 'ob')                              # graficamos los xi, yi 
plt.plot(1.5, y(1.5), 'or', label='$y(x_0 = 1.5)$') # graficamos y(1.5)

plt.title('Interpolación lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend(frameon=False)
plt.show()