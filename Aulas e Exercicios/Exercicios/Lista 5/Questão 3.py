def soma(lista):
    total = sum(lista)
    return total



# Programa

arg = list()
for c in range(0, 3):
    arg.append((int(input(f'Informe o {c+1}º número: '))))

soma(arg)

print(f'A soma é {soma(arg)}')