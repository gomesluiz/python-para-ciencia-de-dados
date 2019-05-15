import pandas as pd
dict = {
"pais":["Brasil","Russia","India","China","Africa do Sul"],
"capital":["Brasila","Moscou","Deli","Pequin","Pretoria"],
"populacao":[207.04, 143.5, 1252, 1357, 52.98]
}

brics = pd.DataFrame(dict)
print(brics)
#             pais    capital  populacao
# 0         Brasil    Brasila     207.04
# 1         Russia     Moscou     143.50
# 2          India  Nova Deli    1252.00
# 3          China     Pequin    1357.00
# 4  Africa do Sul   Pretoria      52.98




"""
Reindexando o dataframe.
"""
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)
#             pais    capital  populacao
# BR        Brasil    Brasila     207.04
# RU        Russia     Moscou     143.50
# I          India  Nova Deli    1252.00
# CH         China     Pequin    1357.00
# AS Africa do Sul   Pretoria      52.98
