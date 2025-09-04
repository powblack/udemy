"""
aprendendo a manejar listas dentro de listas
procurar itens dentro de listas


"""

lista_salas = [
#       0        1         2        
    ['Maria', 'Helena', 'Luiz'],  # sala 1
#      0         1          2
    ['João', 'Natália', 'Eduardo'],  # sala 2
#      0        1        2
    ['Carlos', 'Ana', 'Beatriz', (1, 2, 3)]  # sala 3 , tupla dentro da lista  

]
print("\nListas dentro de listas:\n")
print(lista_salas) # imprimindo todas as listas

print("\nImprimindo as salas:\n")
print(lista_salas[0]) # imprimindo a primeira lista (sala 1)
print(lista_salas[1]) # imprimindo a segunda lista (sala 2)
print(lista_salas[2]) # imprimindo a terceira lista (sala 3)

print("\nImprimindo itens específicos das salas:\n") #ou nomes
print(lista_salas[0][1]) # imprimindo o segundo item da primeira lista (sala 1) - Helena
print(lista_salas[1][2]) # imprimindo o terceiro item da segunda lista (sala 2) - Eduardo
print(lista_salas[2][0]) # imprimindo o primeiro item da terceira lista (sala 3) - Carlos
print(lista_salas[2][3][1])# imprimindo o quarto item da terceira lista (sala 3) - tupla (1, 2, 3)

while True:
    sala = int(input("Digite o número da sala que você quer acessar (1, 2 ou 3): "))
    nome = int(input("Digite o numero do ID do Aluno: "))
    print(lista_salas[sala - 1][nome - 1])  # convertendo a entrada para inteiro e ajustando o índice

