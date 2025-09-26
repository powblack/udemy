perguntas = [
    {
        'pergunta': 'Quanto é 5 x 5 ?',
        'Opções': ['10', '15', '20', '25'],
        'Resposta' : '25',
    },
    {
        'pergunta': 'Quanto é 2 + 2 ?',
        'Opções': ['1', '4', '20', '300'],
        'Resposta' : '4',
    },
]

qtd_acertos = 0

for pergunta in perguntas: # o for pega os valores e joga um por um
    print('pergunta', pergunta["pergunta"])

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes): # o enumarate faz a adicao de indice
        print(f'{i}), {opcao}')

    
    escolha = input("Escolha um opção: ")

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True


    if acertou:
        qtd_acertos += 1
        print("Acertou")

    else:
        print("Errou")

print("voce acertou ", qtd_acertos)
