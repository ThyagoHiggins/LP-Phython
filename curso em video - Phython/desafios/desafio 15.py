dias = int(input('Quantos dias você alugou o carro?'))
km= float(input('Quantos Km você rodou: '))
print(f'O preço a pagar pelo serviço é R${(dias*60) +(km*0.15):.2f}')