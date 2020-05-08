'''

Faça um programa que leia três números e mostre o maior e o menor deles.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

maior = None
menor = None

print("\n* * * * MAIOR E MENOR DE TRÊS NÚMEROS * * * *")

n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print("\nMaior: {}\nMenor: {}\n".format(maior, menor))