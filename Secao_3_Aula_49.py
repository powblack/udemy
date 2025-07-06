# introdução ao try/except
# try - tentar
# except - ocorreu algum erro ao tentar

"""
numero = input('digite um numero: ')

numero_float = float(numero)
print(f'o dobro do numero {numero} é {numero_float * 2}')


#a função isdigit obriga o input usar apenas digitos numericos
# sem pontos e sem virgulas ou qualquer caractere

numero = input("Digite um numero: ")

if numero.isdigit():
    numero = float(numero)
    print(numero)
else:
    print("Digite apenas numeros!!!")

"""

#usando o Try e o Except

nome = input(str("Nome: "))
numero = input("Numero: ")

try:
    print(type(nome))
    print(f"seu nome é {nome}")
    print(f"Numero que vc digitou {numero}")
    print(type(numero))

except:
    print("Voce fez algum errado!!")
