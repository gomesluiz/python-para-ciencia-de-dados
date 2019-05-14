import numpy as np 
alturas = [ 1.73, 1.68, 1.71, 1.89, 1.79 ]
pesos = [ 65.4, 59.2, 63.6, 88.4, 68.7 ]

np_alturas = np.array(alturas)
np_pesos = np.array(pesos)

imcs = np_pesos / np_alturas ** 2
print(imcs)
# output:
# [21.85171573 20.97505669 21.75028214 24.7473475 21.44127836]