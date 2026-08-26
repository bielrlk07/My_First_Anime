from flask import Flask

app = Flask (__name__)

@app.route("/")
def index ():
    return "Opa"
if __name__ == "__main__":
    app.run(port=4567, debug=True)