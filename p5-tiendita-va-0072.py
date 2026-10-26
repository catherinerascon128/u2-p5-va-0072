import matplotlib.pyplot as plt
import numpy as np

num_mes = np.array(
    [1,2,3,4,5,6]
)
venta_mandado = np.array(
    [0,2000,3500,7000,15000,20000]
)
plt.plot(num_mes,venta_mandado,
         marker="o",
         markersize= 10,
         markerfacecolor="#800E8C",
         markeredgecolor="cyan",)
plt.show()