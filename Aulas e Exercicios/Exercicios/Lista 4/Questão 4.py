frase = (str(input('Informe escreva uma frase: '))).upper().strip()


if frase.count('A') > 0:
    print (f'Na frase acima apareceu a vogal A por {frase.count("A")} vezes')
if frase.count('E') > 0:
    print (f'a vogal E por {frase.count("E")} vezes')
if frase.count('I') > 0:
    print (f'a vogal I por {frase.count("I")} vezes')
if frase.count('O') > 0:
    print (f'a vogal O por {frase.count("O")} vezes')
if frase.count('U') > 0:
    print (f'a vogal U por {frase.count("U")} vezes')

print(f' Há {frase.count(" ")} espaço(s) na frase')


