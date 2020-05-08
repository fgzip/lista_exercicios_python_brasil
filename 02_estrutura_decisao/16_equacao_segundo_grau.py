'''

O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao 
usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
        e o programa não deve fazer pedir os demais valores, sendo encerrado;
    - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao 
      usuário e encerre o programa;
    - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
      informe-a ao usuário;
    - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Equação de Segundo Grau * * * *\n")

import math

a = int(input("\nDigite o valor de a: "))

if a == 0:
    print("\nA equação não é de segundo grau.\nFIM DO PROGRAMA.\n")
    
else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    delta = (b * b) - (4 * a * c)
    print("\nDelta: {:.1f}\n".format(delta))

    if delta < 0:
        print("\nA equação não possui raizes reais.\nFIM DO PROGRAMA.\n")
    elif delta == 0:
        x = (b * -1) / (2 * a)
        print("\nA equação só possui uma raiz real: {:.2f}\n".format(x))
    elif delta > 0:
        x_1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
        x_2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
        print("\nx' = {:.2f}".format(x_1))
        print("x'' = {:.2f}\n".format(x_2))