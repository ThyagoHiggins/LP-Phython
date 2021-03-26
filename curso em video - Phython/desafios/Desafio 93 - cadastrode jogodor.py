jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do jogador: '))

tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou?   '))

for c in range(0, tot):
    gols.append(int(input(f'Quantos gols na {c+1}º partida? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-='*30)

print(jogador)

print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')


