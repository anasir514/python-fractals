import numpy as np
import matplotlib.pyplot as plt
def mandel(c, z):
    return z*z + c
N, n, part = 600, 600, []
for c_r in np.linspace(-2, 2, N):
    for c_i in np.linspace(-2, 2, N):
        k = 0
        z = [0]
        for i in range(0, n):
            z.append(mandel(complex(c_r, c_i), z[k]))
            k += 1
        comp = z[n]
        if (comp.real*comp.real + comp.imag*comp.imag) < 2:
            part.append([c_r, c_i])
plt.figure(figsize = (10, 10))
for i in range(0, len(part)):
    plt.plot(part[i][0], part[i][1], ".k", markersize = 2)
plt.show()