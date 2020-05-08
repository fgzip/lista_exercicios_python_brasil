'''

Faça um Programa que peça dois números e imprima o maior deles

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * MAIOR DE DOIS NÚMEROS * * * *\n")

num_1 = int(input("\nDigite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

if num_1 > num_2:
    print("\n{} é o maior.\n".format(num_1))
elif num_2 > num_1:
    print("\n{} é o maior.\n".format(num_2))
else:
    print("\nNúmeros iguais.\n")