# **Desafio 2 — Banco de Dados com Docker + Volume + Script de Inicialização**

## **Descrição do Desafio**

O objetivo deste desafio é criar um ambiente de banco de dados PostgreSQL usando Docker e Docker Compose, garantindo que:

1. O banco seja iniciado automaticamente com um arquivo SQL (init.sql).
2. O volume persista os dados mesmo após o container ser encerrado.
3. A conexão com o banco permita validar que o script foi executado corretamente.

---

## **Estrutura do Projeto**

```
desafio2/
│
├── docker-compose.yml
├── init.sql
└── README.md
```

---

## **Como funciona**

### **1. Docker Compose**

Configura o serviço PostgreSQL com:

- definição da senha;
- definição do banco inicial;
- mapeamento do script init.sql para inicialização automática;
- volume para persistência dos dados;
- exposição da porta 5432 para conexão externa.

O serviço é criado conforme o arquivo:

```
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: meu_banco
    volumes:
      - meu-volume:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"

volumes:
  meu-volume:
```

---

### **2. init.sql**

Arquivo SQL executado automaticamente na primeira inicialização do container:

```
CREATE TABLE teste (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL
);

INSERT INTO teste (nome) VALUES ('Registro inicial');
```

---

## **Como executar o projeto**

### **1. Iniciar o ambiente**

No diretório desafio2/, execute:

```
docker compose up -d
```

---

### **2. Confirmar que o banco subiu**

Para listar os containers:

```
docker ps
```

Você deve ver o container desafio2-db-1 rodando.

---

### **3. Acessar o PostgreSQL**

```
docker exec -it desafio2-db-1 psql -U postgres
```

Trocar para o banco criado:

```
\c meu_banco;
```

Consultar os dados:

```
SELECT * FROM teste;
```

Resultado esperado:

```
 id |       nome
----+------------------
  1 | Registro inicial
```

---

## **Como encerrar corretamente**

Execute:

```
docker compose down
```

Se desejar remover o volume (e perder os dados):

```
docker volume rm desafio2_meu-volume
```
