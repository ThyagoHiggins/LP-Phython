text = 'ip.text'
ip = open('ip.text', 'r')
analise = []
ipcerto=[]
iperrado = []
re1 = []
re2=[]

#abro o arquivo para poder colocar os dados em uma lista sem espaços usando
#a funçaõ strip()
for linha in ip:
    linha = linha.strip()
    analise.append(linha)
ip.close()

#depois percorro com o indice c dentro da tamanho da lista. Jogo os dados
#em outra lista 'verifica' e separo os dados a cada '.'
for c in range(len(analise)):
    verifica = analise[c].split('.')

#foi necessário transformar os dados o foram separados em inteiro para fazer
#analise de comparação,pois se fosse string não haveria possibilidade

    if int(verifica[0])<= 255 and int(verifica[1])<= 255 and int(verifica[2])<= 255 and int(verifica[3]) <= 255:
        ipcerto.append(verifica)

    else:
        iperrado.append(verifica)

#aqui criei duas listas para alocar os ips certo e errados, juntando com o '.'
#novamente

for j in range(len(ipcerto)):
    f = ".".join(ipcerto[j])
    re1.append(f)

for t in range(len(iperrado)):
    v = ".".join(iperrado[t])
    re2.append(v)
a =str(re1)
b=str(re2)

print(re1)
print(re2)

ip = open('ip.text', 'wt')
ip.write('Endereço válido\n')
ip.write(a+'\n')
ip.write('Endereço válido\n')
ip.write(b+'\n')
ip.close()

