import sqlite3

# 1. Conecta ao banco de dados (cria o arquivo se ele não existir)
conexao = sqlite3.connect("financas.db")

# 2. Cria um objeto "cursor" que permite executar comandos SQL
cursor = conexao.cursor()

# 3. Executa o comando SQL para criar a tabela "transacoes"
# Usamos """ para poder quebrar a linha e deixar o comando mais legível
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data DATE NOT NULL
    )
"""
)

# 4. Confirma a execução do comando (salva as alterações)
conexao.commit()

# 5. Fecha a conexão com o banco de dados
conexao.close()

print("Banco de dados e tabela 'transacoes' criados com sucesso!")
