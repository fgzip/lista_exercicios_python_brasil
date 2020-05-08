'''

Faça um programa que leia três números e mostre-os em ordem decrescente.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * ORDEM DECRESCENTE * * * *\n")

n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

print()

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"\n{n1}, {n2}, {n3}\n")
    else:
        print(f"{n1}, {n3}, {n2}\n")

elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"{n2}, {n1}, {n3}\n")
    else:
        print(f"{n2}, {n3}, {n1}\n")

elif n3 > n1 and n3 > n2:
    if n1 > n2:
        print(f"{n3}, {n1}, {n2}\n")
    else:
        print(f"{n3}, {n2}, {n1}\n")