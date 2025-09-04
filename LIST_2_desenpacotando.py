#desempacotamento em chamadasde metodos e funcoes


string = "ABCD"

lista = ["Maria", "Helena", 1, 2, 3, "Luiz"]

tupla = "Maria", "Helena", 1, 2, 3, "Luiz"

print(string)
print(lista)
print(tupla)
print(*string) # desempacotando a string
print(*lista) # desempacotando a lista
print(*tupla) # desempacotando a tupla

#outro exemplo com listas dentro de listas

lista_salas = [
#       0        1         2
    ['Maria', 'Helena', 'Luiz'],  # sala 1
#      0         1          2
    ['João', 'Natália', 'Eduardo'],  # sala 2   
#      0        1        2
    ['Carlos', 'Ana', 'Beatriz']  # sala 3  
]


print(*lista_salas)

print("\n----------------------------\n")
#EXEMPLO ABAIXO, É UM DESEMPACOTAMENTO DE LISTA DENTRO DE LISTA,
# O ( END = '\N' ) É PARA QUE A IMPRESSÃO FIQUE EM UMA LINHA SÓ, NO FINAL DO CODIGO
print(*lista_salas, end='\n') # desempacotando a lista de listas
print("\n----------------------------\n")
print(*lista_salas, sep='\n')