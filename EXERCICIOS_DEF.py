"""
EXERCICIO COM FUNÇÃO

crie uma função que multiplica todos os argumentos 
não nomeados recebidos
retorne o total apra uma variavel e mostre o valor
da variavel.

crie uma função fala se um numero é par ou impar

retorne se o numero é par ou impar

"""
def multplicacao(*args):

    soma = 1

    for numero in args:
        soma *= numero

    return soma


multiplicar = multplicacao(1, 2 ,3, 4)

print(multiplicar)

# ---------------------------------------------------------------------------

def par_impar(x):
    resto = x % 2
    if resto == 0:
        return print("PAR")
    
    else:
        return print("IMPAR")
    

"""
Forma mais reduzida de escrever o codigo de impar ou par

def par_impar(numero):
    return numero % 2 == 0

retorna Tru ou False

-------------------------------------

def par_impar(numero):
    multiplo = numero % 2 == 0
    
    if multiplo:
        return "par"

    else:
        return "impar"

"""

while True:
    digito = input("Digite um numero:  ")
    
    if digito == "sair" or digito == "quit":
        break

    else: 

        try:
            digito = int(digito)
            par_impar(digito)
        except:
            print("Digite so numeros seu besta !!!")
