cont= 0
cpf = str(input('Informe seu CPF (xxx.xxx.xxx-xx):  ')).strip()


if len(cpf) != 13:
    print(' Erro 1 : Quantidade de caracteres digitados fora do padrão!')
    cont +=1
if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
    print("Erro 2 : Estrutura errada use xxx.xxx.xxx-xx!")
    cont += 1
else:
    if len(cpf[:3]) != 3 or len(cpf[4:7]) != 3 or len(cpf[8:11]) != 3 or len(cpf[12:]) != 2:
        print('Erro 3: Quantidade de números incorreto, use o formato xxx.xxx.xxx.xx!')
        cont += 1
    else:
        print(f'{cpf} no formato válido')

print (f'Foram encontrados {[cont]} erros na digitação')

