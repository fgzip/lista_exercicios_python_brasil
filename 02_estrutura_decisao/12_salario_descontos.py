'''

Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de
horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Descontos no Salário * * * *\n")

valor_hora = int(input("\nDigite o salário por hora: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))

salario_total = valor_hora * horas_trabalhadas
salario_final = 0

ir = 0
desconto_ir = 0
desconto_inss = (10/100) * salario_total
desconto_sindicato = (3/100) * salario_total
fgts = (11/100) * salario_total

if salario_total <= 900:
    salario_final = salario_total - desconto_inss - desconto_sindicato

elif salario_total > 900 and salario_total <= 1500:
    ir = 5
    desconto_ir = (5/100) * salario_total
    salario_final = salario_total - desconto_inss - desconto_sindicato - desconto_ir

elif salario_total > 1500 and salario_total <= 2500:
    ir = 10
    desconto_ir = (10/100) * salario_total
    salario_final = salario_total - desconto_inss - desconto_sindicato - desconto_ir

elif salario_total > 2500:
    ir = 20
    desconto_ir = (20/100) * salario_total
    salario_final = salario_total - desconto_inss - desconto_sindicato - desconto_ir

print("\n\nSalário bruto: R${:.2f}".format(salario_total))
print("(-) IR ({}%): R${:.2f}".format(ir, desconto_ir))
print("(-) INSS (10%): R${:.2f}".format(desconto_inss))
print("(-) Desconto sindicato (3%): R${:.2f}".format(desconto_sindicato))
print("FGTS (11%): R${:.2f}".format(fgts))
print("Total de descontos: R${:.2f}".format(desconto_ir + desconto_inss + desconto_sindicato))
print("Salário final: R${:.2f}\n".format(salario_final))
