'''

Faça um Programa que converta metros para centímetros.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 05.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * * metrosCENTIMETROS * * * * *\n")

met = float(input("\nDigite a quantidade em metros: "))
cent = met * 100

print("\n{:.2f}m = {}cm\n".format(met, cent))
