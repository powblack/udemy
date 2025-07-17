#INTERANDO STRINGS COM WHILE

frase = "O Python é uma lingagem de programação" \
    "Multiparadigma" \
    "Python foi criado por Guido"

#variavel frase com 3 strings, a função .lower()
# é para transformar as strings em minusculas
#assim quando for usar a funçã .count, pesquisar
#usando letra minuscula, facilitando a operação

print(frase.count("Python")) #.count() conta quantas vezes apareceu tal informação inserida no ()

i = 0

apareceu = 0
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    apareceu_atual = frase.count(letra_atual)

    if apareceu < apareceu_atual:
        apareceu = apareceu_atual
        letra_mais_vezes = letra_atual

    i += 1

print(
    f"A letra que apareceu mais vezes foi a letra: ",
    f"{letra_atual} , ".upper(),
    f"{apareceu}x"
      )