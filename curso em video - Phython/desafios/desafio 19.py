import random
n1 = str(input('Primeiro Aluno '))
n2 = str(input('Segundo Aluno '))
n3 = str(input('Terceiro Aluno '))
n4 = str(input('Quarto Aluno '))
lista = [n1,n2,n3,n4]

print(f'O Aluno escolhido foi {random.choice(lista)}')