import random


for _ in range(100):
    nine_digits = ''

    for i in range(9):
        nine_digits += str(random.randint(0, 9))

    countdown = 10

    result_digit = 0

    for digit in nine_digits:
        result_digit += int(digit) * countdown
        countdown -= 1

    digit = (result_digit * 10) % 11
    digit = digit if digit <= 9 else 0 

    ten_digits = str(nine_digits) + str(digit)

    countdown2 = 11

    result_digit2 = 0

    for digit2 in ten_digits:
        result_digit2 += int(digit2) * countdown2
        countdown2 -= 1

    digit2 = (result_digit2 * 10) % 11
    digit2 = digit2 if digit2 <= 9 else 0 


    cpf = str(ten_digits) + str(digit2)

    print(cpf)