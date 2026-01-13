from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
#from urllib.parse import quote_plus 
#from sqlalchemy import create_engine, text

app = Flask(__name__)
app.config.from_pyfile('config.py')

#app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+mysqlconnector://root_python:python-cdip-bsb@mbs10065305/jogoteca'

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)