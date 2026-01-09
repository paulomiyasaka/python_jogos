#Cria lista de jogos na memória
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God Of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Need For Speed', 'Corrida', 'PC')
lista = [jogo1, jogo2, jogo3]