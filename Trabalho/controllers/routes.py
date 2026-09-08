from flask import render_template, request, redirect, url_for, flash, session
from models.database import db, Usuario
from werkzeug.security import generate_password_hash, check_password_hash
import urllib.request
import json


def init_app(app):

    @app.before_request
    def check_auth():

        rotasPermitidas = ['home', 'login', 'cadastro', 'static']

        if request.endpoint in rotasPermitidas:
            return

        if 'usuario_id' not in session:
            return redirect(url_for('login'))


    @app.route('/')
    def home():
        return render_template('index.html')


    @app.route('/personas')
    def personas():

        nome = "Fisher Tiger"
        idade = 48
        genero = "Masculino"

        personagem = {
            "Nome": "Silvers Rayleigh",
            "Idade": 78,
            "Classificação": "Humano"
        }

        listaPersonagens = [
            {
                "nome": "Shimotsuki Kuina",
                "idade": 11
            }
        ]

        return render_template(
            'personas.html',
            nome=nome,
            idade=idade,
            genero=genero,
            personagem=personagem,
            listaPersonagens=listaPersonagens
        )


    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():

        if request.method == 'POST':

            email = request.form['email']
            senha = request.form['senha']

            senha_criptografada = generate_password_hash(
                senha,
                method='scrypt'
            )

            novo_usuario = Usuario(
                email=email,
                senha=senha_criptografada
            )

            db.session.add(novo_usuario)
            db.session.commit()

            return redirect(url_for('login'))

        return render_template('cadastro.html')


    @app.route('/login', methods=['GET', 'POST'])
    def login():

        if request.method == 'POST':

            email = request.form['email']
            senha = request.form['senha']

            usuario = Usuario.query.filter_by(email=email).first()

            if usuario:

                if check_password_hash(usuario.senha, senha):

                    session['usuario_id'] = usuario.id
                    session['usuario_email'] = usuario.email

                    flash(
                        'Você foi autenticado com sucesso! Bem-vindo!',
                        'success'
                    )

                    return redirect(url_for('home'))

                else:

                    flash(
                        'Falha no login. Verifique os dados e tente novamente!',
                        'danger'
                    )

                    return redirect(url_for('login'))

            else:

                flash(
                    'O usuário informado não existe!',
                    'danger'
                )

                return redirect(url_for('login'))

        return render_template('login.html')


    @app.route('/logout', methods=['GET', 'POST'])
    def logout():

        session.clear()

        return redirect(url_for('home'))


    @app.route('/apipersonas')
    @app.route('/apipersonas/<id>')
    def apipersonas(id=None):

        urlAPI = 'https://onepieceapi.com/api/characters'

        resposta = urllib.request.urlopen(urlAPI)

        dados = resposta.read()

        listaPersonagens = json.loads(dados)

        if id:

            personagemInfo = None

            for personagem in listaPersonagens:

                if personagem['id'] == id:

                    personagemInfo = personagem
                    break

            if personagemInfo:

                return render_template(
                    'personainfo.html',
                    personagemInfo=personagemInfo
                )

            else:

                return f'Personagem com a ID {id} não foi encontrado.'

        return render_template(
            'apipersonas.html',
            listaPersonagens=listaPersonagens
        )