'''

Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.
Dicas:
    - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    - Triângulo Equilátero: três lados iguais;
    - Triângulo Isósceles: quaisquer dois lados iguais;
    - Triângulo Escaleno: três lados diferentes;

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Triângulos * * * *\n")

lado_1 = int(input("\nDigite o valor do lado 1: "))
lado_2 = int(input("Digite o valor do lado 2: "))
lado_3 = int(input("Digite o valor do lado 3: "))

triangulo_eh_valido = False
tipo_triangulo = None

if (lado_1  + lado_2) > lado_3 and (lado_1 + lado_3) > lado_2 and (lado_2 + lado_3) > lado_1:
    triangulo_eh_valido = True

if triangulo_eh_valido:
    if lado_1 == lado_2 and lado_2 == lado_3:
        tipo_triangulo = "Equilátero"
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        tipo_triangulo = "Escaleno"
    else:
        tipo_triangulo = "Isósceles"

    print("\nTriângulo válido.")
    print("Tipo do triângulo: {}\n".format(tipo_triangulo))

else:
    print("\nTriângulo inválido.\n")
