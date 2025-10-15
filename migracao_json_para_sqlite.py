# Arquivo: migracao_json_para_sqlite.py

import json
import sqlite3
import datetime

# --- CONFIGURAÇÕES ---
ARQUIVO_JSON = "financas.json"
BANCO_DADOS = "financas.db"

# --- LÓGICA DO SCRIPT ---

print("Iniciando migração de dados do JSON para o SQLite...")

# 1. Carregar os dados do arquivo JSON
try:
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        dados_json = json.load(f)
    print(f"{len(dados_json)} registros encontrados no arquivo JSON.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{ARQUIVO_JSON}' não foi encontrado. Abortando migração.")
    exit()  # Encerra o script

# 2. Conectar ao banco de dados SQLite
# O 'with' garante que a conexão será fechada automaticamente no final
with sqlite3.connect(BANCO_DADOS) as conexao:
    cursor = conexao.cursor()

    # 3. Iterar sobre os dados e inserir no banco
    transacoes_migradas = 0
    for transacao_json in dados_json:
        # Converte a string de data do JSON para um objeto date
        data_obj = datetime.date.fromisoformat(transacao_json["data"])

        # Monta os dados para inserção
        dados_para_inserir = (
            transacao_json["descricao"],
            transacao_json["valor"],
            data_obj,
        )

        # Executa o comando INSERT
        cursor.execute(
            "INSERT INTO transacoes (descricao, valor, data) VALUES (?, ?, ?)",
            dados_para_inserir,
        )
        transacoes_migradas += 1
        print(f"  -> Migrando: '{transacao_json['descricao']}'")

# O commit é feito automaticamente ao sair do bloco 'with'

print("\n-------------------------------------------")
print(f"Migração concluída com sucesso!")
print(f"Total de {transacoes_migradas} transações transferidas para '{BANCO_DADOS}'.")
print("-------------------------------------------")
