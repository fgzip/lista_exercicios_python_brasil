'''

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 05.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Conversor de Temperatura II * * * *\n")

cel = float(input("Digite a temperatura em °C: "))
fah = (cel * 1.8) + 32

print("\n* * * {:.1f}°C = {:.1f}°F * * *\n".format(cel, fah))
