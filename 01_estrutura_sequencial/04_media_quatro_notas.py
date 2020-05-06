'''

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 05.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * * MÉDIA * * * * *\n")

n_1 = float(input("\nDigite a primeira nota: "))
n_2 = float(input("Digite a segunda nota: "))
n_3 = float(input("Digite a terceira nota: "))
n_4 = float(input("Digite a quarta nota: "))

media = (n_1 + n_2 + n_3 + n_4) / 4

print("\nMédia final: {:.1f}\n".format(media))
