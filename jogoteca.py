from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God Of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Need For Speed', 'Corrida', 'PC')
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self.senha = senha

usuario1 = Usuario("Paulo", "Paulo", "123456")
usuario2 = Usuario("Miyasaka", "Miyasaka", "123456")
usuario3 = Usuario("Japão", "Japão", "123456")

usuarios = { 
            usuario1.usuario : usuario1,
            usuario2.usuario : usuario2,
            usuario3.usuario : usuario3
            }



app = Flask(__name__)
app.secret_key = 'CORREIOS'


@app.route('/')
def index():
    #return '<h1>Olá Mundo!</h1>'
    #lista = ['Tetris', 'Skyrin', 'Crash']
    #jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    #jogo2 = Jogo('God Of War', 'Rack n Slash', 'PS2')
    #jogo3 = Jogo('Need For Speed', 'Corrida', 'PC')
    #lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Lista de Jogos Cadastrados', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        #return redirect('/login?proxima=novo')
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Cadastrar novo jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    #return render_template('lista.html', titulo='Criar Cadastro de Jogos', jogos= lista)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo="Login", proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.usuario
            flash(usuario.usuario + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login', proxima=url_for('novo')))
    


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)