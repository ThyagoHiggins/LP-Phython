from time import sleep


def maior(*num):
    m = i = 0
    for c in num:
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
        if c > m:
            m = c
    print(f'Os numeros escolhidos foram: {num}\n'
          f'sendo um total de {len(num)}'
          f'e o número maior é: {m}')
    print()




maior(2,9,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()


