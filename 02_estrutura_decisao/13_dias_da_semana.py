'''

Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Dias da Semana * * * *\n")

dia = int(input("\nDigite o número do dia da semana: "))

if dia == 1:
    print("\nDomingo.\n")
elif dia == 2:
    print("\nSegunda.\n")
elif dia == 3:
    print("\nTerça.\n")
elif dia == 4:
    print("\nQuarta.\n")
elif dia == 5:
    print("\nQuinta.\n")
elif dia == 6:
    print("\nSexta.\n")
elif dia == 7:
    print("\nSábado.\n")
else:
    print("\nErro.\n")