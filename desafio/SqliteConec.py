import sqlite3

conn = sqlite3.connect('tabela.db')

def criar_tabelas():
 #primeira tabela com clientes
    conn.execute('''CREATE TABLE clientes (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                email TEXT
                    )
                ''')
 #segunda tabela com produtos
    conn.execute('''CREATE TABLE pedidos (
                id INTEGER PRIMARY KEY,
                cliente_id INTEGER,
                produto TEXT,
                valor REAL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
                    )
                ''')
 #salvando informações
    conn.commit()
 #fechando conexão
    conn.close()
#chamando função para executar
criando = criar_tabelas()
criando