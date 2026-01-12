import os
from jogoteca import app, db

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