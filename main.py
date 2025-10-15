import datetime

# Importa a CLASSE Transacao do MÓDULO transacao
from transacao import Transacao

# Importa a CLASSE GerenciadorFinanceiro do MÓDULO gerenciador_financeiro
from gerenciador_financeiro import GerenciadorFinanceiro


def exibir_menu():
    """
    Exibe o menu principal de opções ao usuário.
    """
    print("\n===== Gestor de Finanças Pessoais =====")
    print("1. Adicionar nova transação")
    print("2. Listar todas as transações")
    print("3. Exibir saldo atual")
    print("4. Sair")
    print("==============================================")


def adicionar_nova_transacao(gerenciador: GerenciadorFinanceiro):
    """
    Solicita os dados de uma nova transação ao usuário e a adiciona.

    A função inclui validações para garantir que o valor e a data
    sejam inseridos em formatos corretos, solicitando novamente se
    a entrada for inválida.

    Args:
        gerenciador (GerenciadorFinanceiro): A instância do gerenciador
        onde a nova transação será adicionada.
    """
    print("\n--- Adicionar Nova Transação ---")
    descricao = input("Descrição: ")

    # Loop para validação do valor inserido >
    while True:
        try:
            valor_str = input("Valor (use sinal de - para despesas, ex: -10.46): ")
            valor = float(valor_str)
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número (ex: 100.00 ou -25.30).")

    # Loop para validação da data >
    while True:
        try:
            data_str = input("Data (DD-MM-AAAA): ")
            data = datetime.datetime.strptime(data_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Formato de data inválido. Por favor, use DD-MM-AAAA.")

    nova_transacao = Transacao(descricao, valor, data)
    gerenciador.adicionar_transacao(nova_transacao)


# Ponto de Entrada Principal do Programa >
if __name__ == "__main__":
    gerenciador = GerenciadorFinanceiro(db_name="financas.db")

    while True:
        # O laço principal (coração da interatividade) executa repetidamente o menu
        # até que o usuário escolha a opção de sair.
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_nova_transacao(gerenciador)
        elif escolha == "2":
            transacoes_todas = gerenciador.listar_transacoes()
            if not transacoes_todas:
                print("\nNenhuma transação cadastrada.")
            else:
                print("\n--- Lista de Transações ---")
                for t in transacoes_todas:
                    print(t)
                print("---------------------------\n")
        elif escolha == "3":
            saldo = gerenciador.calcular_saldo()
            print(f"\n>> Saldo Atual: R${saldo:.2f}")
        elif escolha == "4":
            # Não precisamos mais salvar explicitamente! O banco já está atualizado.
            # Utilizando JSON, precisamos salvar as alterações antes de fechar o programa.
            print("\nObrigado por usar o Gerenciador de Finanças! Até logo 😉")
            break

        else:
            print("\nOpção inválida. Por favor, tente novamente.")
