from random import randint
def jogadados():
    return randint(2, 12)
while True:
    resp = str(input('Digite S para sair ou aperte enter para jogar dados:')).upper()
    if resp == 'S':
        break
    else:
        valor = jogadados()
        cont = 0
        print(valor)


        if valor == 7 or valor ==1:
            print(f'Dados: {valor}, GANHOU!!!')

        if valor == 2 or valor == 3 or valor == 12:
            if cont == 0:
                print(f'CRAPS, você perdeu!')

        if valor == 4 or valor == 5 or valor == 6 or valor == 8 or valor == 9 or valor == 10:
            print('PONTO')

        cont += 1

