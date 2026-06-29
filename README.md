# 🌵 Raízes do Nordeste API

API REST desenvolvida em **Python** utilizando **FastAPI**, **SQLAlchemy** e **SQLite** para gerenciamento da Rede **Raízes do Nordeste**.

O sistema permite o gerenciamento de clientes, produtos, categorias, unidades, estoque, pedidos, pagamentos, programa de fidelidade e autenticação via JWT.

---
# 📚 Tecnologias Utilizadas

* Python 3.12
* FastAPI
* SQLAlchemy 2.0
* SQLite
* Pydantic v2
* Uvicorn
* Passlib (bcrypt)
* Python-Jose (JWT)

---

# 📁 Estrutura do Projeto

```
raizes-api/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── main.py
│
├── postman/
│   ├── raizes-api-postman-collection.json
│   └── raizes-api-postman-environment.json
│
├── requirements.txt
├── README.md
└── raizes.db
```

---

# ⚙️ Instalação

## 1. Clonar o projeto

```bash
git clone <url-do-repositorio>
```

Ou faça o download do projeto em formato ZIP.

---

## 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

---

## 3. Ativar o ambiente virtual

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

---

## 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 5. Executar a API

```bash
uvicorn app.main:app --reload
```

---

# 📖 Documentação

Após iniciar a aplicação, acesse:

Swagger

```
http://127.0.0.1:8000/docs
```

Redoc

```
http://127.0.0.1:8000/redoc
```

---

# 🔐 Autenticação

A API utiliza autenticação JWT.

Fluxo recomendado:

1. Registrar usuário.
2. Realizar login.
3. Copiar o Access Token.
4. Clicar em **Authorize** no Swagger.
5. Informar o Token JWT.
6. Utilizar as rotas protegidas.

---

# 📌 Funcionalidades

## Usuários

* Cadastro
* Login
* Autenticação JWT

## Clientes

* Cadastro
* Consulta
* Atualização
* Exclusão

## Categorias

* CRUD completo

## Produtos

* CRUD completo

## Unidades

* CRUD completo

## Estoque

* Cadastro de estoque
* Atualização de quantidade
* Consulta de estoque

## Pedidos

* Criação de pedidos
* Controle de itens
* Atualização de status
* Registro do canal de origem do pedido
* Consulta por canal e status

## Pagamentos

* Pagamento mock
* Registro da forma de pagamento
* Geração de código de transação

## Programa de Fidelidade

* Cadastro
* Consulta
* Acúmulo de pontos
* Níveis Bronze, Prata e Ouro

## Relatórios

* Resumo geral
* Total de vendas
* Estoque baixo

---

# 🌐 Multicanalidade

A API implementa o conceito de multicanalidade conforme o estudo de caso.

Cada pedido registra obrigatoriamente seu canal de origem por meio do campo `canalPedido`.

Canais suportados:

* APP
* TOTEM
* BALCAO
* PICKUP
* WEB

Também é possível consultar pedidos por canal e status.

Exemplo:

```
GET /pedidos?canalPedido=TOTEM&status=AGUARDANDO_PAGAMENTO
```

---

# 💳 Formas de Pagamento

Cada pedido registra a forma de pagamento escolhida.

Formas disponíveis:

* MOCK
* PIX
* CARTAO_CREDITO
* CARTAO_DEBITO
* DINHEIRO

O endpoint de pagamento utiliza um gateway simulado (mock), retornando um código de transação para fins de teste.

---

# 📦 Banco de Dados

O projeto utiliza SQLite.

Arquivo criado automaticamente:

```
raizes.db
```

---

# 📌 Principais Endpoints

