import os
from jogoteca import app, db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

#LOGIN
class FormularioUsuario(FlaskForm):
    usuario = StringField('Nome do Usuário', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
    


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        #if f'capa_{id}.jpg' == nome_arquivo:
        if f'capa_{id}' in nome_arquivo:
            return nome_arquivo
        
    return 'capa_padrao.jpg'


def deleta_imagem(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))