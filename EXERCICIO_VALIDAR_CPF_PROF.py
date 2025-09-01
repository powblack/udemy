cpf = str(input("Enter your CPF: ")) \
    .replace(',', '') \
    .replace('.', '') \
    .replace(' ', '') \
    .replace(',', '')

nine_digits = cpf[:9] # slicing the str, using : and the 9 means that the function will stop at index 9
countdown = 10
result = 0

for digit in nine_digits:
    result += int(digit) * countdown
    countdown -= 1 # that -= is the function that subtracts the number 10, that is, each time it passes and it decreases

digit = (result * 10) % 11

digit_str = str(digit)

nine_digit = cpf[9]

if digit_str != nine_digit:
    print("CPF is invalid !! Try again ...")

else:
    print("Fist Digit is OK. passed")

#---------------------------------------------
# calculating the next digit, second digit

ten_digits = cpf[:10] # slicing the str, using : and the 9 means that the function will stop at index 9
countdown2 = 11
result2 = 0

for digit2 in ten_digits:
    result2 += int(digit2) * countdown2
    countdown2 -= 1 # that -= is the function that subtracts the number 11, that is, each time it passes and it decreases

digit2 = (result2 * 10) % 11

digit_str2 = str(digit2)

ten_digit = cpf[10]

if digit_str2 != ten_digit:
    print("Second Digit is incorrect, Try again ...")

else:
    print("Second Digit passed, CPF is OK!")
                                                                                                                                                                                        