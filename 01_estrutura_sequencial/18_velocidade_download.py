'''

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download
do arquivo usando este link (em minutos).

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura Sequencial
Data: 06.05.2020

x------------------------------------------------------------------------------x

'''

import math

print("\n* * * * * DOWNLOAD * * * * *\n")

tamanho = float(input("\nDigite o tamanho do arquivo (em mb): "))
velocidade = float(input("Digite a velocidade de conexão (em mbps): "))

total_segundos = math.ceil(tamanho / velocidade)
print("Segundos necessários: {}".format(total_segundos))

minimo_minutos = math.floor(total_segundos / 60)
resto_segundos = math.ceil(total_segundos % 60)

if resto_segundos == 0:
    print("Tempo estimado: {} minuto[s]".format(minimo_minutos))
else:
    print("Tempo estimado: {}m {}s".format(minimo_minutos, resto_segundos))
