""" 
metodos uteis dos dicionarios em python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com as chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especifica (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro

 """

pessoa = {
    'nome': 'jonathan',
    'sobrenome' : 'carvalho',
    'idade': 30,
    'chave': 'valores',
    'keys': 'values',
}

print(len(pessoa))#metodo que conta quantas chaves dentro do dicionario
print(pessoa.keys())#retorna as chaves
print(tuple(pessoa.keys()))# retorna os valores dentro da uma tupla
print(list(pessoa.keys()))# retorna os valores dentro de uma lista

print(pessoa.values())#retorna os valores

for valor in pessoa.values():
    print(valor)


print(pessoa.items())

for i in pessoa.items():#items sao os valores e chaves
    print(i)

for chave, valor in pessoa.items():
    print(f'Essa é a chave: {chave}, Esse é o valor: {valor}')


pessoa.setdefault('idade', 0) #configura uma chave com valor padrao
print(pessoa['idade'])



#  SHALLOW COPY

dicionario1 = {
    "chave1": 1,
    'chave2': 2,
    'lista': [0, 1, 2, 3],
}

dicionario2 = dicionario1 # desta forma essa função nao copia o dicionario
                          # ela aponta para a variavel, ou seja ...

dicionario2['chave1'] = 1000 # alterando o valor da chave1 pela variavel dicionario2
                             # o valor é alterado pois essa variavel aponta como se fosse a propria
                             # não é uma copia e sim so está direcionando
print(dicionario2)

                        

# AGORA PARA COPIAR O DICIONARIO E TER DOIS DICIONARIOS DISTINTOS COPIADOS
# obs: vou utilizar o mesmo dicionario
#porem é uma copia rasa, pois ele copia os dados do dicionarios
#mas, não copia valores tipo uma lista dentro do dicionario
""" 
boas praticas, usando esse tipo de copy, pode consumir muita memoria e 
processamento do computador, pois ele aponta para o dicionario principal
quando há valores mutáveis.

ou seja, valores imutáveis são os valores definidos no dicionario, que
por sua vez é alterado por uma função, no caso dos mutáveis, a lista dentro
de outra lista no dicionario, mesmo com o copy é alterado em todas os
dicionarios pois, a copia rasa significa que o programa aloca na memoria
um cache desse comando esperando alteração ou outro comando.

 """

dicionario2 = dicionario1.copy() 

dicionario2['chave2'] = 8
dicionario2['lista'][1] = 1995 # ordem da funçao, primeiro chama a chave [], depois o indice []


print(dicionario1)
print(dicionario2)

#deep copy

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'c2': 3,
    'l1': ['Rua Travessa floriano', 73, 'porto de santana'],
}

""" 
com deep copy, usar a biblioteca import copy

assim ele copia todos os subniveis do diconario, copiando literalmente tudo
e alterando sem ter consumo de memoria ou ficar dados no cache.
 """


d2 = copy.deepcopy(d1)

d2['c1'] = 27
d2['l1'][1] = 101

print(d1)
print(d2)

