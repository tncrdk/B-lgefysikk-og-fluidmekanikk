import numpy as np
import matplotlib.pyplot as plt

k = 2*np.pi / 10 # [1/cm]
w = 200*np.pi # [1/s]

def y(x: float, t: float) -> float:
    return np.sin(k*x-w*t)

x_values = np.linspace(0, 25, 100)
y0_values = y(x_values, 0)
y1_values = y(x_values, 2.5E-3)
y2_values = y(x_values, 5E-3)

plt.plot(x_values, y0_values)
plt.savefig("Plot0.png")

plt.plot(x_values, y1_values)
plt.savefig("Plot1.png")

plt.plot(x_values, y2_values)
plt.savefig("Plot2.png")