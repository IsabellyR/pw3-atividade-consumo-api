from flask_sqlalchemy import SQLAlchemy

# Criando uma instância do SQLAlchemy
db = SQLAlchemy()


# Classe para representar os usuários
class Usuario(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    senha = db.Column(
        db.String(255),
        nullable=False
    )

    # Método construtor
    def __init__(self, email, senha):

        self.email = email
        self.senha = senha