| Método | Endpoint                 |
| ------ | ------------------------ |
| POST   | /auth/registrar          |
| POST   | /auth/login              |
| GET    | /clientes                |
| POST   | /clientes                |
| GET    | /categorias              |
| POST   | /categorias              |
| GET    | /produtos                |
| POST   | /produtos                |
| GET    | /unidades                |
| POST   | /unidades                |
| GET    | /estoque                 |
| POST   | /estoque                 |
| GET    | /pedidos                 |
| POST   | /pedidos                 |
| POST   | /pagamentos/processar    |
| GET    | /fidelidade/{cliente_id} |
| GET    | /relatorios/resumo       |

---

# 🧪 Execução dos Testes

A validação da API foi realizada utilizando o **Postman**.

## Arquivos de Teste

Os arquivos utilizados encontram-se na pasta:

```
postman/
```

Arquivos:

* `raizes-api-postman-collection.json`
* `raizes-api-postman-environment.json`

Importe ambos no Postman antes da execução.

---

## Ambiente

1. Ative o ambiente virtual.

```powershell
.\.venv\Scripts\Activate.ps1
```

2. Instale as dependências.

```bash
pip install -r requirements.txt
```

3. Execute a API.

```bash
uvicorn app.main:app --reload
```

4. Utilize o ambiente:

```
http://127.0.0.1:8000
```

---

## Ordem recomendada dos testes

Execute na seguinte sequência:

1. Auth
2. Seed
3. Clientes
4. Categorias
5. Produtos
6. Unidades
7. Estoque
8. Pedidos
9. Pagamentos
10. Fidelidade
11. Relatórios
12. Erros

---

## Seed

Antes dos testes principais execute:

* Seed 01 – Criar cliente
* Seed 02 – Criar categoria
* Seed 03 – Criar produto
* Seed 04 – Criar unidade
* Seed 05 – Criar estoque

---

## Cenários implementados

| ID  | Cenário                   | Resultado Esperado |
| --- | ------------------------- | ------------------ |
| T01 | Login válido              | 200 + access_token |
| T02 | Acesso sem token          | 401/403            |
| T03 | Cadastro de cliente       | 200                |
| T04 | E-mail inválido           | 422                |
| T05 | Pedido sem canalPedido    | 422                |
| T06 | Produto inexistente       | 404                |
| T08 | Pedido válido             | 200                |
| T09 | Estoque insuficiente      | 400                |
| T10 | Pagamento mock aprovado   | 200                |
| T11 | Consulta por canal/status | 200                |
| T12 | Relatório resumo          | 200                |

---

## Token JWT

O token é obtido através do endpoint:

```
POST /auth/login
```

O Postman salva automaticamente o token na variável:

```
{{token}}
```

Caso seja necessário configurar manualmente, utilize:

```
Authorization
Bearer Token
{{token}}
```

---

## Reiniciando o banco

Caso seja necessário reiniciar os testes:

1. Exclua o arquivo:

```
raizes.db
```

2. Execute novamente:

```bash
uvicorn app.main:app --reload
```

O banco SQLite será recriado automaticamente.

---

# Observações

* Os testes estão organizados em pastas no Postman conforme os módulos da aplicação.
* O fluxo principal contempla autenticação, estoque, pedidos, pagamento mock, fidelidade e relatórios.
* A autenticação utiliza JWT para proteger os endpoints.
* O sistema implementa multicanalidade por meio do campo `canalPedido`.
* Os pedidos podem ser filtrados por canal e status.
* As formas de pagamento ficam registradas juntamente com o pedido.

---

# Requisitos não implementados

## Controle de perfis (403)

A autenticação via JWT foi implementada.

Entretanto, o controle de autorização baseado em perfis (ADMIN, GERENTE e ATENDENTE) não foi implementado nesta versão.

## Logs e Auditoria

Não foi implementado mecanismo de logs ou auditoria.

A prioridade do desenvolvimento foi atender ao fluxo principal do sistema (autenticação, pedidos, pagamentos, fidelidade, estoque e multicanalidade).

---

# 👨‍💻 Desenvolvedor

Projeto desenvolvido por **Caique Reis** para a disciplina **Projeto Multidisciplinar – Trilha Back-End**.

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
