import pandas as pd
s = pd.Series([1, 0, 2, 1, 2, 3], index=['branco', 'branco', 'azul'
  , 'verde', 'verde', 'amarelo'])

# valores unicos
print(s.unique())
# outuput: [1 0 2 3]

# quantidade de ocorrencias
print(s.value_counts())
# outuput:
# 2   2
# 1   2
# 3   1
# 0   1



# verificando a existencia
print(s.isin([0,3]))
# branco    False
# branco    True
# azul      False
# verde     False
# verde     False
# amarelo   True