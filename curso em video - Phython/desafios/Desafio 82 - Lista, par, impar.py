num = list()
pares = list()
impares = list()
print(f'Informe 10 números para colocar em uma lista:')
for a in range(0, 10):
        num.append((int(input(f'Informe o {a + 1}º número: '))))

for p in num:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
num.sort()
pares.sort()
impares.sort()
print(f'Os números digitados foram: {num}\n'
      f'os pares são{pares}\n'
      f'e por fim os impares são{impares}')