def converter(h, m):
    t=0
    if h >= 12:
        t = h-12

    if h > 12:
         print(f"A hora informada pode ser: {t}:{m} P.M")
    if h < 12:
         print(f'A hora informada pode ser: {h}:{m} A.M')




while True:

    hora = int(input('informe a hora(h): '))
    min = int(input('informe os minutos: '))
    print()

    converter(hora, min)

    resp = int(input('Aperte 0 para finalizar  ou 1 para continuar: ') )
    if resp == 0:
        break
    else:
        print('-='*30)