import os
import pandas as pd
brics = pd.read_csv("{}/pandas/brics.csv".format(os.getcwd())
  , index_col=0)

print(brics.iloc[:, [0, 1]])
#              pais   capital
# BR         Brasil  Brasilia
# RU         Russia    Moscou
# IN          India      Deli
# CH          China    Pequin
# AS  Africa do Sul  Pretoria

print(brics.iloc[[1, 2, 3], [0, 1]])
#       pais capital
# RU  Russia  Moscou
# IN   India    Deli
# CH   China  Pequin