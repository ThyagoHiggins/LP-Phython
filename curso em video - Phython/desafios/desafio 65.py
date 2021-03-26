opcao = ''
cont = soma = maior = menor= 0
while not opcao == 'N':
    num = int(input('Digite um número:  '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? [ S/N]  ')).upper().strip()[0]

print(f'Você digitou {cont} e a média foi {soma/cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
