import os
import pandas as pd
brics = pd.read_csv("{}/aula-2/codigos/pandas/brics.csv".format(os.getcwd())
  , index_col=0)

print(brics)
#              pais   capital    area  populacao
# BR         Brasil  Brasilia   8.516     207.40
# RU         Russia    Moscou  17.100     143.50
# IN          India      Deli   3.286    1252.00
# CH          China    Pequin   9.597    1357.00
# AS  Africa do Sul  Pretoria   1.221      52.98

print(brics["area"])
# BR     8.516                Alternativas:
# RU    17.100                brics.loc[:, "area"]
# IN     3.286                brics.iloc[:, 2]
# CH     9.597
# AS     1.221
# Name: area, dtype: float64

print(brics["area"] > 8)
# BR     True
# RU     True
# IN    False
# CH     True
# AS    False
# Name: area, dtype: bool

print(brics[brics["area"] > 8])
#       pais   capital    area  populacao
# BR  Brasil  Brasilia   8.516      207.4
# RU  Russia    Moscou  17.100      143.5
# CH   China    Pequin   9.597     1357.0