import matplotlib.pyplot as plt

def interpolation(d, x):
    output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
    return output

# Driver Code
data = [[2019, 12124], [2021, 5700]]
years = [d[0] for d in data]
population = [d[1] for d in data]

# Interpolate for the missing year (2020)
year_x = 2020
population_x = interpolation(data, year_x)

# Plotting
plt.plot(years, population, 'bo-', label='Data Points')
plt.plot(year_x, population_x, 'ro', label='Interpolated Point')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Interpolation')
plt.legend()
plt.grid(True)
plt.show()