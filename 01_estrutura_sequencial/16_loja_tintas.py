'''

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 06.05.2020

x------------------------------------------------------------------------------x

'''

import math

print("\n* * * * * LOJA DE TINTAS * * * * *\n")

tamanho = int(input("\nDigite a área a ser pintada: "))

# quantos litros serão necessários
res = math.ceil(tamanho / 3)

# quantas latas serão necessárias
latas = math.ceil(res/18)

print("\nLitros necessários: {:.1f}".format(res))
print("Latas necessárias: {}\n".format(latas))
