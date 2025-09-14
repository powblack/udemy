"""
Higher order functions
Funções de primeira classe


exemplo abaixo, uma função chama a outra


"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!' # retorna o valor que foi enviado para a função no parametro msg

def executa(funcao, *args):
    return funcao(*args) # as () faz a execução de uma função, a variavel funcao() é apena o parametro da funcao executa


print(executa(saudacao, "Bom Dia", "Luiz"))

