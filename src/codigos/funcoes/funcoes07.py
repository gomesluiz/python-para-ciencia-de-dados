def calcula_media(numeros):
    """
    Devolve a media de numeros em uma lista.
    """
    
    quantidade  = len(numeros)
    if quantidade == 0:
      return 0

    total = 0
    for numero in numeros:
        total += numero

    return total / quantidade 

calcula_media([3, 4, 6, 5, 4, 2])
print("A media e igual a " + str(calcula_media([3, 4, 8, 5, 4])))
# output:
# A media e igual a 4