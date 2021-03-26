alunos = []

for c in range(0, 10):
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    nota3 = float(input('Nota 3:'))
    nota4 = float(input('Nota 4:'))

    print()
    print('-='*30)
    print()

    media = (nota1+nota2+nota3+nota4) / 4

    alunos.append([nome, [nota1, nota2, nota3, nota4], media])
print('-='*30)
print('Os alunos com média igual ou maior que 7 são: ')

for i, a in enumerate(alunos):
    if a[2] >= 7:
        print(f'{a[0]} com a média {a[2]}')
