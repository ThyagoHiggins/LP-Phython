print ('-'*30)
print ('ANÁLISE DE EMPRESTIMO')
print ('-'*30)
casa = float(input('Qual o valor da casa?  R$  '))
sal = float(input('Qual o valor do seu salário por mês? R$ '))
tempo = int(input(('Em quantos anos você deseja pagar a casa? ')))

parcela = casa/(tempo*12)
print(f'Para pagar uma casa no valor R$ {casa:.2f} em {tempo} anos a prestação será de R$ {parcela:.2f}')
valormax = sal*0.30

if parcela > valormax:
    print('DESCULPE! De acordo com o perfil informado não é possível aprovar o emprestimo')
else:
    print ('LEGAL!!! Seu emprestimo pode ser aprovado.')
