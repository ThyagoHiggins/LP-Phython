num= (int(input('Digite um número:  ')),
      int(input('Digite outro número:  ')),
      int(input('Digite mais um úmero:  ')),
      int(input('Digite último número:  ')))

print (f'Você digitou os seguintes números: {num}')
print(f'A quantidade do valor 9 foram {num.count(9)} vezes')
if 3 in num:
    print(f'A primeira posição em que foi digitado o nº 3 foi {num.index(3)+1}º')
else:
    print(f'Não foram digitados em nenhuma posição o nº 3')
print('Os valores pares digitados foram  ', end='')
for n in num:
    if n % 2 == 0:
        print(n,  end='  ')
