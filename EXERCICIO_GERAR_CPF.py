"""
CPF: 158 699 617 77

CALCULO DO PRIMEIRO DIGITO VERIFICADOR DO CPF !!!!!!!

Colete a soma dos 9 primeiros digitos do cpf m
multiplicando cada um dos valores por uma contagem regressiva
começando de 10.

Exemplo: cpf 158.699.617-77 (158699617)
contagem regressiva:            10  9  8  7  6  5  4 3  2
9 primeiros digitos:             1  5  8  6  9  9  6 1  7
agora soma os resultados:       10+45+64+42+54+45+24+3+14 = 301

next step:

multiplique a soma por 10: 301 * 10 = 3010

next step:

pegue o resto da divisao do resultado por 11: 3010 % 11 = 7

next step:

VALIDAÇÃO, se o resultado do resto da divisao for maior que 9:
    considerar o digito como 0

se for menor que 9, considerar o digito como o proprio resultado
ou seja, se o resultado for igual ao primeiro digito verificador do cpf, está correto
se for diferente, o cpf é inválido.


"""
print("\n----------------------------------------------------\n")
print("BACKEND - GERADOR DE CPF - PRIMEIRO DIGITO VERIFICADOR\n")
print("\n----------------------------------------------------\n")

while True:

    #Validando a entrada do CPF apenas com números.

    try:
        cpf = int(input("Digite seu CPF (apenas números): "))
        print(f"CPF OK")
        break
    except ValueError:
        print("Por favor, digite apenas números.")
        continue

#Convertendo o CPF para string e garantindo que tenha 11 dígitos
#a função zfill adiciona zeros à esquerda se necessário, para completar 11 dígitos

cpf = str(cpf).zfill(11) # Adiciona zeros à esquerda se necessário

# Validando se o CPF tem 11 dígitos
if len(cpf) != 11:
    print("CPF inválido! Deve conter 11 dígitos.")
    exit()

else:
    print(f"CPF válido com 11 dígitos: {cpf}")

# Extraindo os 9 primeiros dígitos do CPF
nove_digitos = cpf[:9]
print(f"Os 9 primeiros digitos do CPF são: {nove_digitos}")

# Calculando o primeiro dígito verificador
soma = 0

for i, digito in enumerate(nove_digitos):
    # essa função (10 -i) faz a contagem regressiva, toda vez que o i aumenta, o (10 - i) diminui
    # assim, quando i = 0, (10 - 0) = 10
    # a função enumerate percorre a string, pegando o índice e o valor do dígito
    # a funcão int(digito) converte o caractere do dígito para inteiro
    # a funcão soma += acumula o valor da soma dos produtos, ou faz a soma dos produtos
    soma += int(digito) * (10 - i)
    
print(f"A soma dos produtos é: {soma}")

# Multiplicando a soma por 10

multiplicacao = soma * 10
print(f"A multiplicação da soma por 10 é: {multiplicacao}")

# Pegando o resto da divisão por 11

resto = multiplicacao % 11
print(f"O resto da divisão por 11 é: {resto}")

# Validando o primeiro dígito verificador

if resto > 9:
    primeiro_digito = 0
    if primeiro_digito == 0:
        print("\n-------------------\n")
        print("\n-------------------\n")
        print("\n-------------------\n")
        print("\n-------------------\n")
        print(f"CFP: {cpf} É INVÁLIDO, TENTE NOVAMENTE!!!")
        print("\n-------------------\n")


else:
    primeiro_digito = resto

print(f"O primeiro dígito verificador é: {primeiro_digito}")

print("\n-------------------\n")
print("\n-------------------\n")
print("\n-------------------\n")
print("\n-------------------\n")
print(f"CFP: {cpf} É VÁLIDO, PARABENS!!!")
print("\n-------------------\n")

