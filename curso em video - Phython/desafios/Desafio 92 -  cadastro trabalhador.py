from datetime import datetime
trabalhadores = dict()

trabalhadores['Nome: '] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
trabalhadores['idade'] = datetime.now().year - nasc
trabalhadores['carteira'] = int(input(f' Carteira de Trabalho (0 não tem)'))
if trabalhadores['carteira'] != 0:
    trabalhadores['contratação'] = int(input('Ano de Contratação: '))
    trabalhadores['Salário: '] = float(input('Salário: R$ '))
    trabalhadores['Aposentadoria'] = trabalhadores['idade'] + ((trabalhadores['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in trabalhadores.items():
    print(f' - {k} tem o valor {v}')


