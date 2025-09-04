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
"""

o try e except são usados para tratar exceções
se ocorrer um erro no bloco try, o código no bloco except será executado
vantagem de usar try e except:
- evita que o programa quebre com erros inesperados
- permite que você trate erros de forma controlada
- possibilita a execução de código alternativo em caso de erro

ao invez de usar o if e else, o try e except
podem ser mais eficientes e limpos, especialmente.
 
"""

"""
USAR O COMANDO  os.system('cls') PARA LIMPAR O TERMINAL NOS LOOPs

IMPORT OS


x = 5
result = "Even" if x % 2 == 0 else "Odd"

impar o par com uma linha


"""

