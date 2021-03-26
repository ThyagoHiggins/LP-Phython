num = [2,5,9,1]
print(num)

num[2]=3
print(num)

num.append(7)
print(num )

num.sort()
print (num)

num.sort(reverse=True)
print(num)

print(F'Essa lista tem {len(num)} elementos')

num.insert(2,0)
print(num)

num.pop()
print(num)

num.pop(2)
print(num)

if 5 in num:
    num.remove(5)
    print(num)
else:
    print('Não achei o número 4')

valores = []
valores.append(5)
valores.append(9)
valores. append(4)

for v in valores:
    print(f'{v}...')

for c,v in enumerate(valores):
    print(f' No valor {c} encontrei o valor {v}')

    print('\n')
    print('\n')

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f' No valor {c} encontrei o valor {v}')