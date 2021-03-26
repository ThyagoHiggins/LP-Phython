num1 = int(input('Primeiro número:  '))
num2 = int(input('Segundo número:  '))

if num1 > num2:
    print ('O primeiro número é maior')
elif num1 < num2:
    print ('O segundo número o maior')
elif num1 == num2: #Considerando que não há outra opção, poderia ter colocado somente 'else'
    print ('Os números são iguais')