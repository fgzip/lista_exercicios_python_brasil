'''

Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 06.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * PesoIdeaL * * * *\n")

altura = float(input("Digite a altura do usuário: "))
peso_ideal = (72.7 * altura) - 58

print("\nO peso ideal seria: {:.1f}kg\n".format(peso_ideal))
