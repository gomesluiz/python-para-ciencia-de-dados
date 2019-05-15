import pandas as pd
s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
print(s.values)
# outuput:
# [12 -4 7 9]
print(s.index)
# outuput:
# Index (['a', 'b', 'c', ''d], dtype='object')