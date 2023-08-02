import sqlite3

conn = sqlite3.connect('tabela.db')

nomelista = []
nome = str(input('cliente que deseja apagar: '))
nomelista.append(nome)

def delete():
    conn.execute("DELETE from clientes WHERE nome = (?)", nomelista)

    conn.commit()

    conn.close()

apagando = delete()
apagando