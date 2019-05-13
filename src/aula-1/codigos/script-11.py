palavras = ['casa', 'bola', 'lapis'
  , 'Bola', 'LaPis', 'BOLA']
frequencias = {}

for palavra in palavras:
  chave = palavra.lower()
  if chave not in frequencias.keys():
    frequencias[chave] = 1
  else:
    frequencias[chave] += 1

maior_frequencia = 0
maior_palavra    = ""
for palavra, frequencia in frequencias.items():
  if frequencia > maior_frequencia:
    maior_frequencia = frequencia
    maior_palavra    = palavra

print("A palavra com maior frequencia e " 
  + maior_palavra 
  + " com " + str(maior_frequencia) 
  + " ocorrencias ")
    
