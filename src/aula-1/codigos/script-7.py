patio    = 11.25
cozinha  = 18.00
sala     = 20.00
quarto   = 10.75
banheiro = 9.50
areas    = [patio, cozinha, sala, quarto, banheiro]
areas_e_comodos = [ "patio", patio
                   ,"cozinha", cozinha
                   , "sala", sala
                   , "quarto", quarto
                   , "banheiro", banheiro]
for area in areas: 
  print(area)

for n in range(0, 10, 2):
  print("Comodo : " + areas_e_comodos[n]
   + " Area : " + str(areas_e_comodos[n+1]))

print("Maior área: " + str(max(areas)))
print("Menor área: " + str(min(areas)))
print("Total de áreas : " + str(sum(areas)))
media = sum(areas) / len(areas)
print("Média das áreas : " + str(media))

andares_de_baixo = areas_e_comodos[0:6]
print(andares_de_baixo)

andares_de_cima = areas_e_comodos [6:9]
print(andares_de_cima)

andares_de_baixo = areas_e_comodos[:6]
print(andares_de_baixo)

andares_de_cima = areas_e_comodos [6:]
print(andares_de_cima)

andares_de_cima = areas_e_comodos [-4:]
print(andares_de_cima)


anos_de_nascimento = [1973, 1956, 2001, 2011, 2017, 2016]

idades = []
for ano in anos_de_nascimento:
  idades.append(2019 - ano)
print(idades)

idades = [2019 - ano for ano in anos_de_nascimento]
print(idades)