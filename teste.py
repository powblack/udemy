#calculo de splitagem

spliter_10_90 = 11, 0.7

perda1 = -11
perda2 = -0.7

perda_1x8 = -10.5
perda_1x16 = -13.5

potencia_olt = 5

sinal_cto = perda1 + perda_1x8 + potencia_olt

a = 1
b = 2
c = 3

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

print(formato)


print(sinal_cto)
