"""
Formatação básica de strings
s - string
d - int
f - float
.< número de digitos >f
x ou X - hexadecimal
(caractere) (><^) (quantidade)
> - esquerda
< direita
^ - centro
sinal - + ou - 
ex.: 0>-100,.1f
conversion flags - !r !s !a

"""
# o comando f formata a string, veja o exemplo

variavel = 'abc'
print(f"{variavel}")

# outro exemplo

variavel2 = 'joao'
print(f"{variavel2:>>10}") # adicionando simbolo à esquerda
print(f"{variavel2:<>10}") # adicionando simbolo à direta
print(f"{variavel2:%^10}") # adicionando simbolo ao centro

print(f'O hexadecimal de 1500 é {1500:08X}')