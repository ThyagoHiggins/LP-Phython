#confesso que não entendi o enunciado.... mas fiz + ou -

def taxaImposto(tx,valor):
    t = tx/100
    print()
    print(f'O indice para cálculo do imposto é:{t:.2f}')
    print(f'Logo o valor referente sobre o produto é: R$ {valor*t:.2f}')
    return valor*t

def soma_imposto(x,y):
    soma= x+y
    return soma


venda =float(input('Informe o valor do produto: R$ '))
imposto = int(input('Informe a porcentagem de Imposto em %: '))

valorimposto = taxaImposto(imposto, venda)
somei = soma_imposto(venda, valorimposto)
print(f'O custo para venda do produto será no total de: R$ {somei:.2f}')