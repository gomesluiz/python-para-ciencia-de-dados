import pandas as pd
s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
print(s[2])
# outuput: 7
print(s['b'])
# outuput: -4
print(s[0:2])
# output:
# a   12
# b   -4
# dtype: int64
print(s[['a', 'b']])
# output:
# a   -4
# b   -7
# dtype: int64