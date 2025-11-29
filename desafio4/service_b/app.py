from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get("http://service_a:5000/users")
    usuarios = r.json()

    resposta = []
    for u in usuarios:
        resposta.append(f"Usuário {u['nome']} ativo desde 2020.")

    return "<br>".join(resposta)

app.run(host="0.0.0.0", port=6000)