from datetime import date
print ('='*30)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print ('='*30)
print('INDICADOR DE CATEGORIA: ')
print('-'*30)
ano = int(input('Informe o ano de nascimento:  '))
atual = date.today().year
idade= atual - ano
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and  idade <= 14: #podia ser somente idade <= 14 em todas as categorias...
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
else:
     print('Classificação: MASTER')
