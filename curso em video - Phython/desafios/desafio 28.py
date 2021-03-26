from random import randint
from time import sleep

computador = randint(0,5) #computador pensa/escolhe
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO....')
sleep(1)
if jogador == computador:
    print('parabéns! Você me venceu!')
else:
    print(f'POxa eu pensei no número {computador} e você digitou {jogador}, GANHEI!')