import math
g= 9.80665

velo = float(input('Informe a velocidade em KM: '))
converte = velo*1000

ang = int(input('Informe o angulo: '))

radiano = math.radians(ang)
sen = math.sin(radiano)

S = ((2*converte)/g)*sen
final = S/1000

print (f'O alcance será de {final:.2f} km')