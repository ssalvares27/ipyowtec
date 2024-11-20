from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import json
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Carregar variáveis de ambiente do .env
load_dotenv()

# Configurações do Flask e banco de dados
app = Flask(__name__)
admin_login = os.getenv("ADMIN_LOGIN")
admin_password = os.getenv("ADMIN_PASSWORD")
app.secret_key = os.getenv("SECRET_KEY")  # Substitua por uma chave segura!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'  # URI do banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa o rastreamento de modificações
db = SQLAlchemy(app)

# ==================== Modelo Dados ====================================

class Dado(db.Model):
    __tablename__ = 'dado'  # Nome da tabela
    id = db.Column(db.Integer, primary_key=True)
    pagina = db.Column(db.String(80), nullable=False)
    contador = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Dado {self.pagina}>'

# ==================== Funções e Rota ====================================

def registrar_visita(pagina):
    """
    Incrementa o contador de visitas para a página especificada.
    """
    dado = Dado.query.filter_by(pagina=pagina).first()
    if dado is None:
        # Se o dado não existir, cria um novo
        dado = Dado(pagina=pagina, contador=1)
        db.session.add(dado)
        db.session.commit()
    else:
        # Se já existir, incrementa o contador
        dado.contador += 1
        db.session.commit()

def carregar_produtos(categoria):
    """
    Carrega os produtos de acordo com a categoria informada.
    """
    arquivo_json = f'json/{categoria}.json'
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as file:
            produtos = json.load(file)
        return produtos
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo {arquivo_json}.")
        return []

# Middleware de autenticação
def login_required(f):
    """
    Decorador para proteger rotas com autenticação.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in') is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== Rotas ==================================================

@app.route('/')
def home():
    registrar_visita("home")
    produtos = carregar_produtos('destaque')
    return render_template('index.html', produtos=produtos)

@app.route('/tecnologia_som')
def tecnologia_som():
    registrar_visita("tecnologia_som")
    produtos = carregar_produtos('som')
    return render_template('tecnologia_som.html', produtos=produtos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Rota para login de administrador.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']       
        if admin_login == username and admin_password == password:  # Credenciais de exemplo
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', erro="Credenciais inválidas!")
    return render_template('login.html')

@app.route('/logout')
def logout():
    """
    Rota para sair da área administrativa.
    """
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/admin')
@login_required
def admin():
    """
    Área administrativa protegida com estatísticas de visitas.
    """
    dados_visitas = Dado.query.all()
    visitas = {dado.pagina: dado.contador for dado in dados_visitas}
    return render_template('admin.html', visitas=visitas)

# ==================== Inicialização do Banco de Dados ======================

# Criar as tabelas automaticamente se não existirem
with app.app_context():
    db.create_all()  # Isso cria as tabelas no banco de dados

# ==================== Main ===================================================

if __name__ == '__main__':
    app.run(debug=False)
