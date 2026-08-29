from flask import Flask, redirect, render_template, request

app = Flask(__name__)
# Aqui criamos a nossa lista de animes (nossa base de dados de teste)
meus_animes = [
    {
        "nome": "Baki",
        "total_eps": 26,
        "eps_vistos": 0,
        "finalizado": False
    },
    {
        "nome": "Death Note",
        "total_eps": 37,
        "eps_vistos": 0,
        "finalizado": False
    },
    {
        "nome": "Giji Harem",
        "total_eps": 12,
        "eps_vistos": 0,
        "finalizado": False
    }
]

@app.route("/")
def index():
    # O render_template vai buscar um arquivo HTML e nós 'injetamos' a lista nele
    return render_template("listadeanimes.html", lista_animes=meus_animes, ultima_acao=ultima_acao)

ultima_acao = None

@app.route("/atualizar", methods=["POST"])
def atualizar():
    global ultima_acao 
    # Avisa o Python que vamos modificar a memória global
    # Pega as informações que vieram do HTML
    nome = request.form.get("nome_anime")
    novos_eps = int(request.form.get("novos_eps"))

   # Pega o número que a pessoa digitou lá na caixinha
    for anime in meus_animes:
        if anime["nome"] == nome:

            # ANTES de somar os episódios novos, nós tiramos uma "fotografia" do estado atual
            ultima_acao = {
                "nome": anime["nome"],
                "eps_vistos_antes": anime["eps_vistos"],
                "finalizado_antes": anime["finalizado"]
            }

            # AQUI ESTÁ A MÁGICA: O += soma o valor atual com os novos episódios
            anime["eps_vistos"] += novos_eps

            # Verificação de segurança: se a soma bater ou passar do total, finaliza!
            if anime["eps_vistos"] >= anime["total_eps"]:
                anime["eps_vistos"] = anime["total_eps"]
                anime["finalizado"] = True

            break # Como já achamos e atualizamos o anime, podemos parar o loop

    return redirect("/")

# NOVA ROTA: Responsável por reverter a ação quando o botão Desfazer for clicado
@app.route("/desfazer",methods=["POST"])
def desfazer():
    global ultima_acao

    # Só faz alguma coisa se existir uma ação salva na memória
    if ultima_acao is not None:
        for anime in meus_animes:
            if anime["nome"] == ultima_acao["nome"]:
                # Devolve os valores antigos para o anime
                anime["eps_vistos"] = ultima_acao["eps_vistos_antes"]
                anime["finalizado"] = ultima_acao["finalizado_antes"]
                break

        # Limpa a memória para que o botão suma da tela após ser usado
        ultima_acao = None
    return redirect("/")


if __name__ == "__main__":
    app.run(port =4567, debug=True)
