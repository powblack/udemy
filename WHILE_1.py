"""
repitições

while

----------------

condicao = True

while condicao:
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome} seja Bem vindo!")

    if nome == 'sair':
        break

break: comando para parar o programa.
----------------

contador = 1

while contador <= 10:
    print(contador)
    contador = contador + 1

print('Acabou')

-----------------
formas mais simples e mais profissional:


OPERADORES DE ATRIBUIÇÃO

=
+= SOMA OU CONCATENAÇÃO
-= SUBTRAÇÃO
*= MULTIPLICAÇÃO
/= DIVISÃO
//= DIVISÃO INTEIRA: RETORNA VALOR INTEIRO OU REDONDO
**= POTENCIAÇÃO
%= MODULO, É O RESTO DA DIVISÃO DE NUMEROS INPARES


ex: contador = contador + 1 # nesse codigo, faz a soma de + 1 com a variavel contador.

contador += 1 # é a mesma operação acima, pois mais curta e limpa

obs: essa operação funciona com string tambem
porem com string é CONCATENAÇÃO, ou seja, ele junta as strings



--------------

comando BREAK, na linha que estiver, vai parar o codigo, vai quebrar os comandos seguintes

no caso de eu quizer pular:

comando: continue

"""

""" contador = 0
barra = "/"

while contador <= 100:

    
    print(f"Donwload: {barra}{contador}%")
    contador += 10
    barra += "/"
    

print("Download was a sucessfull")

 """

""" max_linhas = input("Qual o Maximo de fichas? ")
linha = 0

linhas = int(max_linhas)

while linha < linhas:
    linha += 1
    print(f"{linha}-_____________")

print("            ")
print("Seu Formulario foi gerado !!!")

 """

# INTERANDO STRINGS COM WHILE

# nome = "Jonathan_"

# tamanho_nome = len(nome) # retorna quantidade de caracteres em numero inteiro

# contador = 0
# contadorint = int(contador)


# while contador < tamanho_nome:
#     if ' ' in nome or '_' in nome:
#         print('digite somente o primeiro nome !!!')
#         break

#     print(nome[contador])
#     contador += 1

# print(f'Seu nome tem {tamanho_nome} letras')

# -------------------------------------------------------

nome = input("Qual o seu nome? ")


indice = 0 # comando pega a string na posição de acordo com o numero
nome_na_vertical = '' # variavel para mostrar o print do nome sendo digitado na vertical

"""
Na função abaixo, o WHILE vai pegar o valor da variavel INDICE e vai
imprimir na tela essa string, e na variavel NOME_NA_VERTICAL, vai
concatenar com a string vazia no inicio do codigo, logo em seguida
continuará concatenando ate acabar a string toda, e imprimindo na vertical
como se estivesse digitando, isso acontece por conta somente da
CONCATENIZAÇÃO!!!

A variavel letra dentro do bloco da funcao WHILE, só é lida dentro do
bloco, e esta pegando a string no indice gerado e fazendo a concatenação
com a variavel NOME_NA_VERTICAL.

"""

while indice < len(nome):
    letra = nome[indice] #variavel pega a string no indice gerado 
    nome_na_vertical += letra #variavel faz a concatenação com a variavel LETRA
    indice += 1

print(nome_na_vertical)

