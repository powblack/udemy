#jogo com while

"""
exemplo de while abaixo, enquanto a for verdadeiro o 
codigo dentro do while sera executado, o continue faz com que o
codigo volte para o inicio do while.
    o break faz com que o while seja encerrado.

"""
import os

palavra_secreta = "python" 

letras_acertadas = '' # variavel que armazena as letras acertadas
numero_tentativas = 0 # variavel que armazena o numero de tentativas

while True:

    letra = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra
    
    else:
        print("Letra não está na palavra secreta.")

    palavra_formada = ''

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra

        else:
            palavra_formada += '*'
    
    if letra not in palavra_secreta:
        print(f"Palavra secreta: {palavra_formada}")
        continue

    if letra in palavra_secreta:
        print(f"Palavra secreta: {palavra_formada}")


    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("Parabéns! Você acertou a palavra secreta.")
        print(f"Número de tentativas: {numero_tentativas}")
        break