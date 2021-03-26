vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    print('VOCÊ FOI \033[1;31mMULTADO\033[m')
    multa = (vel-80)*7
    print(f'A multa irá custar R$ {multa:.2f}')
else:
    print('\033[1;32mTenha um ótimo dia! Dirija com Segurança!\033[m')