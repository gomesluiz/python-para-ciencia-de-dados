empresas   = { 'GE': 'General Motors', 'CAT': 'Caterpillar', 'EK': 'Eastman Kodak'}
compras = [('GE', 100, '10/09/2001', 48), ('CAT', 100, '01/04/1999', 24), ('GE', 200, '10/09/2001', 56)]
totals   = {}

for empresa in empresas:
  totals[empresa] = 0

for compra in compras:
  simbolo = compra[0] 
  print(simbolo, empresas[simbolo], compra[1], compra[2], compra[3])
  totals[compra[0]] = compra[1] * compra[3]

for simbolo, empresa in empresas.items():
    print(simbolo, empresa, totals[simbolo])
