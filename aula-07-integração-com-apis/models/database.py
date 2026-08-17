from flask_sqlalchemy import SQLAlchemy

# Criando uma instância do SQLAlchemy - Carregando um uma variável
db = SQLAlchemy()

# Criando a classe para representar a entidade Games no Banco de Dados (tabela)
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
# Método construtor (atributos que serão utilizados pelos objetos)
    def __init__(self,titulo,ano,categoria,plataforma,preco,quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade
        
        
class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    fabricante = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
    
# Método construtor (atributos que serão utilizados pelos objetos)
    def __init__(self,nome,ano,fabricante,plataforma,preco,quantidade):
        self.nome = nome
        self.ano = ano
        self.fabricante = fabricante
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade
        
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        