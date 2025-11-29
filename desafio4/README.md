# **Desafio 4 — Comunicação entre Dois Microserviços com Docker Compose**

## **Descrição do Desafio**

O objetivo deste desafio é criar dois microserviços independentes, cada um rodando em seu próprio container Docker, de forma que:

1. **Service A (servidor Flask)** expõe uma rota HTTP.
2. **Service B (cliente)** faz requisições HTTP ao Service A.
3. Ambos são conectados por uma rede Docker interna.
4. A porta externa do Service A é exposta para permitir testes via navegador.

O desafio demonstra como containers compartilham rede interna e se comunicam usando nomes de serviço como hostname.

---

## **Estrutura do Projeto**

```
desafio4/
│
├── docker-compose.yml
│
├── service_a/
│   ├── app.py
│   └── Dockerfile
│
└── service_b/
    ├── app.py
    └── Dockerfile
```

---

## **Arquitetura dos Serviços**

### **Service A — Servidor Flask**

- Responde uma rota HTTP simples
- Deve rodar na porta interna 5000
- Expõe uma porta externa (ex.: **5001**) para teste via navegador

### **Service B — Cliente Flask**

- Faz requisições HTTP para Service A
- Utiliza o hostname service_a dentro da rede Docker
- Roda na porta interna 6000
- Porta externa configurada de acordo com disponibilidade (ex.: **8000**)

---

## **docker-compose.yml**

```
services:
  service_a:
    build: ./service_a
    container_name: desafio4_service_a
    ports:
      - "5001:5000"
    networks:
      - minha-rede

  service_b:
    build: ./service_b
    container_name: desafio4_service_b
    ports:
      - "8000:6000"
    depends_on:
      - service_a
    networks:
      - minha-rede

networks:
  minha-rede:
```

---

## **Código dos Microserviços**

### **Service A — app.py**

```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "Resposta do Service A"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### **Service B — app.py**

```
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def chamar_service_a():
    resposta = requests.get("http://service_a:5000/")
    return jsonify({"cliente": True, "resposta": resposta.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
```

---

## **Como executar o projeto**

No diretório desafio4/:

```
docker compose up -d --build
```

---

## **Testes**

### **1. Acessar Service A diretamente (navegador)**

```
http://localhost:5001
```

### **2. Acessar Service B (gateway do cliente)**

```
http://localhost:8000
```

O Service B retorna a própria resposta **e** a resposta repassada do Service A.

---

## **Como encerrar corretamente**

```
docker compose down
```

Se quiser remover os containers antigos:

```
docker rm -f desafio4_service_a desafio4_service_b
```