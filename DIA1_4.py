import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.array ( [7.5, 4.48, 8.60, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06] )
y = np.array ( [28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68, 21.89] )
Vec = np.c_[x, y]  #???ask teacher

#File creation
file4 = open( 'cuarto.txt', 'w')

#file writing & closing
np.savetxt(file4, Vec, fmt='%f', delimiter='\t', header="x #y")
file4.close()

#file reading
raw_array = np.loadtxt(fname="/home/lior/Documents/WORKSHOP_PYTHON/DIA1/cuarto.txt", skiprows=1)

x=raw_array[:, 0]
y=raw_array[:, 1]

#=======================================
#polynomial fitting 1st degree with numpy
#=======================================

m, b = np.polyfit(x, y, 1)

y_funcion = m*x+b
# print(m, b)

plt.plot(x, y_funcion, 'go')

#=======================================
#polynomial fitting 1st degree with scipy
#=======================================

def func(x, a, b):
    return a * x + b

popt, pcov = curve_fit(func, x, y)
plt.plot(x,func(x, *popt),'r--')

#=====================================================
#--------------PLOTS---------------
#if plotting two fittings: one overlaps the other and cannot be seen
#=====================================================
plt.scatter(x, y)  #scatter plot

plt.title('ejercicio 4') #title
plt.xlabel('X[#]') #xlabel
plt.ylabel('Y[#]') #ylabel

plt.show()




