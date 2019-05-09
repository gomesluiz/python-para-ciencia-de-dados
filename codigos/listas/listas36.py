figura = {'x': 0, 'y': 25, 'velocidade': 'media'}
print("x original: " + str(figura['x']))

# move a figura para direita
# determina a distancia que a figura deve se descolocar 
# de acordo com sua velocidade atual.
if figura['velocidade'] == 'baixa':
  incremento_x = 1
elif figura['velocidade'] == 'media':
  incremento_x = 2 
else:
  incremento_x = 3

# a nova posicao e a posicao antiga somada ao incremento
figura['x'] = figura['x'] + incremento_x 

print("x incrementado: " + str(figura['x']))

