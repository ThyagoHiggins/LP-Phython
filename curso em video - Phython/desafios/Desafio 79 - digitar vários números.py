num= list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')

    else:
        print('Valor duplicado!âo vou adicionar!')

    r = str(input('Quer continuar? [S/N]')).upper()
    if r in 'N':
        break

num.sort()
print(num)
