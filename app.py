from flask import Flask, redirect, render_template, session

from dados import (  # Importando os dados do seu arquivo novo
    historico_acoes,
    meus_animes,
)
from routes.animes import animes_bp
from routes.auth import auth_bp

app = Flask(__name__)

app.secret_key = "luizaebiel26"  # Essa chave criptografa os dados da sessão do usuário

app.register_blueprint(auth_bp)
app.register_blueprint(animes_bp)  # 2. Registre o blueprint no Flask

@app.route("/")
def index():

    if "usuario_logado" not in session:  # Se o usuário não estiver logado, redireciona para a página de login
        return redirect("/login")
    
    return render_template("listadeanimes.html", lista_animes=meus_animes, historico_acoes=historico_acoes)     # O render_template vai buscar um arquivo HTML e nós 'injetamos' a lista nele,
        #Enviamos a lista de histórico inteira para o HTML


if __name__ == "__main__":
    app.run(port =4567, debug=True)
