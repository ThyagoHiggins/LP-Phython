somaidade = 0
maioridade= 0
cmulher = 0

for i in range(1,5):
    print(f'------ {i}º PESSOA ------')

    nome = str(input('Nome: ')).strip()

    idade = int(input('Idade: '))
    somaidade = somaidade + idade

    sexo = str (input('Sexo [M/F]: ')).upper().strip()

    if sexo == 'M':
        if i == 0:
            maioridade = idade
        else:
            if idade > maioridade:
                maioridade = idade
                nomemaior = nome
    else:
        if idade < 20:
            cmulher = cmulher + 1


print(f'A média de idade do grupo é de {somaidade/4:.1f}')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomemaior}')
print(f'Ao todo são {cmulher} mulheres com menos de 20 anos')