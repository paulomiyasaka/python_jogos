from urllib.parse import quote_plus 

SECRET_KEY = 'CORREIOS'
#app.secret_key = 'CORREIOS'

#SGBD = 'mysql+mysqlconnector'
#usuario = "root_python" 
#senha = quote_plus('python-cdip-bsb')
#usuario = 'root'
#senha = ''
#host = "MBS10065305" 
#porta = 3306 
#banco = "jogoteca"

#url = f"mysql+mysqlconnector://{usuario}:{senha}@{host}:{porta}/{banco}"

#app.config['SQLALCHEMY_DATABASE_URI'] = (
SQLALCHEMY_DATABASE_URI = (
    '{SGBD}://{usuario}:{senha}@{host}:{porta}/{banco}'.format(
        SGBD = 'mysql+pymysql',
        #SGBD = 'mysql+mysqlconnector',
        #usuario = "root_python",
        #senha = quote_plus('python-cdip-bsb'),
        usuario = "root_python",
        senha = quote_plus("python-cdip-bsb"),
        host = "mbs10065305" ,
        porta = 3306,
        banco = "jogoteca",
    )
)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

#app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
SQLALCHEMY_ENGINE_OPTIONS= {
    "pool_pre_ping": True,
    "pool_recycle": 1800
}