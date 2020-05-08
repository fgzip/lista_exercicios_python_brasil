'''

As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os
reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
    - salários até R$ 280,00 (incluindo) : aumento de 20%
    - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    - o salário antes do reajuste;
    - o percentual de aumento aplicado;
    - o valor do aumento;
    - o novo salário, após o aumento.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Aumento de Salários * * * *\n")

salario = int(input("\nDigite o salário atual: "))
aumento = 0

if salario <= 280:
    aumento = 20    

elif salario > 280 and salario < 700:
    aumento = 15

elif salario >= 700 and salario < 1500:
    aumento = 10

elif salario >= 1500:
    aumento = 5

aumento_total = salario * (aumento / 100)
salario_final = salario + aumento_total

print("\nSalário inicial: R${:.2f}".format(salario))
print("Percentual de aumento: {}%".format(aumento))
print("Aumento: R${:.2f}".format(aumento_total))
print("Salário final: R${:.2f}\n".format(salario_final))
