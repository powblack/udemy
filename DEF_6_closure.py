#Closure e funções que retornam outras funções


def criar_saudacao(saudacao): #função que fica na memoria esperando ser executada
    def saudar(nome): # essa função é executada com a variavel 
        return f'{saudacao}, {nome}'
    return saudar # retorna na memoria a função sem ser executada, esperando ela ser executada depois


bomdia = criar_saudacao("Bom dia") #chamada da função ja criando funções ou blocos prontos
boatarde = criar_saudacao("Boa Tarde")
boanoite = criar_saudacao("Boa Noite")

periodo = input("Digite dia, tarde ou noite:  ")

classe = []

while True:

    nomes = str(input("Digite os nomes nos alunos: "))

    classe.append(nomes)

    print(classe)

    fechar = input("Digite [S]air ou Press Enter: ")

    if fechar == 's':
        break
    
    else:
        continue



if periodo == 'dia':

    for nome in classe:
        print(bomdia(nome))

if periodo == 'tarde':

    for nome in classe:
        print(boatarde(nome))

if periodo == 'noite':

    for nome in classe:
        print(boanoite(nome))


""" 
while True:
    nome = input("Qual o seu nome? ")
    horario = input("Que peridodo é agora? ")

    try:
        if horario == 'dia':
            print(bomdia(nome))
            continue
        if horario == 'tarde':
            print(boatarde(nome))
            continue
        if horario == 'noite':
            print(boanoite(nome))
            continue

        if horario != 'dia' or horario != 'tarde' or horario != 'noite':
            raise ValueError("Periodo inválido. Digite 'dia', 'tarde' ou 'noite'.")
        

    except Exception as e:
        print(e)
        break


 """