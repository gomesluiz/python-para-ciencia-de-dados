
import numpy as np 
array = np.array([[0.173, 0.168, 0.171, 0.189, 0.179],
                   [0.154, 0.259, 0.163, 0.388, 0.287]])

print(np.mean(array[1,: ]))
# 0.2502

print(np.median(array[1,: ]))
# 0.259

print(np.corrcoef(array[0, :] , array[1, :]))
# [[1. 0.79684]
#  [0.79684 1.]]

print(np.std(array[:, 0]))
# 0.0094