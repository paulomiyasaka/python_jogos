#Cria lista de usuários na memória
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
