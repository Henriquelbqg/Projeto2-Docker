from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Comunicação ok entre os containers"

app.run(host="0.0.0.0", port=8080)