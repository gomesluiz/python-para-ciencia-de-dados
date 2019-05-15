import os
import pandas as pd
brics = pd.read_csv("{}/pandas/brics.csv".format(os.getcwd())
  , index_col=0)
  
print(brics.loc["RU"])
# pais         Russia       <- Pandas Series
# capital      Moscou
# area           17.1
# populacao     143.5
# Name: RU, dtype: object

print(brics.loc[["RU"]])
#       pais capital  area  populacao  <- Pandas Dataframes
# RU  Russia  Moscou  17.1      143.5

print(brics.loc[["RU", "IN", "CH"]])
#       pais capital   area  populacao
# RU  Russia  Moscou 17.100      143.5
# IN   India    Deli  3.286     1252.0
# CH   China  Pequin  9.597     1357.0