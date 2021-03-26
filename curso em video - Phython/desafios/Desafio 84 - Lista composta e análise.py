dados = list()
pessoas = list()
mai= men = 0
while True:
    dados.append(str(input('informe o Nome:')))
    dados.append(float(input('informe o Peso em KG: ')))

    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]


    pessoas.append(dados[:])
    dados.clear()

    cont = + 1
    op = str(input('Deseja continuar: [S/N]')).upper()
    if op == 'N':
        break

print(f' Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior foi de {mai}Kg o peso é do(a)', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor foi de {men}Kg o peso é do(a)', end=' ')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')