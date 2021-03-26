soma = 0
cont = 0
for c in range (1,7):
    n = int(input(f'Informe o {c}º  '))
    if n%2 == 0:
        soma = soma + n
        cont = cont + 1


print (f'Você informou {cont} números e a soma foi {soma}')

