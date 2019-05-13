def processa_contas(nao_processada, processada):
    """
    Simula um processamento de uma fila, ate que nao haja mais nenhum
    Transfere cada elemento para a fila de processados.
    """
    
    while nao_processada:
      conta = nao_processada.pop()
      # simula a processamento de uma conta.
      if conta not in processada:
        print("Processando conta: " + conta)
        processada.append(conta)

def mostra_contas_processadas(processadas):
  """ Mostra as contas processadas """
  print("\nAs seguintes contas foram processadas:")
  for processada in processadas:
    print(processada)

contas_nao_processadas  = ['301', '407', '603', '502', '407', '502']
contas_processadas      = []

processa_contas(contas_nao_processadas, contas_processadas)
mostra_contas_processadas(contas_processadas)
# output:
# Processando conta: 502
# Processando conta: 407
# Processando conta: 603
# Processando conta: 301
#
# As seguintes contas foram processadas:
# 502
# 407
# 603
# 301