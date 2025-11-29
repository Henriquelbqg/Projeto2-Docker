# **Desafio 1: Containers em Rede**

## Descrição da Solução
Este desafio demonstra a comunicação entre dois containers Docker conectados por meio de uma rede personalizada.
A solução utiliza:

- Um container executando um servidor Flask na porta 8080.
- Um container cliente em Alpine Linux que realiza requisições HTTP periódicas usando `curl`.
- Uma rede Docker criada manualmente, que permite a comunicação entre os containers pelo nome.

---

## Arquitetura
```

minha-rede

│

├── servidor  (Flask, porta 8080)

└── cliente   (curl em loop acessando http://servidor:8080)

```
---

## Funcionamento Técnico
- O servidor Flask retorna uma mensagem simples quando acessado via HTTP.
- O cliente executa um script que envia requisições contínuas ao servidor em intervalos regulares.
- Os containers são conectados à mesma rede Docker, permitindo comunicação direta através de resolução automática do nome do container.
- Os logs do cliente e do servidor evidenciam a troca de mensagens.

---

## Instruções de Execução

### 1. Criar a rede Docker personalizada
```bash
docker network create minha-rede
```

### **2. Construir a imagem do servidor**

```
docker build -t meu-servidor ./server
```

### **3. Construir a imagem do cliente**

```
docker build -t meu-cliente ./client
```

### **4. Executar o servidor na rede criada**

```
docker run -d --name servidor --network=minha-rede -p 8080:8080 meu-servidor
```

### **5. Executar o cliente na mesma rede**

```
docker run -d --name cliente --network=minha-rede meu-cliente
```

---

## **Testes**

### **Testar via navegador**

Acesse:

```
http://localhost:8080
```

### **Ver logs do servidor**

```
docker logs servidor
```

### **Ver logs do cliente**

```
docker logs cliente
```

Os logs devem mostrar as requisições enviadas pelo cliente e respondidas pelo servidor.

---

## **Arquivos do Projeto**

- server/app.py
- server/Dockerfile
- client/run.sh
- client/Dockerfile