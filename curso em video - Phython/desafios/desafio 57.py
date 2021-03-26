sexo = str(input('Informe o sexo [M/F] : ')).strip().upper()[0]

'''while sexo != 'F' and sexo != 'M':'''
while sexo not in 'MF':
    print ('Voce digitou opção errada!')
    sexo = str(input('Informe o sexo [M/F] : ')).upper()