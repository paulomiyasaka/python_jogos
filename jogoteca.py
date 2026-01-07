from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God Of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Need For Speed', 'Corrida', 'PC')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)


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
    return render_template('novo.html', titulo='Cadastrar novo jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    #return render_template('lista.html', titulo='Criar Cadastro de Jogos', jogos= lista)
    return redirect('/')

app.run(debug=True)