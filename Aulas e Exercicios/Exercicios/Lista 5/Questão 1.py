def linha(v):
    c=1
    from random import randint
    for c in range(1, v+1):
         if c <= v:
             print(f'{c}'*c)



num = int(input('Informe um número: '))
linha(num)