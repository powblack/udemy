# sistema de perguntas

perguntas = {

    'questao1': {
        'pergunta': 'Quanto é 5 x 5 ?',
        'Opções': ['10', '15', '20', '25'],
        'Resposta' : '25',
    },

    'questao2': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'Opções': ['1', '4', '20', '300'],
        'Resposta' : '4',
    },
}


def questao(x, y):

    questao = x[y] 
    pergunta = questao.get('pergunta')
    valores = questao.get('Opções')

    print(f'{pergunta}\n')
    print('Opções:')

    opcoes = 1

    for valor in valores:
        print (f'{opcoes}) {valor}')
        opcoes += 1



def check(x, y, z):
    try:
        resposta = int(z)
        resposta -= 1
        questao = x[y] 
        valores = questao.get('Opções')
        resultado = questao.get('Resposta')
        
        opcao = valores[resposta]
        

        if opcao == resultado:
            print('Você acertou! ')
        
        else: 
            print('Você Errou!! ')

    except:
        print("Digite somente uma Opção!! ")


questao(perguntas, 'questao1')

resposta = input("Escolha a opção? ")

check(perguntas, 'questao1', resposta)

#------------------------------------------

questao(perguntas, 'questao2')

resposta2 = input("Escolha a opção? ")

check(perguntas, 'questao2', resposta2)



