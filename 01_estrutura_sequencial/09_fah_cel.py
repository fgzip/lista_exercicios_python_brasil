'''

Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre
a temperatura em graus Celsius. -> C = (5 * (F-32) / 9).

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 05.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Conversor de Temperatura * * * *\n")

fah = float(input("\nDigite a temperatura em °F: "))
cel = (5 * (fah - 32) / 9)

print("\n* * * {:.1f}°F = {:.1f}°C * * *".format(fah, cel))
