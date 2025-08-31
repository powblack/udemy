cpf = '0029254175'

resultado = 0
contagem = 11

for digito in cpf:
    resultado += int(digito) * contagem
    contagem -= 1

multiplicador = resultado * 10

resto = multiplicador % 11

print(resto)
