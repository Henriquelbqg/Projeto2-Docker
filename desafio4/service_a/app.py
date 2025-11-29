from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    lista = [
        {"id": 1, "nome": "Ana"},
        {"id": 2, "nome": "Carlos"},
        {"id": 3, "nome": "Marina"}
    ]
    return jsonify(lista)

app.run(host="0.0.0.0", port=5000)