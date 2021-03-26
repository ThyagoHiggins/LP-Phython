def leiaint (num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!Digite um num inteiro valido.\033[m')
        if ok:
            break
    return valor




# programa principal

n = leiaint('Digite um número: ')
print(f'Voce digitou um o número {n}')