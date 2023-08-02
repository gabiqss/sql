import sqlite3

conn = sqlite3.connect('tabela.db')
def ler():
    pedidos = conn.execute('SELECT * from pedidos')
    clientes = conn.execute('SELECT * from clientes')

    for i in pedidos:
        print(i)

    for i in clientes:
        print(i)

    conn.close()

lendo = ler()
lendo