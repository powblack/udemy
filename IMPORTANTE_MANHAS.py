"""
USANDO O ... TRES PONTINHOS EM QUALQUER LUGAR
DO CODIGO, CONSIGUO DEIXAR EM ESPERA 
PARA EU EDITAR DEPOIS

EXEMPLO: print ...


"""

variavel = ...
print(variavel)
print(...)



"""
em relação a listas, a função del remove o elemento,
ter cuidado com o uso dela, pois ela não retorna nada
e poder causar lentidão no código se usada de forma inadequada.
del variavel[0]  # remove o primeiro elemento da lista

ao deletar um elemento, o índice dos elementos seguintes
será atualizado, ou seja, o elemento que estava no índice 1
agora estará no índice 0, e assim por diante.
isso causa que o código seja mais lento, pois o Python
precisa atualizar os índices de todos os elementos seguintes.


"""

"""
O USO DE _ , UNDERLINE É UMA CONVENÇÃO PARA INDICAR
QUE A VARIÁVEL É PARA USO INTERNO, NÃO DEVE SER ACESSADA
# fora do módulo ou classe onde foi definida.

EXEMPLE: 

variavel1, variavel2, _ = [1, 2, 3]  # o underscore indica que a variável não será usada
print(variavel1)  # imprime 1


o * é usado para desempacotar listas ou tuplas, como resto

"""