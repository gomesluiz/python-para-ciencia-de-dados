
populacoes = {
  'america' : {'brasil': 207, 'argentina': 44.293
    , 'uruguai': 3.36},
  'europa'  : {'portugal': 10.83, 'espanha': 49.95
    , 'italia': 62.13},
  'asia'    : {'filipinas': 104.25, 'malasia': 31.38
    , 'tailandia': 68.41}
}

for continente, paises in populacoes.items():
  print(continente.upper())
  for pais, populacao in paises.items():
    print('Pais : ' +  pais + ' Populacao: ' + str(populacao))

# output:
# AMERICA
# Pais : argentina Populacao: 44.293
# Pais : brasil Populacao: 207
# Pais : uruguai Populacao: 3.36
# EUROPA
# Pais : italia Populacao: 62.13
# Pais : portugal Populacao: 10.83
# Pais : espanha Populacao: 49.95
# ASIA
# Pais : filipinas Populacao: 104.25
# Pais : malasia Populacao: 31.38
# Pais : tailandia Populacao: 68.41

