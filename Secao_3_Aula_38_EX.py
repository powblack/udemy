#Exercicio if elif else

name1 = input("What is your name? ")
valor1 = input("Type your grade: ")
name2 = input("What is your name? ")
valor2 = input("Type your grade: ")


if valor1 > valor2:
    print(f"{name1}, your grade is higher than {name2}")

elif valor2 > valor1:
    print(f"{name2}, your grade is higher than {name1}")

else:
    print(f"{name1} e {name2} have a same grade !!")

print("Program finished !! ")