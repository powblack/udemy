"""
Calculadora usando while!

"""
print("BEM VINDO !!")
print("FAÇA SEUS CALCULOS ABAIXO")


#bloco função while, loop ate eu digitar S para sair !!!

while True:
    numero_1 = input("Numero:  ")
    numero_2 = input("Numero:  ")
    operador = input("Operador:  ")

    valido = None #essa variavel eu uso para validar em try

    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        """
        nessa etapa o codigo é validado, se as duas variaveis acima
        forem satisfeitas, na variavel VALIDO atribui True como verdadeiro
        para dar continuidade no codigo.
        """
        valido = True

    except:
        valido = None
        """
        Se não passar no TRY, a variavel VALIDO for FALSE, o codigo pula
        para a função IF para voltar o codigo ao inicio!
        """

    if valido is None:
        print("Digite apenas numeros! ")
        print("Tente novamente! ")

    """
    ESSE É AS FUNÇÕES FINAL DA CALCULADORA !!

    para fechar o codigo, baster digitar S, no comando input,
    usar o .lower que converte a string para minuscula e o
    .startwhith pega a primeira string do input e retorna True para a string 
    que eu declarar dentro do ().


    """
    sair = input("Quer sair? [S]im ").lower().startswith("s")

    if sair is True:
        print("LOGOFF")
        break

    else:
        continue # comando retorna para o inicio do laço do WHILE



