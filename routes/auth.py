from flask import Blueprint, redirect, render_template, request, session

from dados import usuarios_db  # Importa o dicionário do outro arquivo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario_digitado = request.form.get("username") # Se a pessoa enviou o formulário (POST)
        senha_digitada = request.form.get("password")

        if usuario_digitado in usuarios_db and usuarios_db[usuario_digitado] == senha_digitada: # Verifica se o usuário existe no nosso "banco de dados" e se a senha bate

            session["usuario_logado"] = usuario_digitado  # O login deu certo! Salvamos o nome na sessão
            return redirect("/")  # Redireciona para a página principal após login bem-sucedido
        else:
            return render_template("login.html", erro="Usuário ou senha incorretos!")  # Mostra a página de login com uma mensagem de erro

    return render_template("login.html")  # Se for GET, apenas mostra a página de login



@auth_bp.route("/logout")
def logout():
    session.pop("usuario_logado", None)  # Remove o usuário da sessão, efetivamente deslogando-o
    return redirect("/login")  # Redireciona para a página de login após logout 
