# importar o sqlite

import sqlite3

# conexão com o banco de dados

conexao = sqlite3.connect("dc_universe.db")

# criar um obejto do tipo cursor, é usado para colocar os comandos do SQL nele

cursor = conexao.cursor()

# comando para inserir um heroi/vilão

sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

# executar o comando SQL

cursor.execute(sql)

#confirmar o insert com o commit() e fechar o banco

conexao.commit()
conexao.close()

