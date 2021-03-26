notas = list()

for n in range(0,4):
    notas.append((float(input(f'Informe o {n+1}º nota do aluno: '))))

print(f' As notas digitadas foram {notas}')
print(f'A média das notas é:{sum(notas)/4:.2f} ')

media = sum(notas)/4

if media >= 7:
    print('O Aluno foi aprovado')
if 4<media<7:
    print('O Aluno fará exame')
if media <= 4:
    print('O Aluno foi reprovado')