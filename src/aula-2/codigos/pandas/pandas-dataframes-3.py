import os
import pandas as pd
brics = pd.read_csv("{}/pandas/brics.csv".format(os.getcwd())
  , index_col=0)
print(brics["pais"])
# BR           Brasil
# RU           Russia
# IN            India
# CH            China
# AS    Africa do Sul
# Name: pais, dtype: object
print(type(brics["pais"]))
# <class 'pandas.core.series.Series'>

print(brics[["pais"]])
#                pais
# BR           Brasil
# RU           Russia
# IN            India
# CH            China
# AS    Africa do Sul
# <class 'pandas.core.frame.DataFrame'>


print(brics[["pais", "capital"]])
#              pais   capital
# BR         Brasil  Brasilia
# RU         Russia    Moscou
# IN          India      Deli
# CH          China    Pequin
# AS  Africa do Sul  Pretoria
