"""
Higher order functions
Funções de primeira classe


exemplo abaixo, uma função chama a outra


"""

def saudacao(msg):
    return msg # retorna o valor que foi enviado para a função no parametro msg

def executa(funcao, msg):
    return funcao(msg) # as () faz a execução de uma função, a variavel funcao() é apena o parametro da funcao executa


v = executa(saudacao, "Bom dia")
print(v)

#-----------------------------------------------------

def funcao1(msg1):
    return msg1

def funcao2(msg2):
    return msg2

def funcao3(msg3):
    return msg3

def exec