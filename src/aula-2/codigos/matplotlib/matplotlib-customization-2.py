import matplotlib.pyplot as plt 
anos = [
  1900, 1950, 1955, 1960, 1965,
  1970, 1975, 1980, 1985, 1990,
  1995, 2000, 2005
 ]
pops = [
  1.65, 2.51, 2.75, 3.02, 3.33,
  3.69, 4.06, 4.43, 4.83, 5.26,
  5.67, 6.07, 6.45
]

plt.plot(anos, pops)
plt.xlabel('Ano')
plt.ylabel('Populacao')
plt.show()