'''

Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a 
letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * GENEROS * * * *\n")

sexo = input("\nDigite o sexo [M, F ou N]: ")

if sexo.upper() == "M":
    print("\nSexo masculino.\n")
elif sexo.upper() == "F":
    print("\nSexo feminino.\n")
elif sexo.upper() == "N":
    print("\nNão binário.\n")
else:
    print("\nInválido.\n")