# 🌵 Raízes do Nordeste API

API REST desenvolvida em **Python** utilizando **FastAPI**, **SQLAlchemy** e **SQLite** para gerenciamento da Rede Raízes do Nordeste.

O sistema permite o gerenciamento de clientes, produtos, categorias, unidades, estoque, pedidos, pagamentos, programa de fidelidade e autenticação via JWT.

---

## 📚 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- SQLite
- Pydantic v2
- Uvicorn
- Passlib (bcrypt)
- Python-Jose (JWT)

---

## 📁 Estrutura do Projeto

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

ou baixe o projeto em ZIP.

---

## 2. Criar ambiente virtual

Windows

```bash
python -m venv .venv
```

---

## 3. Ativar o ambiente virtual

PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Prompt de Comando (CMD)

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

Após iniciar a API, acesse:

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

Fluxo:

1. Registrar usuário
2. Realizar login
3. Copiar o Access Token
4. Clicar em **Authorize** no Swagger
5. Informar o Token JWT
6. Utilizar as rotas protegidas

---

# 📌 Funcionalidades

## Usuários

- Cadastro
- Login
- Autenticação JWT

## Clientes

- Cadastrar
- Listar
- Buscar
- Atualizar
- Excluir

## Categorias

- CRUD completo

## Produtos

- CRUD completo

## Unidades

- CRUD completo

## Estoque

- Cadastro de estoque
- Atualização de quantidade
- Consulta de estoque

## Pedidos

- Criação de pedidos
- Controle de itens
- Atualização de status

## Pagamentos

- Processamento de pagamentos
- Geração de código de transação

## Programa de Fidelidade

- Cadastro
- Consulta
- Acúmulo de pontos
- Níveis Bronze, Prata e Ouro

## Relatórios

- Resumo geral
- Total de vendas
- Estoque baixo

---

# 📦 Banco de Dados

O projeto utiliza SQLite.

Arquivo criado automaticamente:

```
raizes.db
```

---

# 📌 Endpoints Principais

| Método | Endpoint |
|---------|-----------|
| POST | /auth/registrar |
| POST | /auth/login |
| GET | /clientes |
| POST | /clientes |
| GET | /categorias |
| POST | /categorias |
| GET | /produtos |
| POST | /produtos |
| GET | /unidades |
| POST | /unidades |
| GET | /estoque |
| POST | /estoque |
| GET | /pedidos |
| POST | /pedidos |
| POST | /pagamentos/processar |
| GET | /fidelidade/{cliente_id} |
| GET | /relatorios/resumo |

---

# 👨‍💻 Desenvolvedor

Projeto desenvolvido por **Caique Reis** como trabalho acadêmico da disciplina de Desenvolvimento Back-end.

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
