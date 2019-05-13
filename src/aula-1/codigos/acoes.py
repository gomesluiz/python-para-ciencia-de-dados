empresas   = { 
    'GE' : 'General Motors'
  , 'CAT': 'Caterpillar'
  , 'EK' : 'Eastman Kodak'
}
compras = [
    ('GE',  100, '10/09/2001', 48)
  , ('CAT', 100, '01/04/1999', 24)
  , ('GE' , 200, '10/09/2001', 56)
]
totais = {}
for empresa in empresas:
  totais[empresa] = 0

print("\nRELATORIO COMPLETO")
for compra in compras:
  simbolo = compra[0] 
  totais[simbolo] += compra[1] * compra[3]
  print(simbolo, empresas[simbolo]
  , compra[1], compra[2], compra[3])

print("\nRESUMO DE COMPRAS")
for simbolo, empresa in empresas.items():
    print(simbolo, empresa, totais[simbolo])
