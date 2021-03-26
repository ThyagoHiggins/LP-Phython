from Funcao import *
from Arquivo import *
from time import sleep

arq = 'notas.text'

if temarquivo(arq):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')
    criar(arq)

while True:

    linhas()
    cabeçalho('MENU DE NOTAS')
    linhas()
    resp = menu(['Cadastrar Aluno', 'Mostrar Alunos', 'Sair'])

    if resp == 1:
        cabeçalho('Novo Cadastro de Aluno')
        nome = str(input('Nome:'))
        nota1 = float(input('Informe 1º nota: '))
        nota2 = float(input('Informe 2º nota: '))
        media = (nota1+nota2)/2
        if media >= 7:
            apto = 'Aprovado'
        elif 5 <= media < 7:
            apto = 'FARÁ IFA'
        else:
            apto = 'REPROVADO'

        cadastrar(arq, nome, nota1, nota2, media, apto)

        print()
        print('-='*30)
    if resp == 2:
        ler(arq)
    if resp == 3:
        print('Encerrando...')
        sleep(0.5)
        print('ACABOU')
        break
