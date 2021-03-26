n1 = float(input("Insira a nota 1   "))
p1 = float(input("Insira peso para nota 1   "))
n2 = float(input("Insira a nota 2   "))
p2 = float(input("Insira para peso para nota 2   "))
n3 = float(input("Insira a nota 3    "))
p3 = float(input("Insira o peso da  nota 3   "))

mediapon = (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3)



print (f'A sua primeira nota é {n1} e ela tem o peso de {p1}\n Já a sua segunda nota é {n2} e o peso dela é {p2}\n por fim sua terceira nota foi {n3} com peso {p3} \n  Sua média é {mediapon}')
