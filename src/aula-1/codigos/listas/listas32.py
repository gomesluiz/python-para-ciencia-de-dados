carros  = ['audi', 'bmw', 'subaru', 'toyota']
pedidos = ['bmw', 'ferrari']
for pedido in pedidos:
  if pedido in carros:
    print("Requisitanto " + pedido.title() + ".")
  else:
    print("Infelizmente, nao temos " + pedido.upper() + "!")

print("\nO processamento de pedidos foi finalizado!")

# output: Requisitando Bmw.
#         Infelizmente, nao temos FERRARI
#
#   O processamento de pedidos foi finalizadoS
