# Aurora - Sua Gestora de Finanças Pessoais ✨

🇧🇷 Português

Aurora é uma aplicação web full-stack de gerenciamento de finanças pessoais, construída do zero. O projeto permite ao usuário controlar suas receitas e despesas de maneira simples e intuitiva, através de uma interface web dinâmica que se comunica com uma API robusta e um banco de dados relacional.

🇺🇸 English

Aurora is a full-stack personal finance management web application, built from scratch. The project allows users to control their income and expenses in a simple and intuitive way, through a dynamic web interface that communicates with a robust API and a relational database.

🚀 Funcionalidades Principais (Features)

✅ Adicionar novas transações (receitas ou despesas).

✅ Listar todas as transações de forma organizada.

✅ Atualizar os dados de uma transação existente.

✅ Deletar transações que não são mais necessárias.

✅ Interface de usuário reativa que atualiza sem a necessidade de recarregar a página.

✅ Persistência de dados em um banco de dados SQLite.

# 🛠️ Tecnologias Utilizadas (Tech Stack)

Back-end: Python, Flask

Banco de Dados: SQLite

Front-end: HTML5, CSS3, JavaScript (vanilla)

Ambiente: Ambientes Virtuais (venv)

⚙️ Como Executar o Projeto (Getting Started)

Siga os passos abaixo para executar o projeto em sua máquina local.

1. Clone o Repositório

git clone [https://github.com/jyxx-1/gerenciador-de-financas.git](https://github.com/jyxx-1/gerenciador-de-financas.git)
cd nome-do-repositorio


2. Crie e Ative o Ambiente Virtual (venv)

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate


3. Instale as Dependências
Este projeto utiliza a biblioteca Flask. O arquivo requirements.txt lista todas as dependências.
(Se o arquivo requirements.txt não existir, você pode criá-lo com o comando: pip freeze > requirements.txt)

pip install -r requirements.txt


4. Inicialize o Banco de Dados
Este comando precisa ser executado apenas uma vez para criar o arquivo financas.db e a tabela de transações.

python database.py


5. Inicie a Aplicação
Você pode rodar a aplicação de duas formas:

Opção A: Rodando a API Web (Recomendado)
Esta é a versão completa com a interface gráfica.

flask --app api run


Após iniciar o servidor, acesse a seguinte URL no seu navegador:
http://127.0.0.1:5000/

Opção B: Rodando a Versão de Terminal (Legado)
Esta é a versão inicial do projeto, que roda sem interface gráfica, diretamente no terminal.

python main.py


📫 Contato

Em caso de dúvidas ou sugestões, entre em contato!

LinkedIn: [João Massari](https://www.linkedin.com/in/joao-paulo-massari-382604278)

Instagram: @massarii07

Divirta-se!
