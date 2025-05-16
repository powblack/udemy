#Operador or


entrada = input('Type [ENTER] to conect: ')

if entrada == 'ENTER' or entrada == 'enter' or entrada == 'Enter':
    senha = input("Type a key: ")
    confirma_senha = input("Type again your key: ")

    if senha == confirma_senha:
        print("Your registration was sucessful!")
    elif confirma_senha != senha:
        print("Wrong key, restart the program...")
else:
    print("wrong word, restart the program...")


#outro comando legal para fazer

senha = input("Key: ") or 'No keys typed'
print(senha)