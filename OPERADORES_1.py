#OPERADORES ARITMÉTICOS


adicao = 10 + 10
print("adição = ", adicao)


subtracao = 10 -5
print("subritação = ", subtracao)

multiplicacao = 10 * 10
print("Multplicação = ", multiplicacao)

divisao = 10 / 3 #o resultado sempre virá em float
print("Divisão = ", divisao)

divisao_inteira = 10 // 3 #resultado somente inteiro, ele corta os valores decimais depois da virgula
print("Divisão inteira = ", divisao_inteira)

exponenciacao = 2 ** 10 #calculo de um numero elevado a outro
print("Exponenciação", exponenciacao)

modulo = 10 % 3 # é o resto que sobra na divisão
print("Módulo = ", modulo)

#Calculo para saber se um numero é divisivel por outro
#primeiro confere o valor do resto da divisao com o comando %
#depois usa o comando == 0 para checar se o valor é igual a 0
#logo se for 0 quer dizer que o numero é divisivel
print(10 % 5 == 0) # 5 é divisivel por 10
print(10 % 6 == 0) # 6 não é divisivel por 10

#para conferir também se um numero é par ou impar
#bastar verificar se o resto da divisao por 2 
#se é true ou false
print(10 % 2 == 0) #10 é um numero par
print(5 % 2 == 0) #5 é um numero impar
