from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from jogoteca import app, db
from models import Jogos, Usuarios

@app.route('/')
def index():
    #return '<h1>Olá Mundo!</h1>'
    #lista = ['Tetris', 'Skyrin', 'Crash']
    #jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    #jogo2 = Jogo('God Of War', 'Rack n Slash', 'PS2')
    #jogo3 = Jogo('Need For Speed', 'Corrida', 'PC')
    #lista = [jogo1, jogo2, jogo3]
    
    #result = db.session.execute(
    #lista = db.session.execute(
    #    text("SELECT nome FROM jogos")
    #    )
    #jogos = result.fetchall()
    #return render_template("index.html", jogos=jogos)

    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Lista de Jogos Cadastrados', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        #return redirect('/login?proxima=novo')
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Cadastrar novo jogo')

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    jogo = Jogos.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editar jogo', jogo=jogo)


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    #jogo = Jogo(nome, categoria, console)
    #lista.append(jogo)
    #return render_template('lista.html', titulo='Criar Cadastro de Jogos', jogos= lista)

    jogo = Jogos.query.filter_by(nome=nome).first()
    if jogo:
        flash('Jogo já existente.')
        return redirect(url_for('index'))
    
    novoJogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novoJogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    arquivo.save(f'uploads/capa_{novoJogo.id}.jpg')
    
    flash('Jogo cadastrado com sucesso!')
    return redirect(url_for('index'))

@app.route('/atualizar',  methods=['POST',])
def atualizar():
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/capa_{jogo.id}.jpg')

    flash('Jogo atualizado com sucesso!')
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    jogo = Jogos.query.filter_by(id=id).delete()
    
    db.session.commit()
    flash('Jogo excluído com sucesso!')
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo="Login", proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = Usuarios.query.filter_by(usuario=request.form['usuario']).first()
    if usuario:
    #if request.form['usuario'] in usuarios:
    #    usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.usuario
            flash(usuario.usuario + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login', proxima=url_for('novo')))
    else:
        flash('Informe o usuário e senha válidos.')
        return redirect(url_for('login', proxima=url_for('novo')))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)