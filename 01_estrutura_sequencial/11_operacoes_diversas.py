'''

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 06.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * * NÚMEROS * * * * *\n")

n1 = int(input("\nDigite o primeiro número [inteiro]: "))
n2 = int(input("Digite o segundo número [inteiro]: "))
n3 = float(input("Digite o terceiro número [real]: "))

res_a = (n1 * 2) * (n2 / 2)
res_b = (n1 * 3) + n3
res_c = (n3 ** 3)

print("\n\n* * * * RESULTADOS * * * *\n\n")

print("a. Produto do dobro do primeiro com a metade do segundo: {:.2f}".format(res_a))
print("b. Soma do triplo do primeiro com o terceiro: {:.2f}".format(res_b))
print("c. Terceiro elevado ao cubo: {:.2f}\n".format(res_c))
