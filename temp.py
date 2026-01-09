app.config['SQLALCHEMY_DATABASE_URI'] = (
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        #usuario = 'root_python',
        #senha = '@python@',
        #senha = 'python-cdip-bsb',
        servidor = 'MBS10065305',
        #servidor = '10.41.130.184',
        usuario = 'connect_power_bi',
        senha = quote_plus('@Correios*1234'),
        #servidor = 'localhost',
        database = 'jogoteca'
    )
)