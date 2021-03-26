from time import sleep

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'ERRO ao CRIAR')
    else:
        print(f'Arquivo {nome} criado')



# principal
ips= list()
arq = 'ip.text'
if arquivoExiste(arq):
    print('Arquivo encontrado')
else:
    print('O arquivo será criado...')
    sleep(1)
    criararquivo(arq)

a = open('ip.text', 'r')
ips = a.readlines()
a.close()

ipok = " "
iperror =""

for i in range (len(ips)):

    ips2 = ips[i].rsplit(".")
    if (int(ips2[0])<=255 and int(ips2[1])<=255 and int(ips22[2])<=255 and int(ips2[3])<=255):

        ipok += ips[i]

    else:

        iperror += ips[i]

a = open('ip.text', 'wt')
a.write(f'Os ip válidos são:')
a.write(ipok)
a.close()

a = open('ip.text', 'wt')
a.write(f'Os ip  não válidos são:')
a.write(iperror)
a.close()

