import os
import pandas as pd
brics = pd.read_csv("{}/pandas/brics.csv".format(os.getcwd()))
print(brics)
#   Unnamed: 0           pais   capital    area  populacao
# 0         BR         Brasil  Brasilia   8.516     207.40
# 1         RU         Russia    Moscou  17.100     143.50
# 2         IN          India      Deli   3.286    1252.00
# 3         CH          China    Pequin   9.597    1357.00
# 4         AS  Africa do Sul  Pretoria   1.221      52.98









"""
Indexando o dataframe na leitura.
"""
brics = pd.read_csv("{}/pandas/brics.csv".format(os.getcwd())
  , index_col=0)
print(brics)
#              pais   capital    area  populacao
# BR         Brasil  Brasilia   8.516     207.40
# RU         Russia    Moscou  17.100     143.50
# IN          India      Deli   3.286    1252.00
# CH          China    Pequin   9.597    1357.00
# AS  Africa do Sul  Pretoria   1.221      52.98