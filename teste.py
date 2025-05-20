#testes

horas_curso = int(input("Quantas horas é o curso? "))
horas = int(input("Quantas horas por dia você estuda? "))
dias = horas_curso / 24
dias_para_acabar = horas_curso / horas

print(f"São {horas_curso} horas total do curso")
print(f"São {dias:.0f} dias para terminar o curso")
print(f"Mas como eu estudo somente {horas} hr por dia")
print(f"No seu ritmo, são {dias_para_acabar:.0f} dias para terminar")