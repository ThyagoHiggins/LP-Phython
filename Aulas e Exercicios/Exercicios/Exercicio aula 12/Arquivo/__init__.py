from Funcao import *


def temarquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado!')


def cadastrar(arq, nome='desconhecido', nota1=0, nota2=0, media=0, apto="semdados"):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{nota1};{nota2};{media};{apto}\n')
        except:
            print('Houver um problema no cadastramento')
        else:
            print('Cadastro realizado')
        a.close()


def ler(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possivel acessar arquivo')
    else:
        cabeçalho('Alunos Cadastrados')
        for c in a:
           dado = c.split(';')
           print(f'{dado[0]:<8}nota 1: {dado[1]:<8}nota 2: {dado[2]:<8}'
              f'media:  {dado[3]:<8} Situação: {dado[4]:<8}')


    finally:
        a.close()
