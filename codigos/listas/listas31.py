carros = []
if carros:
  for carro in carros:
    if carro == 'bmw':
      print(carro.upper())
    else:
      print(carro.title())
else:
  print("O estoque de carros esta vazio!")

# output: O estoque de carros esta vazio!
