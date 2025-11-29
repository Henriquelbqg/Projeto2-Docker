# **Desafio 3 — Integração entre Flask, PostgreSQL e Redis com Docker Compose**

## **Descrição do Desafio**

O objetivo deste desafio é criar um ambiente com três serviços independentes, todos orquestrados com Docker Compose:

1. **Aplicação Flask**
2. **Banco de Dados PostgreSQL**
3. **Cache Redis**

A aplicação Flask deve:

- conectar ao PostgreSQL;
- buscar dados na tabela;
- armazenar e recuperar dados de cache no Redis;
- retornar uma resposta consolidada.

---

## **Estrutura do Projeto**

```
desafio3/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## **Arquitetura dos Serviços**

### **1. Serviço Web (Flask)**

- Endereço interno: web:5000
- Porta externa: 8080
- Dependências: PostgreSQL e Redis
- Conecta ao banco para consultar dados e ao Redis como cache

### **2. Serviço de Banco (PostgreSQL)**

- Endereço interno: db:5432
- Banco padrão: postgres
- Volume persistente garantindo armazenamento dos dados

### **3. Serviço de Cache (Redis)**

- Endereço interno: cache:6379
- Utilizado como armazenamento temporário

---

## **docker-compose.yml**

```
services:
  web:
    build: .
    container_name: desafio3-web
    ports:
      - "8080:5000"
    depends_on:
      - db
      - cache
    networks:
      - rede-interna

  db:
    image: postgres:16
    container_name: desafio3-db
    environment:
      POSTGRES_PASSWORD: 1234
    volumes:
      - db-volume:/var/lib/postgresql/data
    networks:
      - rede-interna

  cache:
    image: redis:7
    container_name: desafio3-cache
    networks:
      - rede-interna

networks:
  rede-interna:

volumes:
  db-volume:
```

---

## **Lógica da Aplicação (Flask)**

### **Conexões:**

- Redis:
    
    redis.Redis(host='cache', port=6379)
    
- PostgreSQL (via psycopg2):
    
    psycopg2.connect(host="db", ...)
    

### **Rota principal (exemplo):**

```
@app.route("/")
def home():
    # Consulta PostgreSQL
    # Usa Redis como cache
    return {"mensagem": "ok", "dados": ..., "cache": ...}
```

A aplicação retorna dados vindos:

- do banco
- do cache
- da aplicação Flask

---

## **Como executar o projeto**

### **1. Build e subida dos serviços**

No diretório desafio3/:

```
docker compose up -d --build
```

---

### **2. Verificar containers ativos**

```
docker ps
```

Você deve ver:

- desafio3-web
- desafio3-db
- desafio3-cache

---

### **3. Acessar no navegador**

```
http://localhost:8080
```

Se o Chrome bloquear alguma porta, use:

- Safari
- Firefox
- ou altere a porta externa para 8000, 8081 ou 9000

---

## **Como encerrar os serviços**

```
docker compose down
```

Para remover o volume do banco:

```
docker volume rm desafio3_db-volume
```