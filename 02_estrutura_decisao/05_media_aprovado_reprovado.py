'''

Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
    - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    - A mensagem "Reprovado", se a média for menor do que sete;
    - A mensagem "Aprovado com Distinção", se a média for igual a dez.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * NOTAS * * * *\n")

nota_1 = float(input("\nDigite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

print("\nMédia: {:.1f}".format(media))

if media == 10:
    print("\nAprovado com distinção.\n")
elif media < 10 and media >= 7:
    print("\nAprovado.\n")
elif media < 7 and media >= 0:
    print("\nReprovado.\n")
else:
    print("\nErro.\n")