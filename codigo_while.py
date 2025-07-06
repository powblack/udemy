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

max_linhas = input("Qual o Maximo de fichas? ")
linha = 0

linhas = int(max_linhas)

while linha < linhas:
    linha += 1
    print(f"{linha}-_____________")

print("            ")
print("Seu Formulario foi gerado !!!")



