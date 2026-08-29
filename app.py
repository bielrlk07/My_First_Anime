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

# A memória agora é uma Lista (para guardar várias ações)
historico_acoes = []  

@app.route("/")
def index():
    # O render_template vai buscar um arquivo HTML e nós 'injetamos' a lista nele,
    #Enviamos a lista de histórico inteira para o HTML
    return render_template("listadeanimes.html", lista_animes=meus_animes, historico_acoes=historico_acoes)

@app.route("/atualizar", methods=["POST"])
def atualizar():


    nome = request.form.get("nome_anime")     # Avisa o Python que vamos modificar a memória global
    novos_eps = int(request.form.get("novos_eps")) # Pega as informações que vieram do HTML

   
    for anime in meus_animes: # Pega o número que a pessoa digitou lá na caixinha
        if anime["nome"] == nome:

            # ANTES de somar os episódios novos, nós tiramos uma "fotografia" do estado atual
            historico_acoes.append({
                "nome": anime["nome"],
                "eps_vistos_antes": anime["eps_vistos"],
                "finalizado_antes": anime["finalizado"]
            })

            
            anime["eps_vistos"] += novos_eps # O += soma o valor atual com os novos episódios

            
            if anime["eps_vistos"] >= anime["total_eps"]: # Verificação de segurança: se a soma bater ou passar do total, finaliza!
                anime["eps_vistos"] = anime["total_eps"]
                anime["finalizado"] = True

            break # Como já achamos e atualizamos o anime, podemos parar o loop

    return redirect("/")


@app.route("/desfazer",methods=["POST"]) # NOVA ROTA: Responsável por reverter a ação quando o botão Desfazer for clicado
def desfazer():

    if len(historico_acoes) > 0: # Só tenta desfazer se a lista de histórico NÃO estiver vazia (len > 0)
        acao_revertida = historico_acoes.pop() # O .pop() pega a última ação salva e arranca ela da lista

        for anime in meus_animes: 
            if anime["nome"] == acao_revertida["nome"]:
                anime["eps_vistos"] = acao_revertida["eps_vistos_antes"] # Devolve os valores antigos para o anime
                anime["finalizado"] = acao_revertida["finalizado_antes"]
                break

        
    return redirect("/")


if __name__ == "__main__":
    app.run(port =4567, debug=True)
