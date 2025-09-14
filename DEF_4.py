"""
args - Argumentos nõ nomeados

* - *args (empacotamento e desempacotamento)


lembrar do desempacotamento

"""

x, y, *resto = 1, 2, 3, 4, 5 # tupla, com numeros, porem só declarei x e y, o *resto, pega todos os valores
                             # restantes e monta uma lista para exibir no print
                             # como se fosse um pacote mesmo
                         
print(x, y, resto)


def soma(*args): #dessa forma o *args pega todos os valores que foi chamado nessa função e cria uma lista(tupla)
    print(args)

soma(1, 2, 3, 4, 5, 6, 7, 8, 9)

# dessa forma assim acima consiguo mandar varios dados para o def

# outra forma, porem eu consiguo alterar algum na lista é converter a tupla gerada 
# pelo *args, em list

def soma2(*args):
    for n in args:
        print(n)


soma2(10, 20, 30, 40, 50)


#usando o for com o def e args

def numeros(*args):
    total = 0
    for numero in args:
        print(f'{total} + {numero}')
        total = total + numero
        print(f'total ', total)

numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#forma reduzida 

def numeros2(*args):
    total = 0
    for numero in args:
        total += numero
    return total #com return ele joga esse valor para fora da função, para que eu consigua fazer outros calculos com ela

#posso pegar o valor de return da função e jogar numa variável e usar ela, veja abaixo:

soma_numeros = numeros2(10, 20, 30, 40, 50, 60)

print(f"\n Resultado do Return da função: {soma_numeros}\n")


#outra forma de fazer a soma é usa a função "sum"

digitos = 1, 2, 3, 4, 5, 6
digitos_sum = sum(digitos)
print(digitos_sum)

#também podemos usar variáveis para adicionar na função, porem tem alguns detalhes

def digitos1(*args): #o args ele empacota tudo que foi enviado para a função
    print(args) # os valores imprimidos que foram enviados para a funçao 

#vemos que se dermos um print na variavel dessa forma abaixo, é uma lista, porem uma tupla
# se mandarmos para dentro da função essa tupla, ela cria outra tupla, ou seja, vira uma tupla dentro da outra
# para corrigir isso, devemos desenpacotar os dados, para serrem livres para tratar-los melhores.

print(f"\n -------------------------------- \n")

digitos2 = 1, 2, 3, 4, 5, 6 
print(f"Lista empacotada: {digitos2}")
print(f"Lista desempacotada: ", *digitos2) # o * ele desenpacota os dados


print(f"\n -------------------------------- \n")

