def linhas(tam=25):
    return '-=' * tam


def cabeçalho(txt):
    print(linhas())
    print(txt.center(35))
    print(linhas())

def leiaInt(msg):
    while True:
        try:
            n= int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mErro: Usúario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def menu(lista):
    c = 1
    for opcao in lista:
        print(f'{c} - {opcao}')
        c += 1
    op = leiaInt('Qual Opção? ')
    return op