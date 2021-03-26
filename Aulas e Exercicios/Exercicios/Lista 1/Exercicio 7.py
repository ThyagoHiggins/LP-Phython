print(f' Vamos calcular a velocidade de um projetil')
dist = float(input("Qual foi a distancia (em Km)?"))
tempo = float(input("quanto tempo (em min)?"))
vm1 = float(dist/tempo)
vmms = float(vm1*16.667)

print(f"A velocidade em m/s do projétil é {round(vmms,2)}")