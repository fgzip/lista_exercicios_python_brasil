'''

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 05.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Dobro da Área * * * *\n")

lado = float(input("\nDigite o valor do lado: "))
area = lado ** 2

print("\nO dobro da área é: {:.1f}\n".format(area * 2))
