cont = ('zero', 'um','dois','três','quatro',
        'cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','cartoze',
        'quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')

while True:
    while True:
        num= int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end='')
    print (f'Você digitou o número {cont[num]}')
    op = str(input('Você deseja conitunar? S /  N: ')).upper()
    if op == 'N':
        break