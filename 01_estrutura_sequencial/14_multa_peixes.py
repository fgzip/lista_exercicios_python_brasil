'''

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça
um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável
multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 06.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * P E I X E S * * * *\n")

multa = 0
peso_pescado = int(input("Digite o peso do pescado do dia: "))

if peso_pescado > 50:
    excesso = peso_pescado - 50
    multa = 4 * excesso
    print("\nMulta!\nExcesso de: {}kg\nValor: R${:.2f}\n".format(excesso, multa))
else:
    print("\nSem multa. Parabéns!")
