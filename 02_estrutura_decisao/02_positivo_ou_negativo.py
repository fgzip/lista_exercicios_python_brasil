'''

Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * POSITIVO OU NEGATIVO * * * *\n")

numero = int(input("\nDigite um número: "))

if numero >= 0:
    print("\n{} é positivo\n".format(numero))
else:
    print("\n{} é negativo.\n".format(numero))