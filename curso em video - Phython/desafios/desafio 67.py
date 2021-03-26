cont = 1
while True:
    tabu = int(input("Quer ver a tabuada de qual valor?  "))
    if tabu < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    print('-'*30)
    for cont in range(1,11):
        print(f'{tabu} x {cont:} = {tabu*cont}')
    print('-' * 30)

    if tabu < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break