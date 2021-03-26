conta = int( input('Informe o valor da conta: R$ '))
cont50 = cont10 = cont1 = 0

while conta >= 50:
    resto = conta-50
    conta = resto
    cont50 += 1
while conta >= 10:
    resto = conta-10
    conta = resto
    cont10 += 1
while conta >= 1:
    resto = conta-1
    conta = resto
    cont1 += 1

if cont1 > 0:
    print (F'São necessárias {cont1} notas de 1 real ')
if cont10 > 0:
    print (F'São necessárias {cont10} notas de 10 reais')
if cont50 > 0:
        print(F'São necessárias {cont50} notas de 50 reais ')