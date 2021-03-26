# não soube fazer....peguei na python exercicios
from random import shuffle
def embaralha(nome):
    a = list(nome)
    shuffle(a)
    a = ''.join(a)
    print(a.lower())


nome = input('Digite algo: ')
embaralha(nome)