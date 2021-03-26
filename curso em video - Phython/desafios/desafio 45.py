from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print ('Sua opção:\n'
                     '[ 0 ] Pedra\n'
                     '[ 1 ] Papel\n'
                     '[ 2 ] Tesoura\n')
jogador = int(input('Qual é a sua jogada?  '))
print('-='*11)
print (f'O Computador jogou {itens[computador]}')
print (f'Jogador jogou {itens[jogador]}')
print ('-='*11)
if computador == 0:#pedra
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print ('Jogador Vence')
    elif jogador == 2:
        print ('Computador Vence')
    else:
        print('JOGADA INVALIDA')
if computador == 1:# papel
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print ('EMPATE')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('JOGADA INVALIDA')
if computador == 2:#tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print ('Computador Vence')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')