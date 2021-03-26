cont = soma = a =  0

a = int(input('Digite um número [999] para parar]:  '))
while a != 999:
        soma += a
        cont += 1
        a = int(input('Digite um número [998] para parar]:  '))
print (f'Você digitou {cont} números e a soma entre eles foi {soma}. ')
