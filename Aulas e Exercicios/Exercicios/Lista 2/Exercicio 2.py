vendas = float(input('Informe seu valor de vendas: R$  '))

if vendas <= 5000:
    comissao = vendas*0.02
    print(f' O valor da sua comissão este mês é {comissao:.2f}')

elif vendas >= 5000.01 and vendas <= 10000:
    comissao = vendas * 0.05
    print(f' O valor da sua comissão este mês é {comissao:.2f}')

elif vendas >= 10000.01 and vendas <= 15000:
    comissao = vendas * 0.07
    print(f' O valor da sua comissão este mês é {comissao:.2f}')

elif vendas >= 15000.01:
    comissao = vendas * 0.09
    print(f' O valor da sua comissão este mês é {comissao:.2f}')


