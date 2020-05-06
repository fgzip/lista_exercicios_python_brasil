'''

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 06.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * * SALÁRIO * * * * *\n")

ganho_por_hora = float(input("\nDigite o seu salário por hora: "))
numero_de_horas = int(input("Digite o total de horas trabalhadas: "))

salario_total = ganho_por_hora * numero_de_horas

desconto_ir = salario_total * (11/100)
desconto_inss = salario_total * (8/100)
desconto_sind = salario_total * (5/100)

salario_final = salario_total - desconto_ir - desconto_inss - desconto_sind

print("""

Salário bruto: R${:.2f}

- IR (11%): R${:.2f}
- INSS (8%): R${:.2f}
- Sindicato: R${:.2f}

Salário líquido: R${:.2f}

""".format(salario_total, desconto_ir, desconto_inss, desconto_sind, salario_final))
