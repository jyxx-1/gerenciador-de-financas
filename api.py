from flask import Flask, jsonify, request, render_template
from gerenciador_financeiro import GerenciadorFinanceiro
from transacao import Transacao
import datetime

# Cria a aplicação Flask
app = Flask(__name__)

# Cria uma instância do nosso gerenciador
gerenciador = GerenciadorFinanceiro(db_name="financas.db")


# DEFINIÇÃO DAS ROTAS (ENDPOINTS) DA API >


# Rota para LISTAR todas as transações (MÉTODO GET)
@app.route("/transacoes", methods=["GET"])
def get_transacoes():
    """
    Endpoint para obter a lista de todas as transações.
    Acessível via GET http://127.0.0.1:5000/transacoes
    """
    # 1. Usamos nosso gerenciador para buscar os objetos do banco
    lista_de_objetos = gerenciador.listar_transacoes()

    # 2. Convertemos a lista de objetos Python em uma lista de dicionários
    #    para que possa ser transformada em JSON.
    lista_de_dicionarios = []
    for transacao in lista_de_objetos:
        lista_de_dicionarios.append(
            {
                "id": transacao.id,
                "descricao": transacao.descricao,
                "valor": transacao.valor,
                "data": transacao.data.isoformat(),  # Converte a data para string
            }
        )

    # 3. O Flask converte a lista de dicionários para o formato JSON
    return jsonify(lista_de_dicionarios)


# Rota para ADICIONAR uma nova transação (Método POST)
@app.route("/transacoes", methods=["POST"])
def add_transacao():
    """
    Endpoint para adicionar uma nova transação.
    Acessível via POST http://127.0.0.1:5000/transacoes
    """
    # 1. Pega os dados JSON enviados no corpo da requisição
    dados = request.get_json()

    # 2. Validação simples para garantir que os campos necessários foram enviados
    if (
        not dados
        or "descricao" not in dados
        or "valor" not in dados
        or "data" not in dados
    ):
        # Retorna um erro com o status code 400 (Bad Request)
        return (
            jsonify(
                {
                    "erro": "Dados incompletos. Campos necessários: descricao, valor, data"
                }
            ),
            400,
        )

    # 3. Tenta criar um objeto Transacao com os dados recebidos
    try:
        data_obj = datetime.date.fromisoformat(dados["data"])
        nova_transacao = Transacao(
            descricao=dados["descricao"], valor=float(dados["valor"]), data=data_obj
        )
        # 4. Usa o gerenciador para salvar a transação no banco
        gerenciador.adicionar_transacao(nova_transacao)

        # 5. Retorna uma resposta de sucesso com status code 201 (Created)
        return jsonify({"mensagem": "Transação criada com sucesso!"}), 201

    except (ValueError, TypeError) as e:
        # Se houver um erro na conversão dos dados (ex: data em formato inválido)
        return jsonify({"erro": f"Erro no formato dos dados {e}"}), 400


# Rota para atualizar uma transação baseada no seu ID (UPDATE)
@app.route('/transacoes/<int:id>', methods=['PUT'])
def update_transacao(id: int):
    """
    Endpoint para atualizar uma transação existente.
    Acessível via PUT http://127.0.0.1:5000/transacoes/ID_DA_TRANSACAO
    """

    dados = request.get_json()
    if not dados or 'descricao' not in dados or 'valor' not in dados or 'data' not in dados:
        return jsonify({'erro': 'Dados incompletos.'}), 400
    
    try:
        data_obj = datetime.date.fromisoformat(dados['data'])
        transacao_atualizada = Transacao(
            id=id,
            descricao=dados['descricao'],
            valor=float(dados['valor']),
            data=data_obj
        )
        gerenciador.atualizar_transacao(transacao_atualizada)
        return jsonify({'mensagem': f'Transação ID {id} atualizada com sucesso! 😉'})
    
    except (ValueError, TypeError) as e:
        return jsonify({'erro': f'Erro no formato dos dados: {e}'}), 400
    
# Rota para deletar uma transação baseada no seu ID (DELETE)
@app.route('/transacoes/<int:id>', methods=['DELETE'])
def delete_transacao(id: int):
    """
    Endpoint para deletar uma transação.
    Acessível via DELETE http://127.0.0.1:5000/transacoes/ID_DA_TRANSACAO
    """
    try:
        gerenciador.deletar_transacao(id)
        return jsonify({'mensagem': f'Transação ID {id} excluída com sucesso! 😉'})
    
    except Exception as e:
        # Uma exceção pode ocorrer se o ID não existir, por exemplo.
        return jsonify({'erro': f'Erro ao deletar transação {e}'}), 500
    
# Rota para servir a página principal (FRONT-END) >
@app.route('/')
def home():
    """
    Endpoint para servir a página principal da aplicação (o index.html).
    """
    return render_template('index.html')

# Se este arquivo for executado diretamente, inicie o servidor Flask
if __name__ == "__main__":
    # debug=True faz o servidor reiniciar automaticamente quando você salva o arquivo
    app.run(debug=True)
