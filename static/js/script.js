document.addEventListener('DOMContentLoaded', function () {
    const customSelect = document.querySelector('.custom-select');
    const selectedOption = customSelect.querySelector('.selected-option');
    const optionsList = customSelect.querySelector('.options-list');
    const hiddenInput = document.getElementById('categoriaSelector');
    const produtos = document.querySelectorAll('.produto');

    // Alternar o menu dropdown
    selectedOption.addEventListener('click', () => {
        customSelect.classList.toggle('active');
    });

    // Função para filtrar produtos por categoria
    function filtrarProdutos(categoriaSelecionada) {
        if (categoriaSelecionada === "") {
            // Exibe todos os produtos se nenhuma categoria estiver selecionada
            produtos.forEach(produto => {
                produto.style.display = 'block';
            });
        } else {
            // Filtra os produtos pela categoria selecionada
            produtos.forEach(produto => {
                const categoria = produto.getAttribute('data-categoria');
                produto.style.display = categoria === categoriaSelecionada ? 'block' : 'none';
            });
        }
    }

    // Seleção de uma opção no dropdown
    optionsList.addEventListener('click', (e) => {
        if (e.target.tagName === 'LI') {
            const value = e.target.getAttribute('data-value');
            const text = e.target.textContent;

            // Atualiza o campo selecionado e o input oculto
            selectedOption.textContent = text;
            hiddenInput.value = value;

            // Fecha o menu
            customSelect.classList.remove('active');

            // Chama a função de filtragem com a categoria selecionada
            filtrarProdutos(value);
        }
    });

    // Fecha o menu ao clicar fora do seletor
    document.addEventListener('click', (e) => {
        if (!customSelect.contains(e.target)) {
            customSelect.classList.remove('active');
        }
    });
});
