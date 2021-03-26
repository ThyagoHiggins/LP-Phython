jogador = dict()
gols = list()
time = list()

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou?   '))

    for c in range(0, tot):
        gols.append(int(input(f'Quantos gols na {c+1}º partida? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continar? [ S/N ]:  ')).upper()[0]
        if resposta in 'SN':
            break
    if resposta == 'N':
        break

print('-' * 30)
print('cod ', end='')
#busca os valores da tabela
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
    print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código{busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1} fez {g} gols.')
    print('-'*40)



