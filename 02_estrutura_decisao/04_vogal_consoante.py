'''

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 07.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * VOGAL OU CONSOANTE * * * *\n")

vogais = [ 'a', 'e', 'i', 'o', 'u' ]
letra = input("\nDigite uma letra: ")

if letra.lower() in vogais:
    print("\n'{}' é uma vogal.\n".format(letra))
else:
    print("\n'{}' é uma consoante.\n".format(letra))