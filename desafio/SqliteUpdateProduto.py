import sqlite3

conn = sqlite3.connect('tabela.db')
valor = []
produto1 = str(input('nome do produto: '))
novo_valor = float(input('mudar valor: '))
valor.append(novo_valor)
valor.append(produto1)

def update():
    conn.execute("UPDATE pedidos SET valor = (?) WHERE produto = (?)", valor)
    conn.commit()

    conn.close()

atualizando = update()
atualizando
