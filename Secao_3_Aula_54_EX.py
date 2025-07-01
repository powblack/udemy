"""
questão 1: Faça um programa que peça ao usuário
para digitar um numero inteiro, informe se este
nummero se é impar ou par. Caso o usuario
não digite um numero interiro, informe que não 
que é um numero inteiro.
"""
numero = input("Digite um numero inteiro: ")

"""
if numero == int:
    print(f"O numero {numero} é PAR.")
    print(f"O numero {numero} é IMPAR. ")

else:
    print("Você deve digitar um numero inteiro!!! tente novamente...")
"""
"""
Questão 2: Faça um programa que pergute a hora ao
usuário e, baseando-se no horario descrito,
exiba a saudação adequada ao periodo do dia.
Ex: bom dia, boa tarde, boa noite!
"""
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
Faça um programa que peça o primeiro nome do usuario.
se o nome tiver 4 letras ou menos escreva 
"seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "seu nome é normal"; maior que 6 "seu nome é muito grande"
"""

