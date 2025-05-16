# Operadores in e not in
# strings sao iteraveis
# a posicao é marcado por indice
#exemplo
# 0 1 2 3
# n o m e

# no comando abaixo eu consiguo imprimir somente o valor num indice


nome = 'jonathan'

# no nome jonathan o indice é
#0 1 2 3 4 5 6 7
#j o n a t h a n

print(nome[2]) # nesse comando eu imprimo o indice 2 que é na ordem a letra n


# lista com 3 nomes
#ordem 0 1 2

nomes = 'joao', 'maria', 'pedro'

#nesse comando eu imprimo somente o indice 2

print(nomes[2])

#teste de busca intens

produtos = '', 'arroz', 'feijao', 'farinha'

print("Digite 1 para arroz, 2 para feijao, 3 para farinha")
produto = input("Qual produto voce quer? ")
escolha = int(produto)

print("Tome seu produto: ", produtos[escolha])

#Agora temos usando o in

#Codigo que verifica dentro da lista ou dados armazenados
#os itens ou nomes de cidades cadastradas

cidades = 'cariacica', 'vitoria', 'vila velha'
print("Vamos verificar a viabilidade...")
escolha2 = input("Qual sua cidade? ")

if escolha2 in cidades:
    print("Que legal, temos viabilidade para sua cidade!!")

else:
    print("Infelismente não podemos te ajudar no momento!!!")