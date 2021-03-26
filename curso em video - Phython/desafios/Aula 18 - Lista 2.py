#configuração de lista dentro de lista
teste= list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)

print(galera)

#adicionando dados
teste= list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
#pq não funcionou? se dá append eu ligo as duas estruturas... se muda um muda outro
#logo preciso fazer um cópia
teste= list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# fazer lista por lista
galera = [['João', 19],['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])

#trabalhando com estrutura
for p in galera:
    print(p)

for p in galera:
    print(p[0])

for p in galera:
    print(p[1])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

#pegando dados
galera= list()
dado= list()

for c in range(0,3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade;')))
    galera.append((dado[:]))
    dado.clear()

print(galera)

#outro exemplo
galera = list()
dado = list()
menor = maior = 0

for c in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade;')))
    galera.append((dado[:]))
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade')