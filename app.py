from flask import Flask

from routes.animes import animes_bp
from routes.auth import auth_bp

app = Flask(__name__)

app.secret_key = "luizaebiel26"  # Essa chave criptografa os dados da sessão do usuário

app.register_blueprint(auth_bp)
app.register_blueprint(animes_bp)  # 2. Registre o blueprint no Flask


if __name__ == "__main__":
    app.run(port =4567, debug=True)
