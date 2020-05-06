'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
    e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
    ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    - comprar apenas latas de 18 litros;
    - comprar apenas galões de 3,6 litros;
    - misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 06.05.2020

x------------------------------------------------------------------------------x

'''

import math

print("\n* * * * * LOJA DE TINTAS II * * * * *\n")

area = int(input("\nDigite a área: "))

# quantos litros serão necessários
litros = math.ceil(area/6)
print("\nLitros necessários: {:.1f}\n".format(litros))

# lata de 18 litros
lata_18 = math.ceil(litros/18)
preco_18 = lata_18 * 80
print("\nLatas de 18 litros\nQuantidade necessária: {}\nPreço total: R${:.2f}\n".format(lata_18, preco_18))


# galão de 3.6 litros
galao_36 = math.ceil(litros/3.6)
preco_36 = galao_36 * 25
print("\nGalões de 3.6 litros\nQuantidade necessária: {}\nPreço total: R${:.2f}\n".format(galao_36, preco_36))


# misturado
litros_mistura = litros * 1.1
print("Litros +10%: {}".format(math.ceil(litros_mistura)))

if litros_mistura < 18:
    qtd_36_mistura = math.ceil(litros_mistura % 3.6)
    print("\nEconomia misturando...\nQuantidade de latas de 18: 0\nQuantidade de galões de 3.6: {}".format(qtd_36_mistura))
    print("Valor total: R${:.2f}".format(qtd_36_mistura * 25))
elif litros_mistura > 18:
    print("\nEconomia misturando...\n")
    latas_de_18 = math.floor(litros_mistura / 18)
    print("Latas de 18: {}".format(latas_de_18))

    resto_18 = math.ceil(litros_mistura % 18)

    galao_de_36 = math.ceil(resto_18 / 3.6)
    print("Galões de 3.6: {}".format(galao_de_36))
