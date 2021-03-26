frase = str(input('Escreva uma frase:  ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
print (f' O inverso de {frase} é {inverso}')
if inverso == junto:

    print('TEMOS UM PALINDROMO')
else:
    print('A frase digitada não é um palindromo')