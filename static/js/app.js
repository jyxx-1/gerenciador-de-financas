document.addEventListener('DOMContentLoaded', () => {
    
    const form = document.getElementById('add-transaction-form');
    const lista = document.getElementById('transaction-list');
    let transacoesAtuais = []; // Guarda a lista de transações atual

    // --- FUNÇÃO PARA CARREGAR AS TRANSAÇÕES ---
    async function carregarTransacoes() {
        const response = await fetch('/transacoes');
        transacoesAtuais = await response.json();

        lista.innerHTML = '';

        if (transacoesAtuais.length === 0) {
            lista.innerHTML = '<li>Nenhuma transação encontrada.</li>';
            return;
        }

        transacoesAtuais.forEach(transacao => {
            const item = document.createElement('li');
            const dataFormatada = new Date(transacao.data + 'T00:00:00').toLocaleDateString('pt-BR');
            const corValor = transacao.valor >= 0 ? 'positivo' : 'negativo';
            
            item.innerHTML = `
                <div class="info">
                    <span>${transacao.descricao}</span>
                    <span class="data">Data: ${dataFormatada}</span>
                </div>
                <div class="valor-e-acoes">
                    <span class="valor ${corValor}">R$ ${transacao.valor.toFixed(2)}</span>
                    <div class="acoes">
                        <button class="edit-btn" data-id="${transacao.id}">✏️</button>
                        <button class="delete-btn" data-id="${transacao.id}">🗑️</button>
                    </div>
                </div>
            `;
            
            lista.appendChild(item);
        });
    }

    // --- LÓGICA PARA O FORMULÁRIO DE ADIÇÃO ---
    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const descricao = document.getElementById('descricao').value;
        const valor = document.getElementById('valor').value;
        const data = document.getElementById('data').value;

        const dadosTransacao = {
            descricao: descricao,
            valor: parseFloat(valor),
            data: data
        };

        const response = await fetch('/transacoes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dadosTransacao),
        });

        if (response.ok) {
            form.reset();
            await carregarTransacoes();
        } else {
            const erro = await response.json();
            console.error('Erro ao adicionar transação:', erro);
            alert('Não foi possível adicionar a transação.');
        }
    });

    // --- LÓGICA PARA OS BOTÕES DE AÇÃO NA LISTA ---
    lista.addEventListener('click', async (event) => {
        const target = event.target; // <-- A LINHA QUE FALTAVA! Definimos o alvo do clique aqui.

        // LÓGICA DE DELETAR
        if (target.classList.contains('delete-btn')) {
            const id = target.dataset.id;
            if (confirm(`Tem certeza que deseja deletar a transação ID ${id}?`)) {
                const response = await fetch(`/transacoes/${id}`, { method: 'DELETE' });
                if (response.ok) await carregarTransacoes();
                else alert('Erro ao deletar a transação.');
            }
        }

        // LÓGICA PARA MOSTRAR O FORM DE EDIÇÃO
        if (target.classList.contains('edit-btn')) {
            const id = target.dataset.id;
            const li = target.closest('li');
            const transacao = transacoesAtuais.find(t => t.id == id);

            li.innerHTML = `
                <form class="edit-form">
                    <input type="text" name="descricao" value="${transacao.descricao}" required>
                    <input type="number" step="0.01" name="valor" value="${transacao.valor}" required>
                    <input type="date" name="data" value="${transacao.data}" required>
                    <div class="edit-actions">
                        <button type="submit" class="save-edit-btn" data-id="${id}">✔️</button>
                        <button type="button" class="cancel-edit-btn">❌</button>
                    </div>
                </form>
            `;
        }

        // LÓGICA PARA SALVAR A EDIÇÃO
        if (target.classList.contains('save-edit-btn')) {
            event.preventDefault();
            
            const id = target.dataset.id;
            const formEdicao = target.closest('.edit-form');
            
            const dadosAtualizados = {
                descricao: formEdicao.querySelector('[name="descricao"]').value,
                valor: parseFloat(formEdicao.querySelector('[name="valor"]').value),
                data: formEdicao.querySelector('[name="data"]').value
            };

            const response = await fetch(`/transacoes/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dadosAtualizados)
            });

            if (response.ok) await carregarTransacoes();
            else alert('Erro ao atualizar a transação.');
        }

        // LÓGICA PARA CANCELAR A EDIÇÃO
        if (target.classList.contains('cancel-edit-btn')) {
            await carregarTransacoes();
        }
    });

    // --- CHAMADA INICIAL ---
    carregarTransacoes();
});