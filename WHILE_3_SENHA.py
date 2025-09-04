#Exemplo de repetição
"""
O while é usado para repetições onde a quantidade
de strings é dinamica ou atualizada....
o FOR é a mesma função, porem melhor usado para strings ja
definidas  ou estáticas.
"""

senha = "12345678"
senha_digitada = ''
repetições = 0


while senha_digitada != senha: # função != é diferente de
    senha_digitada = input("Digite a senha: ")

    repetições += 1
    print(f"Tentativas de acesso: {repetições}x")

print("Senha válida")