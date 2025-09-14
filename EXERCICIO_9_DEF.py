""" 
funções que duplicam, triplicam e quadriplicam

"""

def duplica(numero):
    resultado = numero * 2
    return f'O dobro de {numero} é {resultado}'

def triplica(numero):
    resultado = numero * 3
    return f'O Triplo de {numero} é {resultado}'

def quadriplica(numero):
    resultado = numero * 4
    return f'O Quadriplo de {numero} é {resultado}'


print(duplica(2))
print(triplica(2))
print(quadriplica(2))

#---------------------------------------------------------------

# OUTRA FORMA

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(10))
print(quadriplicar(10))

