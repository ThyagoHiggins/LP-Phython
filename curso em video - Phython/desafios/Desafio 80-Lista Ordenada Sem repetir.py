lista = []

for c in range(0, 5):
    n = int(input(f'Digite um número:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}da Lista...')
                break
            pos += 1
        print('-'*30)
        print(f'Os valores digitados em ordem foram: {lista}')

