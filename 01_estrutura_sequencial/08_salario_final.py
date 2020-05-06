'''

Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 05.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * * SALÁRIO FINAL * * * * *\n")

ganho_hora = float(input("Digite quanto o funcionário ganha por hora trabalhada: "))
horas_trabalhadas = int(input("Digite quantas horas o funcionário trabalhou: "))

salario_final = ganho_hora * horas_trabalhadas

print("\n* * * * Salário final: R$ {:.2f} * * * *\n".format(salario_final))
