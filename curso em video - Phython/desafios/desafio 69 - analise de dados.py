id=masc=fmenor=0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade:  '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]:  ')).strip().upper()[0]
    if idade > 18:
        id += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fmenor += 1
    print('-' * 30)
    op = ' '
    while op not in 'SN':
     op = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print (f'Total de pessoas com mais de 18 anos : {id}\n'
       f'Ao todo temos {masc} homens cadastrados\n'
       f'E temos {fmenor} mulheres com menos de 20 anos')