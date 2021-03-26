nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1+nota2)/2

print(f'Considerando que você tirou {nota1} e {nota2}, a média é {media:.1f}')

if media < 5.0:
    print('O aluno está REPROVADO')
elif media > 5.0 and media < 6.9:
    print('O aluno está de RECUPERAÇão')
else:
    print('O aluno está APROVADO')