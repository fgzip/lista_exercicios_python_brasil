'''

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 05.05.2020

x------------------------------------------------------------------------------x

'''

import math

print("\n* * * ÁREA DO CÍRCULO * * *\n")

raio = int(input("\nDigite o raio: "))

area_circulo = math.pi * (raio ** 2)

print("\nÁrea do círculo: {:.2f}\n".format(area_circulo))
