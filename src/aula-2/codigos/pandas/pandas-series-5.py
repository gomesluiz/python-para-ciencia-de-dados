import pandas as pd
s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
s[1] = 0
print(s)
# outuput:
# a   12
# b   0
# c   7
# d   9
# dtype: int64
s['b'] = 1
print(s)
# outuput:
# a   12
# b   1
# c   7
# d   9
# dtype: int64
