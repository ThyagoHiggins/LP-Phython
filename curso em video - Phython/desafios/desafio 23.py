num = int(input('Informe um número (0 a 9999)'))
n = str(num)
print(f'Analisando o número {num}')
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')