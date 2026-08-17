# Importando o Flask na aplicação
from flask import Flask, render_template
from controllers import routes
import pymysql
from models.database import db, Game, Console

# Carregando o Flask em uma variável
app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente do Python que tem o nome do módulo atual

DB_NAME = 'thegames'
app.config['DATABASE_NAME'] = DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

# Enviando a variavel app para as rotas
routes.init_app(app)

# Iniciando o servidor web
if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("O Banco de Dados foi criado com sucesso!")
    except Exception as error:
        print(f"Erro ao criar o Banco de Dados: {error}")
    finally:
        connection.close()
        
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
        
    app.run(debug=True)




