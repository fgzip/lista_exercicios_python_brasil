'''

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
    - Para homens: (72.7*h) - 58
    - Para mulheres: (62.1*h) - 44.7

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 06.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * PesoIdeaL * * *\n")

altura = float(input("\nDigite a sua altura: "))

peso_homens = (72.7 * altura) - 58
peso_mulheres = (62.1 * altura) - 44.7

print("\nPeso ideal para homens: {:.1f}kg".format(peso_homens))
print("Peso ideal para mulheres: {:.1f}kg\n".format(peso_mulheres))
