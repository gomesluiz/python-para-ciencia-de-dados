# -*- coding: utf-8 -*-
altura = input("Entre com a sua altura: ")
peso   = input("Entre com o seu peso: ")
altura = float(altura)
peso   = float(peso)
imc = peso / (altura * altura)    

print("O seu imc e igual a " + str(round(imc,2)))