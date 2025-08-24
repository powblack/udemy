# double-precision-point-format IEEE 754


numero_1 = 0.1
numero_2 = 0.2
soma = numero_1 + numero_2
print(f"Resultado impreciso: {soma}") # o resultado esperado seria 0.3, mas o resultado é 0.30000000000000004

# o python trabalha com precisão de 15 a 17 digitos

# para resolver esse problema, podemos usar a biblioteca decimal
from decimal import Decimal
numero_1 = Decimal("0.1")
numero_2 = Decimal("0.2")
soma = numero_1 + numero_2
print(soma)  # o resultado esperado seria 0.3, e o resultado é 0.3
print(f"Resultado com biblioteca decimal: {soma:.2f}") # o resultado esperado seria 0.3, e o resultado é 0.30 , 

# a função round() tambem pode ser usada para resolver esse problema
numero_1 = 0.1      
numero_2 = 0.2
soma = numero_1 + numero_2
soma = round(soma, 2)
print(f"Resultado com round: {soma}")  # o resultado esperado seria 0.3, e o resultado é

