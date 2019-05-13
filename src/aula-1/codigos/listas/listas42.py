
populacoes = {
  'america' : ['brasil', 207, 'argentina', 44.293
    , 'uruguai', 3.36],
  'europa'  : ['portugal', 10.83, 'espanha', 49.95
    , 'italia', 62.13],
  'asia'    : ['filipinas', 104.25, 'malasia', 31.38
    , 'tailandia', 68.41]
}

for continente, paises in populacoes.items():
  print(continente.upper())
  for n in range(0, len(paises), 2):
    print('Pais : ' +  paises[n] + ' Populacao: ' + str(paises[n+1]))

# output:
# AMERICA
# Pais : brasil Populacao: 207
# Pais : argentina Populacao: 44.293
# Pais : uruguai Populacao: 3.36
# EUROPA
# Pais : portugal Populacao: 10.83
# Pais : espanha Populacao: 49.95
# Pais : italia Populacao: 62.13
# ASIA
# Pais : filipinas Populacao: 104.25
# Pais : malasia Populacao: 31.38
# Pais : tailandia Populacao: 68.41


