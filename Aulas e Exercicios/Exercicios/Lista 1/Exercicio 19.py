prestacao = float(input('Informe o valor da prestação: R$  '))
tempo = int(input('Informe o tempo em meses: '))
taxa= float(input('Informe a taxa em %:  '))

taxa2 = taxa/100
final= prestacao+(prestacao*taxa2*tempo)
print (f'O valor da prestação será {final:.2f}')