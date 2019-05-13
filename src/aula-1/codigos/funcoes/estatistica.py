def calcula_media(numeros):
    """
    Retorna a media de numeros em uma lista.
    """
    quantidade  = len(numeros)
    if quantidade == 0:
      return 0

    total = 0
    for numero in numeros:
        total += numero

    return total / quantidade 