salario = float(input('Informe o salário a ser reajustado: R$  '))
reajuste = float(input('Informe a porcentagem de reajuste:  '))
per = (reajuste/100)+1

print(f'O salário de R$ {salario:.2f} com reajuste de {reajuste}% passar a ser R$ {salario*per:.2f}')