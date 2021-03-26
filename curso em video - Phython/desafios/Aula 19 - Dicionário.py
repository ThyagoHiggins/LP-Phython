pessoas = {'nome':'Gustavo', 'Sexo': 'M', 'idade': 22}
print(pessoas)

print()

pessoas = {'nome':'Gustavo', 'Sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['idade'])

print()

pessoas = {'nome':'Gustavo', 'Sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print()

pessoas = {'nome':'Gustavo', 'Sexo': 'M', 'idade': 22}
#Vai mostrar as chaves, ou seja, nome, sexo e idade
print(pessoas.keys())
#neste abaixo, vai mostrar os valores:
print(pessoas.values())
# neste aqui eu mostro todos os valores:
print(pessoas.items())

print()
#vamos navegar no dicionário:
for k in pessoas.keys():
    print(k)

print()
for v in pessoas.values():
    print(v)

print()

for k, v in pessoas.items():
    print(f'O {k} = {v} ')
print()
#podemos apagar pessoas...
#del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'O {k} = {v} ')
print()
#alterações tipo:
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'O {k} = {v} ')
print()
#adicionar:
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'O {k} = {v} ')