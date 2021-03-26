sal = float(input("Insira o valor de salário "))
aumento = float(input("Insira o valor do aumento "))

valoraumentado = sal*(aumento/100)

salariofinal = sal + valoraumentado

print (f' O valor de seu salário é {sal}\n O percentual de aumento é {aumento}\n Valor a ser adicionado{valoraumentado}\n salario final {salariofinal}')
