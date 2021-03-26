print('='*20, end ='')
print('LOJAS HIGGINS', end = '')
print('='*20)

preco = float (input('Preço da compra: R$  '))
print ('FORMAS DE PAGAMENTO\n'
       '[ 1 ] à vista dinheiro/cheque\n'
       '[ 2 ] à vista cartão\n'
       '[ 3 ] 2x no cartão\n'
       '[ 4 ] 3x ou mais no cartão\n')
op = int(input('Opção: '))
if op == 1:
    print (f'O preço final é R$ {preco*0.90:.2f}')
elif op == 2:
    print (f'O preço final é R$ {preco*0.95:.2f}')
elif op == 3:
    print (f'O valor a pagar em 2x é R$ {preco/2:.2f}')
elif op == 4:
    precojuros = preco*1.20
    parcela = int(input(f'Em quantas vezes:  '))
    print (f'Sua compra ficará em  {parcela}x R$ {precojuros/parcela:.2f}  ')
    print(f'Sua compra de {preco:.2f} terá o valor final de {precojuros:.2f}')

