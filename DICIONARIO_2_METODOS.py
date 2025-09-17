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