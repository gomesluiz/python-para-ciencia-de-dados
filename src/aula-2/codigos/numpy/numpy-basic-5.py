
import numpy as np 
medidas = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                   [65.4, 59.2, 63.6, 88.4, 68.7]])

print(medidas[0])
# [1.73, 1.68, 1.71, 1.89, 1.79]

print(medidas[0][2])
# 1.71

print(medidas[0, 2])
# 1.71

print(medidas[:, 1:3])
#   [[ 1.68,  1.71],
#    [59.2 , 63.6 ]]