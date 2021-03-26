jogador = dict()
gols = list()
time= list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou?   '))
    gols.clear()
    for c in range(0, tot):
        gols.append(int(input(f'Quantos gols na {c+1}º partida? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    time.append(jogador.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda S ou N:')
    if resp == 'N':
        break

print('-'*40)

print('Cod ', end='  ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca= int(input('Motrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- Levantamento do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate (time[busca]['gols']):
            print(f'   NO jogo {i+1} fez {g} gols.')
print('-'*40)






