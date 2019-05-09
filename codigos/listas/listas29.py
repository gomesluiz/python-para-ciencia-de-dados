carros = ['audi', 'bmw', 'subaru', 'toyota']
carro  = carros[1]
ano  = 2014
print(carro == 'bmw')    # igualdade
print(carro != 'bmw')    # diferenca
print(ano <   2014)      # menor
print(ano <=  2014)      # menor ou igual
print(ano >   2014)      # maior
print(ano >=  2014)      # maior ou igual
print(ano >= 2014 and ano <= 2018)  # conectivo E 
print(ano == 2014 or ano == 21)     # conectivo OR 
print('bmw' in carros)      # checa se esta na lista
print('bmw' not in carros)  # checa se nao esta na lista
# output:  True
#          False
#          False
#          True
#          False
#          True
#          True
#          True
#          True
#          False 