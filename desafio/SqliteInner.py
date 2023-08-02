import sqlite3

conn = sqlite3.connect('tabela.db')

def ler():
    pedidosclientes = conn.execute("SELECT clientes.nome, pedidos.produto \
                    FROM clientes \
                    INNER JOIN pedidos ON clientes.id=pedidos.id")

    for i in pedidosclientes:
        print(i)

conn.close()

lendo = ler()
lendo
