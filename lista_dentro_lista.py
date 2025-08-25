"""
aprendendo a manejar listas dentro de listas
procurar itens dentro de listas


"""

lista_salas = [

    ['Maria', 'Helena', 'Luiz'],  # sala 1
    ['João', 'Natália', 'Eduardo'],  # sala 2
    ['Carlos', 'Ana', 'Beatriz']  # sala 3  

]
print("\nListas dentro de listas:\n")
print(lista_salas) # imprimindo todas as listas

print("\Imprimindo as salas:\n")
print(lista_salas[0]) # imprimindo a primeira lista (sala 1)
print(lista_salas[1]) # imprimindo a segunda lista (sala 2)
print(lista_salas[2]) # imprimindo a terceira lista (sala 3)

print("\nImprimindo itens específicos das salas:\n") #ou nomes
print(""lista_salas[0][1]) # imprimindo o segundo item da primeira lista (sala 1) - Helena
print(lista_salas[1][2]) # imprimindo o terceiro item da segunda lista (sala 2) - Eduardo
print(lista_salas[2][0]) # imprimindo o primeiro item da terceira lista (sala 3) - Carlos

