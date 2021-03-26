def valorpagamento(p, a):
    valorfinal = (p*1.03) + (0.01*a)
    return valorfinal


cont = 0
somatotal = 0





while True:
    pagamento = float(input('Informe o valor:'))
    if pagamento == 0:
        break
    cont += 1

    atraso = int(input('Quantos dias de atraso: '))
    total = valorpagamento(pagamento, atraso)
    print(f'Valor reajustado é {total}')
    somatotal += total
    print('-='* 30)
print(f'Foram reajustadas {cont} parcelas e ficou num total de {somatotal}')

