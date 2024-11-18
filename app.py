# -*- coding: utf-8 -*-
from flask import Flask, render_template
import json


app = Flask(__name__)

# ==================== funcoes ================================================

# carrega os dados dos produtos por categoria
def carregar_produtos(categoria):
    """
    Função que carrega os produtos de acordo com a categoria informada.
    O nome do arquivo JSON será construído com base na categoria.
    """
    # Exemplo: 'json/som.json' ou 'json/informatica.json'
    arquivo_json = f'json/{categoria}.json'    
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as file:
            produtos = json.load(file)  # Carrega o conteúdo do arquivo JSON
        return produtos
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo {arquivo_json}.")
        return []

# ==================== Rotas ==================================================

# Rotas do Flask
@app.route('/')
def home():
    produtos = carregar_produtos('destaque')
    return render_template('index.html', produtos=produtos)  # Página inicial

@app.route('/tecnologia_som')
def tecnologia_som():
    produtos = carregar_produtos('som')
    return render_template('tecnologia_som.html', produtos=produtos)


# ==================== main ===================================================

if __name__ == '__main__':
    app.run(debug=False)


