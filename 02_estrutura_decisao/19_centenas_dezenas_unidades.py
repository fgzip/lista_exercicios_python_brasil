'''

Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades 
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 
    11, 1, 7 e 16

x------------------------------------------------------------------------------x

Fonte: Lista de Exercícios PythonBrasil
Estrutura de Decisão
Data: 08.05.2020

x------------------------------------------------------------------------------x

'''

print("\n* * * * Centenas, dezenas e unidades * * * *\n")

imprime_centena = ""
imprime_dezena = ""
imprime_unidade = ""

tem_centena = False
tem_dezena = False
tem_unidade = False

numero = int(input("\nDigite um número: "))

unidade = numero % 10
if unidade > 0:
    tem_unidade = True

#   elimina a unidade do número
numero = (numero - unidade) / 10

#   extraindo a dezena
dezena = numero % 10

#   elimina a dezena do número original, fica a centena
numero = (numero - dezena) / 10
centena = numero

#   transforma em inteiros
dezena = int(dezena)
if dezena > 0:
    tem_dezena = True
    
centena = int(centena)
if centena > 0:
    tem_centena = True


def verifica_centena(cent):
    if cent > 1:
        return "{} centenas".format(cent)
    else:
        return "{} centena".format(cent)

def verifica_dezena(dez):
    if dez > 1:
        return "{} dezenas".format(dez)
    else:
        return "{} dezena".format(dez)

def verifica_unidade(uni):
    if uni > 1:
        return "{} unidades".format(uni)
    else:
        return "{} unidade".format(uni)

cents = verifica_centena(centena)
dezs = verifica_dezena(dezena)
uns = verifica_unidade(unidade)


if tem_centena:
    if not tem_dezena and not tem_unidade:
        print("\n{}\n".format(cents))
    elif tem_dezena and not tem_unidade:
        print("\n{} e {}\n".format(cents, dezs))
    elif not tem_dezena and tem_unidade:
        print("\n{} e {}\n".format(cents, uns))
    elif tem_dezena and tem_unidade:
        print("\n{}, {} e {}\n".format(cents, dezs, uns))

elif not tem_centena:
    if tem_dezena and not tem_unidade:
        print("\n{}\n".format(dezs))
    elif tem_dezena and tem_unidade:
        print("\n{} e {}\n".format(dezs, uns))
    elif not tem_dezena and tem_unidade:
        print("\n{}\n".format(uns))