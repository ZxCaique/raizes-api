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

# 🧪 Execução dos Testes

A validação da API foi realizada utilizando o **Postman**, conforme os requisitos da atividade prática.

## Arquivos de Teste

O repositório contém:

- `raizes-api-postman-collection.json`
- `raizes-api-postman-environment.json`

Importe ambos no Postman antes de executar os testes.

---

## Ambiente

Antes de iniciar os testes:

1. Ative o ambiente virtual.

Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a API:

```bash
uvicorn app.main:app --reload
```

4. Acesse a API em:

```
http://127.0.0.1:8000
```

---

## Ordem recomendada dos testes

Os testes devem ser executados na seguinte sequência para garantir que todas as dependências estejam criadas corretamente.

### 1. Autenticação

- T00 – Registrar usuário ADMIN
- T01 – Login válido

Ao executar o login, o token JWT é salvo automaticamente na variável `token` da coleção.

---

### 2. Seed (dados iniciais)

Executar:

- Seed 01 – Criar cliente base
- Seed 02 – Criar categoria base
- Seed 03 – Criar produto base
- Seed 04 – Criar unidade base
- Seed 05 – Criar estoque base

Esses registros são utilizados pelos testes seguintes.

---

### 3. Fluxos positivos

Executar:

- T03 – Criar cliente válido
- T08 – Criar pedido válido (multicanal)
- T10 – Pagamento mock aprovado
- T11 – Filtrar pedidos por canal e status
- T12 – Relatório resumo

---

### 4. Fluxos negativos

Executar:

- T02 – Acesso sem token
- T04 – Cliente com e-mail inválido
- T05 – Pedido sem campo obrigatório `canalPedido`
- T06 – Pedido com produto inexistente
- T09 – Pedido com estoque insuficiente

---

# Cenários de teste implementados

| ID | Cenário | Resultado esperado |
|----|----------|--------------------|
| T01 | Login válido | 200 + access_token |
| T02 | Acesso sem token | 401 (ou 403, conforme configuração do HTTPBearer) |
| T03 | Cadastro de cliente válido | 200 |
| T04 | E-mail inválido | 422 |
| T05 | Pedido sem `canalPedido` | 422 |
| T06 | Produto inexistente | 404 |
| T08 | Pedido válido | 200 |
| T09 | Estoque insuficiente | 400 |
| T10 | Pagamento mock aprovado | 200 + status do pedido atualizado |
| T11 | Consulta de pedidos por canal/status | 200 |
| T12 | Resumo geral | 200 |

---

## Token JWT

O token é obtido automaticamente após o teste **T01 – Login válido**.

Caso seja necessário informar manualmente, utilize o endpoint:

```
POST /auth/login
```

Após copiar o campo `access_token`, configure o Authorization do Postman como:

```
Bearer Token
```

e utilize a variável:

```
{{token}}
```

---

## Banco de Dados

A aplicação utiliza **SQLite**.

Caso seja necessário reiniciar os testes do zero, exclua o arquivo:

```
raizes.db
```

Em seguida execute novamente:

```bash
uvicorn app.main:app --reload
```

O banco será recriado automaticamente.

---

## Observações

- Os testes foram organizados em pastas no Postman conforme os módulos da aplicação.
- O fluxo principal contempla autenticação, cadastro, estoque, pedidos, pagamento mock, programa de fidelidade e relatórios.
- A autenticação utiliza JWT e é obrigatória para os endpoints protegidos.
- O sistema implementa multicanalidade por meio do campo `canalPedido`, permitindo registrar e filtrar pedidos por canal de origem (APP, TOTEM, BALCAO, PICKUP e WEB).

## Observações sobre requisitos não implementados

O controle de autorização por perfil ainda não foi implementado nesta versão. A API valida a autenticação via JWT, mas não diferencia permissões entre ADMIN, GERENTE e ATENDENTE. Por isso, o cenário de acesso com perfil sem permissão (403) foi documentado como limitação conhecida.

Logs/auditoria também não foram implementados nesta versão. A decisão foi priorizar o fluxo principal de negócio: autenticação, cadastro, estoque, pedidos, pagamento mock, fidelidade e relatórios.

# 👨‍💻 Desenvolvedor

Projeto desenvolvido por **Caique Reis** como trabalho acadêmico da disciplina Projeto: Desenvolvimento Back-end.

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
