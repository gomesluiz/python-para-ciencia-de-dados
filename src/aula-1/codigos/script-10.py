usuarios_correntes = ['joao', 'maria', 'pedro', 'ana', 'jose']
usuarios_novos = ['luiz', 'gabriel', 'Pedro', 'ana']
usuarios_repetidos = []

for usuario_novo in usuarios_novos:
  if usuario_novo.lower() in usuarios_correntes:
    usuarios_repetidos.append(usuario_novo)
    print("Usuario " + usuario_novo + " nao esta disponivel!")
  else:
    print("Usuario " + usuario_novo + " esta disponivel!")

print(usuarios_repetidos)