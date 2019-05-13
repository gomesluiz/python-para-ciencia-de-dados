# -*- coding: utf-8 -*-
saldo = input("Entre com seu saldo : ")
taxa  = input("Entre com a taxa de correção: ")
anos  = input("Entre com a quantidade de anos: ")
saldo = float(saldo)
taxa  = float(taxa)
anos  = int(anos)
saldo_final = saldo * ((1 + taxa/100) ** anos)

print("O saldo final e de " + str(round(saldo_final,2)))