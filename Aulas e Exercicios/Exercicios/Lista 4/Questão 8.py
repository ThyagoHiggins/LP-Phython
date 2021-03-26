num = list()

for a in range(0,15):
    num.append((int(input(f'Informe o {a+1}º número: '))))

print(f' Os números que você digitou foram {num}')

print(f'Invertidos é {num[::-1]}')