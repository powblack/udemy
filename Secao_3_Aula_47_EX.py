#EXERCICIO
"""
peça ao usuario para digitar seu nome
peça ao usuario para digitar sua idade
se nome e idade forem digitados:
    exiba
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        se nome contem (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}

se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."

    print(f"Seu nome é {nome}")
    print(f"Sua idade é de {idade} anos")
    #print(f'seu nome invertido é {nome invertido}')
    #print(f'se nome contem (ou não) espaços')
    print(f'seu nome tem {len(nome)} letras')
    #print(f'a primeira letra do seu nome é {letra}')
    #print(f'a ultima letra do seu nome é {letra}')

"""

nome = input("Digite seu nome: ")
idade = input("digite sua idade: ")

"""

# A forma que eu estava fazendo !!1
if (nome != "") and (idade != ""):
    print(f"Seu nome é {nome}")
    print(f"Sua idade é de {idade} anos")
    #print(f'seu nome invertido é {nome invertido}')
    if nome == (" " in nome):
        print(f'se nome contem (ou não) espaços')
        print(f'seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'a ultima letra do seu nome é {nome[:20]}')

else:
    print("Desculpe, você deixou campos vazios.")

"""

# A forma que o professor fez

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Você tem {idade} anos de idade")
    print(f'Seu nome invertido é {nome[::-1]}') # o comando ::-1 conta os passos voltando, pois é negativo
    
    if " " in nome:
        print(f'Seu nome é composto !!')
    else:
        print("Seu nome é simples !! ")

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}') # o indice -1 é a ultima str

else: 
    print("Desculpe, você deixou campos vazios.")