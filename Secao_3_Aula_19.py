#Tipos de dados no python

#tipagem do python= dinamica forte
#ou seja, ele consegue pegar alguns dados que não foram estabelecido a tipagem e fazer a tipagem por si proprio
#exemplo = 123 esse dado o python ja le como um numero do tipo inteiro, mas se eu quizesse que fosse na tipagem tipo string 
#eu teria que defini-la previamente

#Outro comando é o \ que dentro de uma string ou dentro de "aspas" faz com que ele ignore um comando
#Exemplo=
#print("Bom dia "Tudo bem?")
#Dessa forma o interpretador le o que esta dentro de aspas como string mas onde só tem uma aspa de um lado, ele tentar 
#enxergar como comando, por isso retorna como erro.

print("Bom dia \"Tudo bem?") # dessa forma , ele ignora a aspa do meio e le como se fosse um unica string

#Se eu quizer que o caracter \ apareça , eu uso o comando r
#Exemplo=
print(r"teste \"teste\" ")

# Outro exemplo para o codigo ficar mais limpo é usar aspa simples e duplas

print('"teste"')