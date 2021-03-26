import random
import time
banco=['cabeca', 'gato', 'elefante', 'eletronico']
while True:
    print('-='*30)
    print('JOGO DA FORCA')
    print('-='*30)
    print()

    print(f' 1 - Cadastrar palavras\n'
          f' 2 - Jogar\n'
          f' 3 - Sair')
    resp = int(input('Escolha uma opção:  '))

    if resp == 3:
        break
    if resp == 1:
        palavra = str(input('Informe a palavra para cadastro:')).upper().strip()
        banco.append(palavra[:])
        palavra = ''

    if resp == 2:
        sorteio = random.choice(banco)
        print(f'Sorteando palavra:')
        time.sleep(2)
        print('Vamos começar:')

        digitadas = []
        acertos = []
        erros = 0
        while True:
            escolhida = ''
            for letra in sorteio:
                escolhida += letra if letra in acertos else "."
            print(escolhida)
            if escolhida == sorteio:
                print("Você acertou!")
                break
            tentativa = input("\nDigite uma letra:").lower().strip()
            if tentativa in digitadas:
                print("Você já tentou esta letra!")
                continue
            else:
                digitadas += tentativa
                if tentativa in sorteio:
                    acertos += tentativa
                else:
                    erros += 1
                    print("Você errou!")
            print("X==:==\nX  :   ")
            print("X  O   " if erros >= 1 else "X")
            linha2 = ""
            if erros == 2:
                linha2 = "  |   "
            elif erros == 3:
                linha2 = " \|   "
            elif erros >= 4:
                linha2 = " \|/ "
            print("X%s" % linha2)
            linha3 = ""
            if erros == 5:
                linha3 += " /     "
            elif erros >= 6:
                linha3 += " / \ "
            print("X%s" % linha3)
            print("X\n===========")
            if erros == 6:
                print("Enfrcado!")
                break

