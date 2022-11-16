# importar o sqlite

import sqlite3

# conexão com o banco de dados

conexao = sqlite3.connect("dc_universe.db")

# criar um obejto do tipo cursor, é usado para colocar os comandos do SQL nele

cursor = conexao.cursor()

#comando SQL

sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

# botar comando no cursor

cursor.execute(sql)

# exibitr a consulta, fetchall = ele pega e guarda

pessoas = cursor.fetchall()

for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")