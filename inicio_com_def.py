"""
introdução às funções (def) em python
funções são trechos de código usados para 
replicar determinada ação ao longo do seu codigo
e retornar um valor específico.

por padrao as funções retornam valor= none
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
    
