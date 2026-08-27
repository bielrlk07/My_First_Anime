from flask import Flask, redirect, render_template, request

app = Flask(__name__)
# Aqui criamos a nossa lista de animes (nossa base de dados de teste)
meus_animes = [
    {
        "nome": "Baki",
        "total_eps": 26,
        "eps_vistos": 7,
        "finalizado": False
    },
    {
        "nome": "Death Note",
        "total_eps": 37,
        "eps_vistos": 37,
        "finalizado": True
    },
    {
        "nome": "Giji Harem",
        "total_eps": 12,
        "eps_vistos": 3,
        "finalizado": False
    }
]

@app.route("/")
def index():
    # O render_template vai buscar um arquivo HTML e nós 'injetamos' a lista nele
    return render_template("listadeanimes.html", lista_animes=meus_animes)

@app.route("/atualizar", methods=["POST"])
def atualizar():
    # Pega as informações que vieram do HTML
    nome = request.form.get("nome_anime")
    novos_eps = int(request.form.get("novos_eps"))

    # Procura o anime na lista e atualiza o número
    for anime in meus_animes:
        if anime["nome"] == nome:
            anime["eps_vistos"] = novos_eps
            # Se o número de episódios vistos for igual ao total, finaliza automaticamente!
            if novos_eps >= anime["total_eps"]:
                anime["finalizado"] = True
            break

    return redirect("/")

if __name__ == "__main__":
    app.run(port =4567, debug=True)
