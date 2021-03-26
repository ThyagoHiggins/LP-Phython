valoraula = float(input(f'informe o valor da hora aula: '))

quantidadedeaulas = float(input(f'Informe a quantidade de hora aula dada: '))

inss = float(input(f'Informe a porcentagem de desconto ( 1 a 100): '))

descontoinss = inss/100

print (f'O seu salário bruto é {round(quantidadedeaulas*valoraula,2)}')
print (f'O valor do desconto de INSS é {round(descontoinss*quantidadedeaulas*valoraula,2)}')
print (f'Você receberá  {round((quantidadedeaulas*valoraula) - (descontoinss*quantidadedeaulas*valoraula),2)}')