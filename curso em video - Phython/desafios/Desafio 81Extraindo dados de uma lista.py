valor = list()

while True:
    num = int(input('Digite um valor:'))
    valor.append(num)
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    if resp == 'N':
        break
print(valor)
print(f'Você digitou {len(valor)} elementos')

#outra forma de deixar de trás para frente
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valor}')

#print(f'Os valores em ordem decrescente são {valor[::-1]}')

if 5 in valor:
    print('Há o número 5 na lista')
else:
    print('O valor 5 não foi encontrado na lista')