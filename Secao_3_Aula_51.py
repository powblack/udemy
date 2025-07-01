#codigo, exercicio de radar

# variaveis do movimento do carro

velocidade = input("Qual foi sua velocidade no radar? ")
velocidade = float(velocidade)

# KM onde está o carro na pista

local_carro = input("Qual KM voce estava? ")
local_carro = int(local_carro)

# valores constantes, ou base de dados
#limites difinidos para o calculo do radar
RADAR_1 = 60 # LIMITE DE VELOCIDADE 
LOCAL_1 = 100 # LOCAL ONDE SE ENCONTRA O RADAR
RADAR_RANGE = 1 # DISTANCIA EM METROS DA LEITURA

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    
    print('Voce foi multado no Radar 1!!')


else:
    print('multa não encontrada!')