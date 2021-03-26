print('='*30),
print('10 TERMOS DE UMA PA:')
print('='*30)

a1= int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = a1 + (10-1)*razao

for i in range(a1,decimo+1,razao):
    print(i, end=' > ')
print('ACABOU')