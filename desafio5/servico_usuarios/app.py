from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def usuarios():
    return jsonify([
        {"id": 1, "nome": "Renata"},
        {"id": 2, "nome": "Henrique"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)