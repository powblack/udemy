""" 
dicionarios em python (tipo dict)

dicionarios sao estruturas de dados do tipo 
par de "chave" e "Valor" .
chaves podem ser consideradas como o "indice"
que vimos na lista e podem ser de tipos imutaveis
como: str, int, float, bool, tuple, incluindo outro dicionario.

"""

dicionario = {} #dicionarios usam a estrutura com {chaves}
print(type(dicionario)) # veja o exemplo no terminal

pessoa = {

    "Nome" : "Jonathan",
    "Idade": 30
    
}
print(pessoa)

# outra forma de fazer um dicionario

pessoa2 = dict(
    nome="Jonathan",
    sobrenome="Carvalho"
)
print(pessoa2)

#--------------------------------------------------
#dicionarios com lista dentro de listas

pessoa3 = {
    'nome': 'jonathan',
    'idade': 30,
    'endereços': [
        {'minha casa': 'porto de santana'},
        {'empresa': 'porto novo'},
    ]
}
print(pessoa3)
print(pessoa3['nome']) # para acessar os dados que eu quero no dicionario, usar o ['']

for chave in pessoa3:
    print(chave, pessoa3[chave])

# tambem pode montar dinamicamente

dicionario_pessoa = {} # dicionario vazio

chave = 'nome' # criado uma variavel

dicionario_pessoa[chave] = 'Jonathan' # adicionando no dicionario usando variavel 

dicionario_pessoa['Sobrenome'] = 'Carvalho' # adicionando no dicionario diretamente


print(dicionario_pessoa)

# para remover ou deletar

del dicionario_pessoa['Sobrenome']

print(dicionario_pessoa)

#modos para evitar erros 
# quando ocorre um erro o programa quebra,
# e nao executa nenhum codigo posterior
# para corrigir pode usar o 
# TRY EXECPT    
# ou o .get(), veja abaixo

print(dicionario_pessoa.get('Sobrenome'))# dessa forma o get retorna uma valor none
print(dicionario_pessoa.get('Sobrenome', 'Não existe')) # dessa forma eu configuro uma mensagem no lugar de none

#se exister vai exibir o valor

#forma mais usual

if dicionario_pessoa.get('Sobrenome') is None:
    print("Valor não existe")

else:
    print(dicionario_pessoa)

