// Função para alternar o menu dropdown
function toggleDropdown(id) {
    const dropdown = document.getElementById(id);
    dropdown.style.display = (dropdown.style.display === "block") ? "none" : "block";
}


// Filtragem de produtos por categoria
document.getElementById('categoriaSelector').addEventListener('change', function() {
    const categoriaSelecionada = this.value;
    const produtos = document.querySelectorAll('.produto');

    // Se a opção "Selecione uma categoria" for escolhida, exibe todos os produtos
    if (categoriaSelecionada === "") {
        produtos.forEach(produto => {
            produto.style.display = 'block';  // Exibe todos os produtos
        });
    } else {
        // Caso contrário, faz a filtragem de produtos pela categoria selecionada
        produtos.forEach(produto => {
            const categoria = produto.getAttribute('data-categoria');
            if (categoria === categoriaSelecionada) {
                produto.style.display = 'block';  // Exibe o produto que corresponde à categoria
            } else {
                produto.style.display = 'none';   // Oculta o produto que não corresponde à categoria
            }
        });
    }
});