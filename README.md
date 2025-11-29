# **Projeto: Sistemas Distribuídos com Docker, Microserviços e Redes**

## **Visão Geral**

Este projeto consiste na implementação de cinco desafios progressivos que demonstram conceitos centrais de sistemas distribuídos utilizando **Docker**, **Docker Compose**, **redes virtuais**, **microsserviços**, **volumes persistentes**, **cache**, **bancos de dados**, e **API Gateway**.

Cada desafio representa um nível crescente de complexidade, desde a criação de um único container até a composição completa de múltiplos serviços integrados em um ecossistema distribuído.

---

# **Estrutura do Repositório**

```
projeto_repo/
│
├── desafio1/
│   ├── server/
│   ├── client/
│   └── docker-compose.yml
│
├── desafio2/
│   ├── init.sql
│   └── docker-compose.yml
│
├── desafio3/
│   ├── app.py
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── desafio4/
│   ├── service_a/
│   ├── service_b/
│   └── docker-compose.yml
│
└── desafio5/
    ├── api_gateway/
    ├── servico_usuarios/
    ├── servico_produtos/
    └── docker-compose.yml
```

---

# **Resumo dos Desafios**

---

## **Desafio 1 — Cliente e Servidor em Containers Separados**

**Objetivo:**

Criar dois containers (servidor Flask e cliente shell) que se comunicam em uma rede Docker personalizada.

**Conceitos aplicados:**

- Dockerfile
- Construção de imagens
- Rede customizada
- Comunicação via hostname

**Funcionalidade:**

O cliente faz requisições HTTP para o servidor repetidamente.

---

## **Desafio 2 — Banco de Dados com Volume Persistente e Script de Inicialização**

**Objetivo:**

Executar um container PostgreSQL com:

- volume persistente
- script SQL automático
- porta exposta para testes externos

**Conceitos aplicados:**

- Volumes
- Entrada automática via /docker-entrypoint-initdb.d
- Persistência de dados
- Execução de SQL no primeiro build

**Validação:**

Conectar via psql e consultar tabela criada pelo init.sql.

---

## **Desafio 3 — Integração entre Flask, PostgreSQL e Redis**

**Objetivo:**

Construir um microserviço Flask que:

- lê dados do PostgreSQL
- utiliza Redis como cache
- retorna uma resposta combinada

**Conceitos aplicados:**

- Múltiplos serviços com Compose
- Uso de nomes de serviço como hostname
- Cache distribuído
- Conexão simultânea a banco + cache

---

## **Desafio 4 — Comunicação entre Dois Microserviços**

**Objetivo:**

Criar dois microsserviços independentes, onde:

- Service A é uma API básica Flask
- Service B consome a API de A
- Ambos compartilham rede interna
- Uma porta externa é exposta ao host

**Conceitos aplicados:**

- Microserviços independentes
- Comunicação interna via rede Docker
- Chamadas HTTP entre containers
- Exposição de portas para o host

---

## **Desafio 5 — API Gateway e Arquitetura Completa de Microsserviços**

**Objetivo:**

Criar três microsserviços:

1. **API Gateway**
2. **Serviço de Usuários**
3. **Serviço de Produtos**

O gateway deve centralizar chamadas e redirecionar para os serviços corretos.

**Conceitos aplicados:**

- API Gateway
- Encaminhamento de requisições
- Três serviços independentes
- Comunicação interna via rede
- Exposição segura da porta do gateway

---

# **Tecnologias Utilizadas**

- Docker
- Docker Compose
- Python 3.10
- Flask
- Redis
- PostgreSQL
- Redes Docker
- Volumes persistentes
- HTTP e microarquitetura

---

# **Como Executar o Projeto Completo**

Cada desafio pode ser executado isoladamente:

```
cd desafioX
docker compose up -d --build
```

Para encerrar:

```
docker compose down
```

---

# **Principais Aprendizados do Projeto**

- Construção de imagens customizadas.
- Criação de redes Docker e DNS interno.
- Comunicação distribuída entre serviços.
- Persistência de dados com volumes.
- Orquestração multi-container com Compose.
- Roteamento de requisições em microarquitetura.
- Uso de banco + cache + API em conjunto.
- Padrões fundamentais de sistemas distribuídos.

---

# **Conclusão**

O projeto demonstra, na prática, como construir e integrar múltiplos serviços independentes utilizando Docker de forma modular, escalável e organizada, cobrindo os fundamentos essenciais de sistemas distribuídos modernos.
