'''

Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito 
for D ou E.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * MÉDIAS * * * *\n")

nota_1 = int(input("\nDigite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2
conceito = None
passou = None

if media >= 9 and media <= 10:
    conceito = "A"
    passou = "Aprovado"
elif media >= 7.5 and media < 9:
    conceito = "B"
    passou = "Aprovado"
elif media >= 6 and media < 7.5:
    conceito = "C"
    passou = "Aprovado"
elif media >= 4 and media < 6:
    conceito = "D"
    passou = "Reprovado"
elif media < 4 and media >= 0:
    conceito = "E"
    passou= "Reprovado"

print("\nMédia: {:.1f}".format(media))
print("Conceito: {}".format(conceito))
print("Aluno - {}\n".format(passou))