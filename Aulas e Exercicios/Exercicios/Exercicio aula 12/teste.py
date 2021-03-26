nome = str(input('Nome:'))
nota1 = float(input('Informe 1º nota: '))
nota2 = float(input('Informe 2º nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    apto = 'Aprovado'
elif 5 <= media < 7:
    apto = 'FARÁ IFA'
else:
    apto = 'REPROVADO'
print(media)
print(apto)