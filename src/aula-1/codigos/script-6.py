patio    = 11.25
cozinha  = 18.00
sala     = 20.00
quarto   = 10.75
banheiro = 9.50
areas = [patio, cozinha, sala, quarto, banheiro]
print(areas)
areas_e_comodos = [ "patio", patio
                   ,"cozinha", cozinha
                   , "sala", sala
                   , "quarto", quarto
                   , "banheiro", banheiro]
print(areas_e_comodos)

print("Segunda area: " + str(areas[1]))
print("Area da sala: " + str(areas[2]))
print("Ultima area:  " + str(areas[-1]))

print("Area do quarto + cozinha: " 
+ str(areas[1] + areas[3]))
areas[-1] = 10.50

areas_e_comodos[4]  = "sala de jantar"
print(areas_e_comodos)

areas.insert(0, 24.5)
areas.append(15.45)
print(areas)

del(areas_e_comodos[6])
del(areas_e_comodos[6])
print(areas_e_comodos)

comodos = [ "piscina", "patio", "cozinha"
  , "sala", "quarto", "banheiro"
  , "garagem"]

print(sorted(comodos))
print(sorted(areas))
