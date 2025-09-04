"""
Interpolação básica de strings

s  - string 
d e i - int
f - float 
x e X - hexadecimal (ABCDEF0123456789)


"""

# o % faz como se fosse uma substituicao para 
#diminuir a 
nome = 'Luiz'
preco = 1000.832423
variavel = "%s, o preço é R$%.2f reais" % (nome, preco)
print(variavel)