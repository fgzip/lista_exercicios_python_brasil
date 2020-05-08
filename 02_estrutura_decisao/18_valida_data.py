'''

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Valida Data * * * *\n")

dia = int(input("\nDigite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if (dia > 0 and dia < 32) and (mes > 0 and mes < 13) and (ano > 0 and ano < 10000):
    print("\nData válida. {:0>2}/{:0>2}/{:0>4}\n".format(dia, mes, ano))
else:
    print("\nData inválida.\n")