import os
import pandas as pd
brics = pd.read_csv("{}/pandas/brics.csv".format(os.getcwd())
  , index_col=0)
  
print(brics.loc[["RU", "IN", "CH"], ["pais", "capital"]])
#       pais capital
# RU  Russia  Moscou
# IN   India    Deli
# CH   China  Pequin

print(brics.loc[:, ["pais", "capital"]])
#              pais   capital
# BR         Brasil  Brasilia
# RU         Russia    Moscou
# IN          India      Deli
# CH          China    Pequin
# AS  Africa do Sul  Pretoria