#Operadores lógicos
#  and /  or  /  not
# and - todas as condições precisam ser verdadeiras

"""
se qualquer valor for falso dentro do and 
a expressao inteira será avaliada naquele valor

0  0.0  'vazio' false  - sao expressoes do valor falso

"""

entrada = input("type E para ENTRAR: ")

if entrada == 'E':
    print("You entered the system !!")

else:
    print("***** ERROR ******")
    print("You need to type the word correctly !!")
    print("*** TRY AGAIN ****")