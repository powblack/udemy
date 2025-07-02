"""
questão 1: Faça um programa que peça ao usuário
para digitar um numero inteiro, informe se este
nummero se é impar ou par. Caso o usuario
não digite um numero interiro, informe que não 
que é um numero inteiro.
"""
print("QUESTÃO: NUMERO PAR OU IMPAR")
numero = input("Digite um numero: ")


if numero.isdigit():
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print(f"O numero {numero_inteiro} é par !!")
    else:
        print(f"O numero {numero_inteiro} é impar !!")
else:
    print('Voçê não digitou um numero!!')


"""
Questão 2: Faça um programa que pergute a hora ao
usuário e, baseando-se no horario descrito,
exiba a saudação adequada ao periodo do dia.
Ex: bom dia, boa tarde, boa noite!
"""
print("QUESTÃO: HORA DO DIA")
entrada = input("Digite a hora: ")

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
    else:
        print("Horario não reconhecido !!")

except:
    print("Digite apenas numeros inteiros!!")

"""
 FORMA QUE EU FIZ

horas = input("Que horas são? ")

horas = int(horas)
if (horas >= 6) and (horas <= 12):
    print("Bom dia")

if (horas >= 13) and (horas <= 18):
    print("Bom tarde")

if (horas >= 19) and (horas <= 23):
    print("Bom noite")


if (horas >= 0) and (horas <= 5):
    print("Bom Madrugada")


else:
    ...

"""
"""
Faça um programa que peça o primeiro nome do usuario.
se o nome tiver 4 letras ou menos escreva 
"seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "seu nome é normal"; maior que 6 "seu nome é muito grande"
"""
print("QUESTÃO TAMANHO DO NOME")
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if " " in nome:
    print('Digite só o primeiro nome!')

elif tamanho_nome <= 1:
    print('Digite mais de uma letra!')

elif tamanho_nome <= 4:
    print('Seu nome é curto!')

elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal!')

elif tamanho_nome > 7:
    print('Seu nome é muito grande!!! ual')

else:
    print('HOUVE ALGUM ERRO!!')