import sqlite3

conn = sqlite3.connect('tabela.db')
#novo_cliente = ('Gabriela', 'gabi@email.com')
#novo_pedido = ('Celular', '1500.00', 'Gabriela')
novo_cliente = []
nome = str(input('nome: '))
email = str(input('email: '))
novo_cliente.append(nome)
novo_cliente.append(email)

novo_pedido = []
produto = str(input('produto: '))
valor = float(input('valor: '))
novo_pedido.append(produto)
novo_pedido.append(valor)
novo_pedido.append(nome)



def inserindo_dados():

    conn.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', novo_cliente)

    conn.execute('INSERT INTO pedidos (produto, valor, cliente_id) VALUES (?, ?, (SELECT id FROM clientes WHERE nome = ?))', novo_pedido)

    conn.commit()

    conn.close()

inserir = inserindo_dados()
inserir