
from flask import Flask, render_template
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

app = Flask(__name__)

# ===== CONFIGURAÇÃO DO BANCO =====
USUARIO = "root_python"
SENHA = quote_plus("python-cdip-bsb")
HOST = "mbs10065305"      # IP do servidor MySQL
PORTA = 3306
BANCO = "jogoteca"

# String de conexão SQLAlchemy (MySQL remoto)
DATABASE_URL = (
    f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=1800,
    echo=False
)

# ===== ROTA PRINCIPAL =====
@app.route("/")
def index():

    with engine.connect() as conn:

        # SELECT na tabela jogos
        jogos = conn.execute(
            text("SELECT id, nome, categoria, console FROM jogos")
        ).fetchall()

        # SELECT na tabela usuarios
        usuarios = conn.execute(
            text("SELECT nome, usuario FROM usuarios")
        ).fetchall()

    return render_template(
        "connection.html",
        jogos=jogos,
        usuarios=usuarios
    )


if __name__ == "__main__":
    # escuta fora do localhost
    app.run(debug=True)
