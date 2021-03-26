sal = float(input('Informe o salário: R$  '))

if sal <= 600.00:
    desconto= sal*0.07
    print(f'O valor de contribução ao INSS é de {desconto:.2f}\n'
          f'Logo seu Salário final é R$ {sal-desconto:.2f}')

if sal >= 600.01 and sal <= 800:
    desconto = sal * 0.08
    print(f'O valor de contribução ao INSS é de {desconto:.2f}\n'
          f'Logo seu Salário final é R$ {sal - desconto:.2f}')

if sal >= 800.01 and sal <= 1200:
    desconto = sal * 0.09
    print(f'O valor de contribução ao INSS é de {desconto:.2f}\n'
          f'Logo seu Salário final é R$ {sal - desconto:.2f}')

if sal >= 1200.01:
    desconto = sal * 0.11
    print(f'O valor de contribução ao INSS é de {desconto:.2f}\n'
          f'Logo seu Salário final é R$ {sal - desconto:.2f}')