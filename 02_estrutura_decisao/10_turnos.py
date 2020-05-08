'''

Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino 
ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou 
"Boa Noite!" ou "Valor Inválido!", conforme o caso.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * TURNOS * * * *\n")

turno = input("\nDigite o seu turno [M, V ou N]: ")

if turno.upper() == "M":
    print("\nBom dia!\n")
elif turno.upper() == "V":
    print("\nBoa tarde!\n")
elif turno.upper() == "N":
    print("\nBoa noite!\n")
else:
    print("\nErro.\n")
