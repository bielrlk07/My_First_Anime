from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template("listadeanimes.html", meus_animes=meus_animes)

if __name__ == "__main__":
    app.run(port =4567, debug=True)
