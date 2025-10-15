import sqlite3
import datetime
from transacao import Transacao


class GerenciadorFinanceiro:
    """
    Gerencia uma coleção de transações, interagindo com um banco de dados SQLite.
    """

    def __init__(self, db_name: str):
        """
        Inicializa o gerenciador financeiro.

        Args:
            db_name (str): O nome do banco de dados para carregar e salvar os dados.
        """
        # Cada método gerenciará sua conexão.
        self.db_name = db_name

    def _get_conexao(self):
        """Retorna uma conexão com o banco de dados."""
        return sqlite3.connect(self.db_name)

    def adicionar_transacao(self, transacao: Transacao):
        """Adiciona uma nova transação ao banco de dados."""
        conexao = self._get_conexao()
        cursor = conexao.cursor()

        # Usamos '?' para evitar injeção de SQL. É a forma segura!
        cursor.execute(
            "INSERT INTO transacoes (descricao, valor, data) VALUES (?, ?, ?)",
            (transacao.descricao, transacao.valor, transacao.data),
        )

        conexao.commit()
        conexao.close()
        print("Transação adicionada com sucesso! 🤝")

    def listar_transacoes(self) -> list[Transacao]:
        """
        Busca e retorna todas as transações do banco de dados.

        Args:
            id (int): Identificador da transação para armazenamento no banco de dados.
            descricao (str): A descrição da transação (ex: "Salário", "Aluguel").
            valor (float): O valor da transação. Positivo para receitas, negativo para despesas.
            data (datetime.date): A data em que a transação ocorreu.
        """
        conexao = self._get_conexao()
        # Garante que os resultados venham como objetos que permitem acesso por nome de coluna
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM transacoes ORDER BY data")
        linhas = cursor.fetchall()

        # Convertendo as linhas do banco de dados em objetos Transacao
        transacoes = []
        for linha in linhas:
            # A data vem do SQLite como string 'AAAA-MM-DD'
            data_obj = datetime.date.fromisoformat(linha["data"])
            transacoes.append(
                Transacao(
                    id=linha["id"],
                    descricao=linha["descricao"],
                    valor=linha["valor"],
                    data=data_obj,
                )
            )

        conexao.close()
        return transacoes

    def calcular_saldo(self) -> float:
        """Calcula o saldo total diretamente no banco de dados."""
        conexao = self._get_conexao()
        cursor = conexao.cursor()

        # O SQL pode fazer a soma. Torna muito mais eficiente.
        cursor.execute("SELECT SUM(valor) FROM transacoes")

        # O fetchone() busca apenas o primeiro resultado
        resultado = cursor.fetchone()

        conexao.close()

        # Se não houver transações, o resultado é None
        saldo = resultado[0] if resultado[0] is not None else 0.0
        return saldo

    def atualizar_transacao(self, transacao: Transacao):
        """Atualiza uma transação existente no banco de dados com base no seu ID."""
        conexao = self._get_conexao()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE transacoes
            SET descricao = ?, valor = ?, data = ?
            WHERE id = ?
            """,
            (transacao.descricao, transacao.valor, transacao.data, transacao.id),
        )

        conexao.commit()
        conexao.close()

    def deletar_transacao(self, id: int):
        """Deleta uma transação do banco de dados com base no seu ID."""
        conexao = self._get_conexao()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM transacoes WHERE id = ?", (id,))

        conexao.commit()
        conexao.close()
