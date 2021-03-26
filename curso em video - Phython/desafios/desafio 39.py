from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = atual - ano

if idade < 18:
    print(f'Quem nasceu em {ano} tem {idade} em {atual}')
    print (f' Ainda faltam {18-idade} para o alistamento')
    print (f'Seu alistamento será em {ano+18}.')
else:
    print(f'Quem nasceu em {ano} tem {idade} em {atual}')
    print ('Você tem que se alistar IMEDIATAMENTE')