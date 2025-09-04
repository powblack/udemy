"""


argumento nomeado tem nome com sinal de igual

argumento não nomeado recebe apenas o argumento (valor) posicional


Quando falamos em argumentos, estamos falando sobre os valores passados para as funções no ato da sua execução. 
Existem argumentos nomeados e argumentos posicionais.

Argumentos nomeados recebem o nome do parâmetro antes do valor, 
argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem.


"""

def soma(x, y):
    print(f'{x=} y={y}') # mostra o valor sendo nomeado


print(soma(1, 2))


"""
para eu definir um parametro que tenha por padrao sem valor,
devo fazer assim para o parametro Z,abaixo:

def soma (x, y, z=None) isso faz com que o parametro Z tenha declarado algum sem valor
    if z is not None: se valor de Z continuar sem valor, for None, ele é True, falso seria se tivesse um valor
        print(x, y, z)
    
        else:
        print(x, y)

soma(1, 2) passando valores somente para x e y

        
outro exemplo

def numero(x, y=None, z) dessa forma está incorreta, pois é necessario passar um valor na sequencia do que ja foi dado.

forma correta

def numero()x, y=None, z=None)


escopo da função


def escopo():  |    
    x = 1      |   esse é o bloco da função, ela não altera em nada for dela
    print(x)   |

    
escopo()
print(x) esse x não foi declarado, logo dará erro, no pois é uma variavel que não existe

porem se eu declarar a variavel X for do escopo da função, a função lê essa variavel e pega seu valor, 
mas do escopo da função nenhum codigo externo lê a variavel dentro dela.

porem para eu não permitir que a função pegue o valor da variavel fora da função com o mesmo nome, 
bastar declarar novamente dentro da função, pois ela prioriza o valor dentro dela.

exemplo:

x = 1 variavel fora

def funcao(): 
    x = 10 variavel dentro
    print(x)

    
funcao() vai mostrar o valor de X de dentro da funcao que é 10

print(x) vai mostrar o valor de X de fora da funcao que é 1

"""
