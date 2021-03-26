pessoa = dict()
galera= list()
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
    while True:
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? S/N  ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)

print(f' A)Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f' B) A média de idade é de {média:5.2f} anos')
print(f'C) As mulheres cadastradas foram', end = ' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')
print(f'D) Listas de pessoas acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print ('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end= ' ')
        print()
print("AcABOU")