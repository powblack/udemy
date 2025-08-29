cpf = '15869961777'

nove_digitos = cpf[:9] # fatiamento da str, usando o : e o 9 quer dizer que a função vai parar no indice 9

contador_regressivo = 10

resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1 # o -= é a função que faz a subtração do numero 10, ou seja, cada fez que passa ele diminui

digito = (resultado * 10) % 11

digito = digito if digito <= 9 else 0

print(digito)

