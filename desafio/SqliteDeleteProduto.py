import sqlite3

conn = sqlite3.connect('tabela.db')


produtolista = []
produto = str(input('produto que deseja apagar: '))
produtolista.append(produto)
def delete():
    conn.execute("DELETE from pedidos WHERE produto = (?)", produtolista)

    conn.commit()

    conn.close()

apagando = delete()
apagando