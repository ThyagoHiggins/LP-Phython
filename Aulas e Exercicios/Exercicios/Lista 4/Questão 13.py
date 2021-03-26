carro = []
from time import sleep
menor = 0
for c in range(0, 5):
    marca = str(input(f'Informe a marca: '))
    mediaporl = float(input(f'Quantos Km por litro ele faz: '))
    litros = 1000/mediaporl
    gasolina = litros*2.5
    print('-='*30)

    if menor == 0:
        menor = gasolina
    else:
        if gasolina < menor:
            menor = gasolina
    carro.append([marca, mediaporl, litros, gasolina])

print(f'Considerando uma distancia de 1000 Km...')
sleep(1)
print('Considerando a gasolina a R$ 2,50...')
sleep(1)
print('_+'*30)
print('Calculando dados....')
sleep(2)
print('_+'*30)
print(f'{"No.":<4}{"Marca":<10}{"Consumo km/l":>16}{" Litros":>16}{" total gasto":>16}')


print('-'*26)

for i, c in enumerate(carro):
    print(f'{i:<4}{c[0]:<6}{c[1]:>16.2f}{c[2]:>16.2f}{c[3]:>16.2f}')
print()
for m in carro:
    if m[3] == menor:
        print(f' O menor consumo é o {m[0]}')