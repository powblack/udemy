p1 = {
    'nome': 'jonathan',
    'idade': 30,
}

print(p1.get('nome'))# o get ele pega o valor que foi setado
print(p1.get('sobrenome'))# caso tente pegar um valor que não existe, retorna none
print('------------------------------')
""" 
bom de usar o get é que ele não gera erro quando busca um valor no
dicionario que não existe, já o comando

print(p1['valor']) usando [] gera um erro.

e com o get também tem a possibilidade de eu criar uma mensagem 
para modificar o none, exemplo

print(p1.get('nome', 'não existe'))

terminal: não existe

ou seja, no terminal era para aparecer none, porem foi modificado pelo 
comando apois o valor que tentei buscar



POP - APAGANDO 
o pop só apaga chaves especificas, que é setada, se não configura uma
chave dentro do () o programa retorna um erro, e se digitar um
valor ao inves de chave, também retorna um erro.

 """

nome = p1.pop('nome')

print(nome)
print(p1)

print('---------------------------')

p2 = {
    'key1': 10,
    'key2': 20,
    'list': [
        'nome',
        'sobrenome',
    ]
}

print(p2)
print('-------------------')
ultima_chave = p2.popitem()# apaga o ultimo item do dicionario, e mostra o item apagado

print(ultima_chave)
print(p2)


print('---------------------')
# UPDATE - atualiza como se fosse alterando com variavel

dic1 = {
    'nome': 'maria',
    'sobrenome': 'penha',
}

print(dic1)

atualizar = dic1.update({
    'nome': 'Jonathan',
    'idade': 30,
    'endereço': ['rua 1', 101, 'Bairro'],
})

print(dic1)


""" 
de forma melhor, podemos atulizar o dicionario usando o uptade com 
argumentos nomeados.

 """

dic1.update(
    nome= 'Atualizado',
    idade= 0
)
print(dic1)

print("---------------------------")

""" 
o update ele funciona com listas e tuplas, ou seja, ele funciona com
interaveis que possuam chave e valor.

veja o exemplo com lista e tupla

 """

p1 = {

}

lista = ['nome', 'jon'],
tupla = ('sobrenome', 'carvalho'),

p1.update(lista)
p1.update(tupla)

print(p1)