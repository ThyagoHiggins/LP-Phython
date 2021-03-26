def arg(x):
    if x>0:
        resp = 'P'
    else:
        resp = 'N'
    return resp

num = int(input('Informe um número: '))
analise = arg(num)
print(f'O número {num} resultou no argumento {analise}')