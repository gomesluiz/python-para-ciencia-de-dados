def monta_pais(nome, capital, populacao=0):
    """
    Devolve um dicionario com informacoes de um pais 
    """
    pais = {'nome': nome, 'capital': capital}
    
    if populacao > 0:
      pais['populacao'] = populacao

    return pais 

um_pais = monta_pais("Argentina", "Buenos Aires")
print(um_pais)
outro_pais = monta_pais("Brasil", "Brasilia", 207)
print(outro_pais)
# output:
# {'capital': 'Buenos Aires', 'nome': 'Argentina'}
# {'capital': 'Brasilia', 'nome': 'Brasil', populacao: 207}