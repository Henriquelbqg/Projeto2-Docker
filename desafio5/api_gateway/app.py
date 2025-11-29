from flask import Flask, jsonify
import requests

app = Flask(__name__)

USUARIOS_URL = "http://usuarios:5000"
PRODUTOS_URL = "http://produtos:5000"


@app.route("/")
def home():
    return jsonify({"mensagem": "API Gateway ativo"})


@app.route("/usuarios")
def get_users():
    resposta = requests.get(f"{USUARIOS_URL}/")
    return jsonify({"gateway": True, "resposta": resposta.json()})


@app.route("/produtos")
def get_products():
    resposta = requests.get(f"{PRODUTOS_URL}/")
    return jsonify({"gateway": True, "resposta": resposta.json()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)