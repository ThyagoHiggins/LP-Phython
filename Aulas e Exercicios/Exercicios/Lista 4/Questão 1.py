string1 = str(input('Escreva uma frase: ')).strip()
string2 = str(input('Escreva outra frase: ')).strip()

print(f' A frase: {string1}, tem o tamanho de nº {len(string1)}')
print(f' A frase: {string2}, tem o tamanho de nº {len(string2)}')

if len(string1) == len(string2):
    print ('O tamanho das frases são iguais', end ='  ')
else:
    print('O tamanhos das frases são diferentes', end = ' ')

if string1 == string2:
    print ('e o seu conteudo também!!!', end = '  ')
else:
    print('com conteudo diferentes')