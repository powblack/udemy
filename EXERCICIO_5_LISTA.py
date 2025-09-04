"""
Faça uma lista de comprar com listas.
o usuario deve ter a possibilidade de inserir
apagar e listar valores da sua lista.
não permita que o programa quebre com erros 
de indices inexistentes.

"""
import os

os.system("cls" if os.name == "nt" else "clear")

print("---------------------------------")
print("Bem-vindo à sua lista de compras!")
print("---------------------------------")

lista = []

while True:
    print("Digite uma opção:")
    print("[I]nserir item [A]pagar item [L]istar itens [S]air")

    resposta = input("Opcão: ").upper()

    
    if resposta == 'I':
        os.system("cls" if os.name == "nt" else "clear")
        item = input("Digite o item que deseja inserir: ")
        lista.append(item)
        print(f"Item '{item}' adicionado à lista.")

    elif resposta == 'A':
        os.system("cls" if os.name == "nt" else "clear")
        if lista == []:
            print("A lista está vazia. Não há itens para apagar.")
            continue
        
        try:
            indice = int(input("Digite o índice do item que deseja apagar: "))
            del lista[indice]
            print(f"Item no índice {indice} removido da lista.")
        
        except (ValueError, IndexError):
            print("Índice inválido. Tente novamente.")
        
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


    elif resposta == 'L':
        os.system("cls" if os.name == "nt" else "clear")
        if lista == []:
            print("A lista está vazia.")

        else:
            print("Itens na sua lista de compras:")
            for i, item in enumerate(lista):
                print(f"{i}. {item}")

    elif resposta == 'S':
        os.system("cls" if os.name == "nt" else "clear")
        print("Saindo do programa...")
        break

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Opção inválida. Tente novamente.")
        continue

    