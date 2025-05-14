#AULA SOBRE INPUT
"""

name = input('What is your name? ')
print(f"Nice to meet you {name}")

"""

#forma iniciante de converter a tipagem direto no comando input
#O codigo dessa forma faz com que o programa dê erro
#caso o usuario der os inputs incorretos
#Por exemplo: dessa forma se o usuario digitar uma letra ao inves
#de um numero, o programa imediatamente retornará um erro
#parando toda a operação ja no inicio do programa

numero1 = int(input('Type a number: '))
numero2 = int(input('Type another number: '))

print(f'The sum of th numbers is {numero1 + numero2}')

#forma melhor e sem margem para erro


numero1 = int(input('Type a number: '))
numero2 = int(input('Type another number: '))

#até aqui o programa le o input do usuario e adiciona na variavel
#no comando abaixo esse valor é convertido para inteiro
#porem caso o usuario digite uma string , o programa irá parar
#será necessario fazer a checagem...

int_numero1 = int(numero1)
int_numero2 = int(numero2)

print(f'The sum of th numbers is {int_numero1 + int_numero2}')

