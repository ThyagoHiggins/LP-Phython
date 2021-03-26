num = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha a seguinte opção:\n [ 1 ] Converter para Binário\n [ 2 ] Converter para Octal\n '
                  '[ 3 ] Converter para hexadecimal\n'
                  'Sua opção:  '))
if opcao == 1:
    print(f'O número {num} convertido em Binário é {bin(num)[2:]}')
elif opcao == 2:
        print(f'O número {num} convertido em OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido em Hexadecimal é {hex(num)[2:]}')
else:
    print('Meu filho!!! Opção errada, TCHAU!')