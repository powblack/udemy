"""
split, join, strip methods in Python

split: divide a string

join: combine a list of strings into one string / combina as strings

strip: remove whitespace from the beginning and end of a string / remove espaços em branco do início e do fim de uma string
rstrip - remove espaços em branco do fim
lstrip - remove espaços em branco do início




"""

frase = "   Olá, meu nome é João.   "
lista_palavras = frase.split()  # separando por espaço
print(lista_palavras)  

lista_palavras_virgula = frase.split(",")  # separando por vírgula, ou separa frases
print(lista_palavras_virgula)

lista_palavras_virgula_espaco = frase.split(", ")  # separando por vírgula e espaço
print(lista_palavras_virgula_espaco)

#outra forma melhor de usar
frase2 = 'Olá, meu nome é Ana. Eu gosto de ler, escrever, estudar, aprender. Eu gosto de viajar. Eu gosto de programar.'
lista2 = frase2.split('.')

for i, frase2 in enumerate(lista2):
    print(lista2[i].strip())  # removendo espaços em branco do início e do fim (STRIP)

"""
METODO MAIS CORRETO DO QUE O DE CIMA
EXEMPLO ABAIXO

pois a lista agora não é alterada, e sim uma nova lista é criada com as frases sem espaços em branco
a lista3 continua a mesma.

sendo boas pra práticas de programação, pois no futuro vc pode precisar da lista original


"""
print("\nOutro exemplo mais correto:\n") #\n é para pular linha



frase3 = "Helow, my name is John. I like to read, write, study, learn. I like to travel. I like to program."

lista3 = frase3.split('. ')

lista_frases3 = [] # criando uma lista vazia para adicionar as frases sem espaços em branco

for i, frase3 in enumerate(lista3):
    lista_frases3.append(lista3[i].strip())  # removendo espaços em branco do início e do fim (STRIP) e adicionando na nova lista   

print(lista_frases3)


print("\nUSANDO O JOIN:\n")

"""
#join para juntar uma lista de strings em uma string só

"""

frases_unidas = '. '.join(lista_frases3)  # juntando a lista de frases em uma string só, separando por '. '

print(frases_unidas)