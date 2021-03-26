from random import randint
cont = 1
print('Sou seu computador')
pc = randint(0,10)
print ('Acabei de pensar em um número entre 0 e 10.\n'
       'Será que você consegue adivinhar qual foi?')
op = int(input('Qual o seu palpite: '))
while op != pc:

    if op < pc:
        print('Mais... Tente mais uma vez.')

    else:
        print ('Menos... tente mais uma vez.')
    cont += 1
    op = int(input('Qual o seu palpite: '))

print(f'Acertou {cont} tentativas. Parabéns!')