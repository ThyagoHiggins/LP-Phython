alunos= dict()

alunos['Nome'] = str(input('Nome: ')).upper()
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))

print('-='*30)

if alunos['Média'] >= 7:
    alunos['Situação '] = 'Aprovado'
elif 5 < alunos['Média'] < 7:
        alunos['Situação '] = 'Recuperação'
else:
    alunos['Situação '] = 'Reprovado'
print('-='*30)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')

