'''

Faça um Programa que peça um número correspondente a um determinado ano e em 
seguida informe se este ano é ou não bissexto.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Ano Bissexto * * * *\n")

ano = int(input("\nDigite o ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\n{} é bissexto.\n".format(ano))
else:
    print("\n{} não é bissexto.\n".format(ano))