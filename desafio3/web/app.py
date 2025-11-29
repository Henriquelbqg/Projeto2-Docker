from flask import Flask

import psycopg2
import redis

app = Flask(__name__)


@app.route("/")
def index():
    return "Serviço Web funcionando com DB e Cache"


@app.route("/db")
def db_test():
    try:
        conn = psycopg2.connect(
            host="db",
            database="meu_banco",
            user="postgres",
            password="1234"
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        conn.close()
        return f"DB OK: {result}"
    except Exception as e:
        return f"Erro DB: {e}"


@app.route("/cache")
def cache_test():
    try:
        r = redis.Redis(host="cache", port=6379)
        r.set("teste", "ok")
        val = r.get("teste").decode()
        return f"Cache OK: {val}"
    except Exception as e:
        return f"Erro Cache: {e}"


app.run(host="0.0.0.0", port=8080)