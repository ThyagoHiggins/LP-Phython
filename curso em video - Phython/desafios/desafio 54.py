from datetime import date

contmaior = 0
contmenor = 0
atual = date.today().year

for c in range(1,8):
    n = int(input(f'Em que ano a {c}º pessoa nasceu?  '))
    idade = atual - n
    if idade > 18:
        contmaior = contmaior+1
    else:
        contmenor = contmenor+1
print(f'Ao todo tivemos {contmaior} maiores de idade\n'
      f'E também tivemos {contmenor} menores de idade')