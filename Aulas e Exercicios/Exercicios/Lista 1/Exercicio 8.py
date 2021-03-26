print(f'---------------------')
print(f'CÁLCULO DO SALÁRIO')
print(f'---------------------\n\n')

horatra = float(input(f'Informe as horas trabalhadas'))
salmin = float(input(f'Agora informe o salário minimo'))

valorporhora = (salmin/220)/2

salbruto = horatra*valorporhora

print(f'Seu salário bruto é {round(salbruto,2)}')
imposto = salbruto*0.03
print(f'O imposto a ser pago é {round(imposto,2)}')
print(f'Seu salario do mês é {round(salbruto-imposto,2)}')