from desafio115.libi.interface import *
from desafio115.libi.arquivo import *
from time import sleep
import os
arq = 'pessoas.text'

if arquivoExiste(arq):
    print(f'Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)


while True:

    resposta = menu(['Ver pessoas', 'Cadastrar novas Pessoas',
       'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar o conteúdo de um arquivo
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade:')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho ('Saindo do Sistema... Até Logo')
        break

    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
