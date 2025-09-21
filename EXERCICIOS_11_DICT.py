# sistema de perguntas



""" print(
    f"Pergunta: Quanto é  5 x 5 ?\n", 
    f"\nOpções:",
    f'\n1) 10',
    f'\n2) 15',
    f'\n3) 20',
    f'\n4) 25'
) """

#pergunta1 = input("escolha uma opção: ")

perguntas = {

    'questao1': {
        'pergunta': 'Quanto é 5 x 5 ?',
        'Opções': ['10', '15', '20', '25'],
        'Resposta' : '25',
    },

    'questao2': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'Opções': ['1', '4', '20', '300'],
        'Resposta' : '25',
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
    questao = x[y] 
    valores = questao.get('Opções')
    resultado = questao.get('Resposta')
    opcao = z

    if opcao == resultado:
        print('Você acertou! ')
    
    else: 
        print('Você Errou!! ')



questao(perguntas, 'questao1')

#opcao1 = input("Escolha uma Opção? ")

#check(perguntas, 'questao1', opcao1)


lista = ['1', '2']

n2 = 1
n = lista[n2]

print(n)


if n2 == n:
    print('ok')

""" 
questao(perguntas, 'questao2')

opcao1 = input("Escolha uma Opção? ")
 """
