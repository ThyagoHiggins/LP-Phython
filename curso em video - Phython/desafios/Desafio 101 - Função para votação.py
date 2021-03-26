from datetime import datetime
#from datetime import date

def votacao(nasc):
    #atual = date.today().year
    idade = datetime.now().year - nasc

    if idade < 16:
        print(f'Com {idade}: NÃO VOTA')
        #return f'Com {idade}: NÃO VOTA' - possível fazer para todos.
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade}: VOTO OPCIONAL')
    else:
        print(f'Com {idade}: VOTO OBRIGATóRIO')


print('-'* 30)
ano = int(input('Em que ano você nasceu? '))
votacao(ano)
#print(voto(nasc))