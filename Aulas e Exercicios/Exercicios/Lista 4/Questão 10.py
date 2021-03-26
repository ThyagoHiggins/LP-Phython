caracteres = list()
cont=0
for c in range(0,10):
    caracteres.append((str(input(f'Informe o {c+1}º caracter: '))))

print(caracteres)

for consoante in caracteres:
    if consoante  not in "aeiou":
        cont +=1
        print(consoante, end=' ')
print(f'\n Forma imprimidas {cont} consoantes')