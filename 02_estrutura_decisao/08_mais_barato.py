'''
Faça um programa que pergunte o preço de três produtos e informe qual produto 
você deve comprar, sabendo que a decisão é sempre pelo mais barato.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * PRODUTO MAIS BARATO * * * *\n")

p1 = int(input("\nDigite o valor do primeiro produto: "))
p2 = int(input("Digite o valor do segundo produto: "))
p3 = int(input("Digite o valor do terceiro produto: "))

if p1 < p2 and p1 < p3:
    print("\nVocê deve comprar o primeiro produto.\n")
elif p2 < p1 and p2 < p3:
    print("\nVocê deve comprar o segundo produto.\n")
elif p3 < p1 and p3 < p2:
    print("\nVocê deve comprar o terceiro produto.\n")