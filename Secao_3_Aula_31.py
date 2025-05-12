#limpando o codigo, ou outra forma de usar variaveis
#dentro o comando print

nome = 'jonathan carvalho gregorio'
altura = 1.63
peso = 70
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} metros de altura'
linha_2 = f"Seu peso é {peso} Kg"
#O comando :.2f formata o numero para apenas 2 casa decimais depois da virgula
linha_3 = f"Seu IMC é de {imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)