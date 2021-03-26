def ficha (n, g):
    if n == '' and g == '':
        print(f'O <jogador desconhecido> fez 0 gols')
    elif g == '':
        print(f'O jogador {n} fez 0 gols')
    elif n == '':
        print(f'O <jogador desconhecido> fez {g} gol(s)')
    else:
        print(f'O jogador {n} fez {g} gol(s)')



print('-='* 30)
nome = str(input('Nome do Jogador: '))
gol = str(input(('Número de gols: ')))
if gol.isnumeric():
    gol = int(gol)
else:
    gol= 0

ficha(nome, gol)