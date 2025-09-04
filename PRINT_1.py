#Explicando sobre os comandos print

print(12, 34) #Esse comando o print, vai imprimir na tela esse dois argumentos, sem formatação, somento com espaço.

print(56, 78, sep=",") #Nesse o comando sep (separador), ele adiciona o simbolo que desejar no lugar do padrão, que é o espaço

"""
Quebra de linha tem um comando oculto do proprio sistema operacional, 
no windows usa-se o CRLF que são interpretados com (\r , \n), em linux LF (\n)
porem em sistemas novos windows, somente o comando \n já faz a quebra de linha ou remove a quebra de linha.
"""

"""
O comando end significa que terá uma função no final do comando print, ou seja usando o \n faz a mesma coisa do padrao
que é a quebra de linha.


"""
print(10, 20, sep=",", end="\n")

"""
outro exemplo é o comando end, quando digitado um caracter qualquer, ele exibe os valores da proxima linha juntos
e com o caracter no meio colado, veja o exemplo abaixo.
"""
print("jonathan_c.g1995", sep="-", end="@")
print("hotmail.com")

# se eu adicionar o \n antes ou depois, ele faz a quebra de linha adicionando o caractere.

print(1, 2, 3, sep="-", end="\n...\n")
print("Bom dia")