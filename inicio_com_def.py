"""
introdução às funções (def) em python
funções são trechos de código usados para 
replicar determinada ação ao longo do seu codigo
e retornar um valor específico.

por padrao as funções retornam valor= none


creating functions allows you to write code once and reuse it in multiple locations, 
promoting efficiency and reducing redundancy in your programming. 
This not only saves time but also makes your code easier to manage and maintain.


"""

def funcao(): #nome da função, dentro de () é os parametros
    print('varias')

funcao() #chamando a funcao



def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)


def saudacao(nome = ''):
    print(f"Oi, {nome}, tudo bem? ")

def fechar(entrada = "c"):
    entrada = input("digite [S]air ou Pressicone Enter para continuar: ")
    if entrada == "s":
        print("saindo...  ")
        quit()

def opcao(escolha = 3):
    while True:
        print("Opção [1] Continuar ou [2] Sair.")
    
        try:
            escolha = int(input("Digite opção 1 ou 2, apenas numeros:  ")) 
            if escolha == 1:
                break
            if escolha == 2:
                quit()
            if escolha == 3:
                ...
        except Exception as e:
            print("Tente novamente!!!")
            continue



while True:
    nome = input("nome: ")
    saudacao(nome)
    opcao()
    
"""
More about DEF

example below:

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)

a linha resultado = numero % multiplo == 0, confere se o resto do numero pelo outro for igual a 0, essa linha de 
codigo retorna um valor boleano TRUE ou FALSE.

a linha de codigo print(f'{numero} é múltiplo de {multiplo}?', end=' '), o end=" ", faz com que o output
no terminal fique na mesma linha do print, ou seja, ele evita a quebra de linha, pois quando der um input
o valor iria para linha de baixo, com o end=" " faz com que o valor input fique na mesma linha do output.


"""