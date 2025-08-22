
lista = []
start = input("Digite 'start' para iniciar o programa: ")

while True:
    if start.lower() != 'start':
        print("Comando inválido. Tente novamente.")
        start = input("Digite 'start' para iniciar o programa: ")
        continue
    try:
        numero1 = int(input("Digite um número: "))
        lista.append(numero1)
        print(f"Números digitados: {lista}")
        continue

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


    