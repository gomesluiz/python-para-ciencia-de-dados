import numpy as np 
import os
import pandas as pd
brics = pd.read_csv("{}/aula-2/codigos/pandas/brics.csv".format(os.getcwd())
  , index_col=0)

filtro_por_area = np.logical_and(brics["area"] > 8, 
                                 brics["area"] < 10)
print(brics[filtro_por_area])
#       pais   capital    area  populacao
# BR  Brasil  Brasilia   8.516      207.4
# CH   China    Pequin   9.597     1357.0