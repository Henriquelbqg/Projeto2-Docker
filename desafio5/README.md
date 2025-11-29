# **Desafio 5 — Arquitetura com API Gateway e Dois Microserviços Independentes**

## **Descrição do Desafio**

O objetivo deste desafio é criar uma arquitetura completa baseada em microserviços utilizando Docker e Docker Compose.

A estrutura deve conter:

1. **API Gateway (Flask)**
    
    Centraliza o acesso externo e encaminha requisições para os microserviços.
    
2. **Serviço de Usuários**
    
    Fornece dados simulados de usuários.
    
3. **Serviço de Produtos**
    
    Fornece dados simulados de produtos.
    

Cada serviço deve rodar em seu próprio container, e o gateway deve se comunicar com os demais usando nomes de serviço na rede interna do Docker.

---

## **Estrutura do Projeto**

```
desafio5/
│
├── docker-compose.yml
│
├── api_gateway/
│   ├── app.py
│   └── Dockerfile
│
├── servico_usuarios/
│   ├── app.py
│   └── Dockerfile
│
└── servico_produtos/
    ├── app.py
    └── Dockerfile
```

---

## **Arquitetura dos Serviços**

### **API Gateway**

- Porta interna: 5000
- Porta externa exposta: **9000**
- Roteia chamadas para:
    - usuarios:5000
    - produtos:5000

### **Serviço de Usuários**

- Porta interna: 5000
- Porta externa: **5002**

### **Serviço de Produtos**

- Porta interna: 5000
- Porta externa: **5003**

Todos conectados pela rede:

```
minha-rede
```

---

## **docker-compose.yml**

```
version: "3.8"

services:
  api_gateway:
    build: ./api_gateway
    container_name: desafio5_api_gateway
    ports:
      - "9000:5000"
    depends_on:
      - usuarios
      - produtos
    networks:
      - minha-rede

  usuarios:
    build: ./servico_usuarios
    container_name: desafio5_usuarios
    ports:
      - "5002:5000"
    networks:
      - minha-rede

  produtos:
    build: ./servico_produtos
    container_name: desafio5_produtos
    ports:
      - "5003:5000"
    networks:
      - minha-rede

networks:
  minha-rede:
```

---

## **Código Resumido dos Serviços**

### **API Gateway — app.py**

```
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "API Gateway ativo"})

@app.route("/usuarios")
def get_users():
    resposta = requests.get("http://usuarios:5000/")
    return jsonify({"gateway": True, "resposta": resposta.json()})

@app.route("/produtos")
def get_products():
    resposta = requests.get("http://produtos:5000/")
    return jsonify({"gateway": True, "resposta": resposta.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### **Serviço de Usuários — app.py**

```
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
```

---

### **Serviço de Produtos — app.py**

```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def produtos():
    return jsonify([
        {"id": 1, "produto": "Notebook"},
        {"id": 2, "produto": "Monitor"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## **Dockerfile para os três serviços**

```
FROM python:3.10
WORKDIR /app
COPY app.py .
RUN pip install flask requests
CMD ["python", "app.py"]
```

---

## **Como executar o projeto**

### **1. Subir os serviços**

No diretório desafio5/:

```
docker compose up -d --build
```

---

### **2. Testar no navegador**

API Gateway:

```
http://localhost:9000
```

Via Gateway:

```
http://localhost:9000/usuarios
http://localhost:9000/produtos
```

Serviços individuais:

```
http://localhost:5002
http://localhost:5003
```

---

## **Encerrando os serviços**

```
docker compose down
```