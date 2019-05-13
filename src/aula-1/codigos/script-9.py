idade = int(input("Entre com sua idade : "))
if idade < 2:
  print("Voce e um bebe")
elif idade < 4:
  print("Voce e uma crianca")
elif idade < 13:
  print("Voce e um garoto(a)")
elif idade < 20:
  print("Voce e um(a) adolescente")
elif idade < 65:
  print("Voce e um adulto")
else:
  print("Voce e um idoso")
