times = ('Internacional','Flamengo','São Paulo', 'Palmeiras',
         'Atletico MG', 'Vasco','Fluminense','Santos','Ceará',
         'Corinthians','Fortaleza','Bahia','Botafogo','Athletico-PR',
         'Sport','Coritiba','Grêmio', 'Bragantino', 'Atletico - Go',
         'Goiás')

print ('*'*30)
#print(f'A lista de times do Brasileirão: {times}')
for t in times:
    print(f'{t}')

print('-='*30)
print(f' A lista dos 5º primeiros são:v {times[0:5]}')
print('-='*30)
#print(f' Os times na zona de rebaixamento são: {times[16:20]}')
print(f' Os times na zona de rebaixamento são: {times[-4:]}')

print('-='*30)
print(f' Os times em ordem alfabética {sorted(times)}')

print('-='*30)
print(f'O Santos está na {times.index("Santos")+1}ª posição')