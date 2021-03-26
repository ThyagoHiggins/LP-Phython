op = False

n1 = int(input('Primeiro valor:  '))
n2=  int(input('Segundo valor:  '))

while not op:
    print(' [ 1 ] somar\n'
          ' [ 2 ] mutiplicar\n'
          ' [ 3 ] maior\n'
          ' [ 4 ] Novos números\n'
          ' [ 5 ] Sair do programa')
    opt = (int(input('>>>>> Qual é a sua opção?')) )
    if opt == 5:
        op = True
        print('Você escolheu terminar o programa')
    else:
        if opt == 1:
            print(f'A soma entre {n1} + {n2} é {n1+n2}')

        if opt == 2:
            print(f'A Multiplicação  entre {n1} X {n2} é {n1 * n2}')
        if opt == 3:
            if n1 == n2:
                print('O número é igual')
            else:
                if n1>n2:
                    print(f'O maior é {n1}')
                else:
                        print(f'O maior é {n2}')
        if opt == 4:
            n1 = int(input('Primeiro valor:  '))
            n2 = int(input('Segundo valor:  '))
        print('=-'*30)
