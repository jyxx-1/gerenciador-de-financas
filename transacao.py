import datetime


class Transacao:
    """
    Representa uma única transação financeira, que pode ser uma receita ou uma despesa.
    Agora inclui um 'id' opcional para integração com o banco de dados.
    """

    def __init__(
        self, descricao: str, valor: float, data: datetime.date, id: int = None
    ):
        """
        Inicializa um objeto de Transacao.

        Args:
            id (int): Identificador da transação para armazenamento no banco de dados.
            descricao (str): A descrição da transação (ex: "Salário", "Aluguel").
            valor (float): O valor da transação. Positivo para receitas, negativo para despesas.
            data (datetime.date): A data em que a transação ocorreu.
        """
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.data = data

    def __repr__(self):
        """
        Retorna uma representação em string do objeto, útil para debugging e exibição.
        """
        data_formatada = self.data.strftime("%d-%m-%Y")
        sinal = "+" if self.valor >= 0 else ""
        # Adicionamos a exibição do ID para facilitar o debug
        id_str = f" (ID: {self.id})" if self.id else ""
        return (
            f"[{data_formatada}] {self.descricao}{id_str}: R$ {sinal}{self.valor:.2f}"
        )
