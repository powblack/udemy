#formatação de strings

#Essa são as variáveis
a = 'a'
b = 'b'
c = 1.1

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
#neste caso a variavel string está como funcao objeto, sendo o
#.format() um metodo que modifica o objeto
print(formato)

#Desta forma embaixo, para que eu fuja do index oculto da ordem dos itens
#Posso adicionar um parametro para o argumento e criar meu index 
string = 'a={parametro1} b={parametro2} c={parametro3}'
#As variaveis que estão dentro da funcao, são chamadas argumentos
formato2 = string.format(
    parametro1=a,
    parametro2=b,
    parametro3=c
    )

print(formato2)

"""
em uma função como (a, b, c) existe uma ordem oculta, 
exemplo, o index dessa ordem é 0 1 2 ...
ou seja, se eu quizer alterar a ordem que aparece no terminal usando
o print, basta eu setar o index dentro das chaves {1} {0} {2}...
"""

#outro exemplo da funcao print, outro formato

#usando o index oculto ou ordem do python
nome = 'jonathan'
idade = 29

formato3 = '{} tem {} anos'
print(formato3.format(nome, idade))

#Definindo minha ordem, usando parametro para os argumentos
nome = 'manoely'
idade = 21

formato3 = '{n} tem {age} anos'
print(formato3.format(n=nome, age=idade))