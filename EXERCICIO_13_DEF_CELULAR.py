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
    
    'questao3': {
        'pergunta': 'Quanto é R$ 100,00 reais + R$ 50,00 reais?',
        'Opções': ['R$30,00 reais', 'R$300,00 reais', 'R$10,00 reais', 'R$150,00 reais'],
        'Resposta': 'R$150,00 reais',
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
            return True

        else: 
            return False

    except:
        print("Digite somente uma Opção!! ")


nota = 0

for questoes in perguntas:
    questao(perguntas, questoes)
    resposta = input("Escolha a opção? ")
    
    v= check(perguntas, questoes, resposta)
    
    if v == True:
        nota += 1
        
lista = len(perguntas)

acertos = nota

print(f"Voce acertou {acertos} de {lista} perguntas")