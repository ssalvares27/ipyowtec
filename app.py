# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:50:27 2024

@author: SSA
"""

from flask import Flask, render_template

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Definindo a rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=False)
