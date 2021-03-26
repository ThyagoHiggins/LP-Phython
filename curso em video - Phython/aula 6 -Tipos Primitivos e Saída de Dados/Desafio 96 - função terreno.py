def linhas():
    print('-'*30)

def calculo(a,b):
    area = a*b
    print(f'A àrea de terreno de {a:.2f} x {b:.2f} é {area:.2f}')


print('Controle de Terrenos')
linhas()
l = float(input("LARGURA: "))
c= float(input(('COMPRIMENTO: ')))

calculo(l,c)
