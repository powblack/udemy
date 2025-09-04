"""
args - Argumentos nõ nomeados

* - *args (empacotamento e desempacotamento)


lembrar do desempacotamento

"""

x, y, *resto = 1, 2, 3, 4, 5 # tupla, com numeros, porem só declarei x e y, o *resto, pega todos os valores
                             # restantes e monta uma lista para exibir no print
                             # como se fosse um pacote mesmo
print(x, y, resto)




