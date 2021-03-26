from random import randint
cont = 0
print('Sou seu computador')
pc = randint(0,10)
print ('Acabei de pensar em um número entre 0 e 10.\n'
       'Será que você consegue adivinhar qual foi?')
acertou = False
while not acertou:
    op = int(input('Qual o seu palpite: '))
    cont += 1
    if pc == op:
        acertou = True
    else:
        if op < pc:
            print('Mais... Tente mais uma vez.')
        else:
            print ('Menos... tente mais uma vez.')

print(f'Acertou {cont} tentativas. Parabéns!')