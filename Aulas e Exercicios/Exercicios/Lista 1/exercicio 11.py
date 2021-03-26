print(f'---------------------')
print(f'CÁLCULO DA ENERGIA ELÉTRICA')
print(f'---------------------\n\n')

salmin = float(input(f'informe o salário minimo em vigor: '))

quilowatts = float(input(f'Informe a quantidade de Kw usadas: '))

indice = salmin*0.00143

valordeconsumo = quilowatts*indice

print (f'O valor unitário de Kw é {round(indice,2)}')

print (f'O valor da sua conta é {round(valordeconsumo,2)}')

print(f'O valor com desconto é {round(valordeconsumo*0.90,2)}')