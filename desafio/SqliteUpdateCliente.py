import sqlite3

conn = sqlite3.connect('tabela.db')
nome1 = str(input('nome: '))
email = []
novo_email = str(input('novo email: '))
email.append(novo_email)
email.append(nome1)

def update():
    conn.execute("UPDATE clientes SET email = (?) WHERE nome = (?)", email)

    conn.commit()

    conn.close()

atualizando = update()
atualizando
