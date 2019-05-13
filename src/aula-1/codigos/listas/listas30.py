ano = 1998
if ano < 1980:
  imposto = 0
elif ano < 1990:
  imposto = 5
elif ano < 2000:
  imposto = 10 
elif ano < 2010:
  imposto = 15
else:
  imposto = 20
print("O valor do imposto e " + str(imposto) + ".")
# output: O valor do imposto e 10.

