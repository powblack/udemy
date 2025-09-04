"""""
operação ternária em Python
<valor> if <condição> else <outro valor>

explicando essa estrutura:
<condição> é avaliada como True ou False
<valor> é retornado se a condição for True
<outro valor> é retornado se a condição for False


"""
condicao = 10 == 10


variavel = 'Valor' if condicao else 'Outro valor'

print(variavel)

print("\nExemplo 2:\n")

idade = 17

conferir_idade = idade if idade >= 18 else 'Não pode entrar'

print(conferir_idade)
