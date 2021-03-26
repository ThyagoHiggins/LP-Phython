cont = 0
num = int(input('Digite um número:  '))

for c in range(1,num+1):
    if num%c == 0:
        print('\033[34m', end =' ')
        cont = cont+1
    else:
        print('\033[31m', end = ' ')
    print(c, end=' ')

print (f'\n\33[mO número {num} foi divisivel {cont} vezes')
if cont > 2:
    print ('E por isso ele não é primo')
else:
    print ('O número é PRIMO!')