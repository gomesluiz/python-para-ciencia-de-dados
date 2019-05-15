import pandas as pd
s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
print(s[s > 8])
# outuput:
# a   12
# d   9
# dtype: int64
