# retorno de valores (return)

"""
as funções no python sem o uso do return, todas as operações dentro 
da função def retornam valor None.

expemplo:

def soma(x, y):
    print(x + y)


soma(1, 2)

output:  

"""
def soma(x, y):
    print(x + y) # o print somente exibi o valor, ele não faz nenhum calculo


variavel = soma(1, 2) # dessa forma estou criando uma variavel com o valor da soma em def
print("Print 1 ", variavel) # exibindo o resultado da variavel

print("------------")

# porem o resultado é None, quer dizer que a função def não está retornando nenhum valor,
# somente exibindo uma operação de dentro dela.
# ou seja, para que eu possa usar esse valor ou gere um valor real, devo usar o return.
# veja abaixo:

def soma2(x, y):
    return x + y # retorna o valor para fora da funcao

variavel1 = soma2(1, 2) # declare a variavel e passe os valores chamando a funcao, assim ele pega o valor do return
print(variavel1)

variavel2 = soma2(3, 4)

print(variavel2)

variavel3 = variavel1 + variavel2

print(variavel3)


