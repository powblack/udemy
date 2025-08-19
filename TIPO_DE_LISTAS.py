"""
string sao caracteres, ou seja, uma sequencia de caracteres
com indices, ou seja, cada caracter tem um indice.

tipo de lista  = mutáveis

forma mais comum de criar uma lista é:
lista = [1, 2, 3, 4, 5] - usando colchetes
outra forma de criar uma lista é:
lista = list(range(1, 6)) - usando a função list()



"""
import os

os.system('cls' if os.name == 'nt' else 'clear')  # limpa o terminal

lista = [1, 2, 3, 4, 5]  # criando uma lista com colchetes

print(lista)  # imprime a lista completa


lista.append(1)  # adiciona o elemento 1 no final da lista


print(lista)  # imprime a lista completa após adicionar o elemento


lista.pop()  # remove o último elemento da lista
print(lista)  # imprime a lista completa após remover o último elemento


lista.clear()  # remove todos os elementos da lista
print(lista)  # imprime a lista completa após limpar todos os elementos

"""
-----------------------------------------------------------------


insert - insere um elemento em um índice específico
append - adiciona um elemento no final da lista
pop - remove o último elemento da lista
clear - remove todos os elementos da lista
extend - adiciona vários elementos no final da lista
del - remove um elemento específico da lista
remove - remove o primeiro elemento encontrado com o valor especificado


-----------------------------------------------------------------

cuidados com dados mutuáveis, como listas, dicionários e conjuntos,




exercicios 

exibir os indices da lista 

"""


lista = ['a', 'b', 'c', 'd', 'e']  # criando uma lista de letras
indices = range(len(lista))  # criando uma lista de índices

for indice in indices:  # iterando sobre os índices
    print(f'Índice: {indice}, Valor: {lista[indice]}')  # imprimindo o índice e o valor correspondente

"""
TUPLAS SÃO IMUTAVEIS, OU SEJA, NÃO PODEM SER ALTERADAS
AS LISTAS SÃO MUTÁVEIS, OU SEJA, PODEM SER ALTERADAS

E SÃO MAIS RÁPIDAS AS TUPLAS, POIS NÃO PRECISAM
ATUALIZAR OS ÍNDICES DOS ELEMENTOS SEGUIDOS.


"""

#ENUMERATE É UMA FUNÇÃO QUE RETORNA UM OBJETO ITERÁVEL
#QUE CONTÉM PARES DE ÍNDICES E VALORES DE UMA LISTA OU

lista = ['a', 'b', 'c', 'd', 'e']  # criando uma lista de letras

#lista.append('f')  # adicionando o elemento 'f' no final da lista

lista_enumerada = enumerate(lista)  # enumerando a lista

print(lista)
print(lista_enumerada)

for item in lista_enumerada:  # iterando sobre a lista enumerada
    print(item)  # imprimindo o item (índice, valor)

"""
o intereitor (enumerate) retorna um objeto iterável, porem usando 
na variavel antes das funções ou operações, ele é consumido 
pelo primeiro loop, ou seja, não pode ser usado novamente
ou seja, usar o interator direto na função.
veja o exemplo abaixo:

"""

lista = ['a', 'b', 'c', 'd', 'e']  # criando uma lista de letras


#for item in enumerate(lista):  # iterando sobre a lista enumerada
 #   print(item)  # imprimindo o item (índice, valor)

for item in lista:
    print(item)  # imprimindo o item (valor) da lista