
import numpy as np 
alturas = np.round(np.random.normal(1.75, 0.20, 5000), 2)
pesos = np.round(np.random.normal(60.32, 15, 5000), 2)

medidas = np.column_stack((alturas, pesos))
print(medidas)
# output:
#   [[1.73  65.9]
#    [2.03  69.91]
#    [1.48  63.18]
# ...
#    [2.    52.73]
#    [1.97  27.79]
#    [1.89  44.29]]