num=[]
for cont in range(0,5):
    num.append(int(input(f'Informe um número para posição {cont}: ')))

print(f'Os números que você digitou foram {num}')

print()

print(f'O maior valor digitado foi {max(num)} nas posições ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}...', end='')

print()

print(f'O menor valor digitado foi {min(num)} nas posições ', end='')
for i, v in enumerate(num):
    if v== min(num):
        print(f'{i}...', end='')


