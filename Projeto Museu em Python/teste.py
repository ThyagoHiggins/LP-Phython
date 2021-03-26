import sqlite3
from sqlite3 import Error

def criar(file_db):
    banco = sqlite3.connect('PinaQr.db')
    cursor =banco.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS ESCOLARIDADE (idCategoria_Doacao int ,nome_Escolaridade varchar(45),ESCOLARIDADECOL VARCHAR(45)")
    banco.commit()

    cursor.execute("SELECT*from table")
    print(cursor.fetchall())

if __name__ == '__main__':

    criar(r"C:\Users\Tiago\Desktop\Projeto\trabalho.db")