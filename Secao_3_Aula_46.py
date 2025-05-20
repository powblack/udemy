#Fatiamento de strings
#o mesmo estudo de index ou indice

#fatiamento [i:f:p] [::]
#obs.: a funcao len retorna a qtd 
#de caracteres da str


variavel = 'inicio', 'meio', 'fim'
alfabeto = 'ABCDEFGHIJLMNOPQRSTUVXZWY'
print(len(variavel)) # conta a  quantidade de indice 
print(len(alfabeto))

#o p é o passo

#exemplo: o 0 é o inicio, o 9 é o fim da contagem e o 3 é o passo
#ou seja, ele vai contar os indices do inicio ate o fim pulando de 
#3 em 3
print(alfabeto[0:25:2])
