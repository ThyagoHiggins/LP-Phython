def byteparamb(quant):

    valor = quant/1048576
    final = str(round(valor, 2)).replace('.', ',')
    return

def per(esp, total):

    conta = esp*100/total
    valor2 = str(round(conta,2)).replace('.', ',')

arq = open('usuarios', 'r')
arquivo = arq.read().split('\n')

if len(arquivo) > 0:
    relatorio = open('relatorio.txt', 'wt')
    relatorio.write('ACME Inc.               Uso de Espaço em disco pelos usuários')
    relatorio.write("-"*70+"\n")
    relatorio.write('Nº'.ljust(5))
    relatorio.write('Usuário'.ljust(15))
    relatorio.write('Espaço utilizado'.ljust(21))
    relatorio.write('% do uso'.ljust(5))

    somadoespaco = 0



    for i in range(len(arquivo)):
        arquivo = arquivo[i].split()
        user = arquivo[0]
        space = arquivo[1]

        relatorio.write(str(i+1).ljust(5))
        relatorio.write(user.ljust(15))
        relatorio.write(byteparamb(space).rjust(7)+' MB     ')
        relatorio.write(per(space,somadoespaco).rjust(7)+'%  ')
    relatorio.write('\nEspaço total ocupado: '+ byteparamb(space)+ 'MB\n')
    relatorio.write('Espaço médio ocupado: '+byteparamb(space/len(arquivo))+'MB' )
    relatorio.close()