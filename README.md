# 🌵 Raízes do Nordeste API

API REST desenvolvida em **Python** utilizando **FastAPI**, **SQLAlchemy** e **SQLite** para gerenciamento da Rede **Raízes do Nordeste**.

O sistema permite o gerenciamento de clientes, produtos, categorias, unidades, estoque, pedidos, pagamentos, programa de fidelidade, autenticação via JWT e suporte à multicanalidade.

---

# 📂 Repositório

Código-fonte disponível em:

**GitHub**

https://github.com/ZxCaique/raizes-api

Clone o projeto:

```bash
git clone https://github.com/ZxCaique/raizes-api.git
```

---

# 🚀 Demonstração

Após executar a aplicação, acesse:

## Swagger

```
http://127.0.0.1:8000/docs
```

## ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📚 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- SQLite
- Pydantic v2
- Uvicorn
- Passlib (bcrypt)
- Python-Jose (JWT)

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
git clone https://github.com/ZxCaique/raizes-api.git
```

Ou faça o download do projeto em formato ZIP.

---

## 2. Criar ambiente virtual

```bash
python -m venv .venv
```

---

## 3. Ativar ambiente virtual

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 5. Executar a API

```bash
uvicorn app.main:app --reload
```

---

# 🔐 Autenticação

A API utiliza autenticação JWT para proteger os endpoints.

Fluxo recomendado:

1. Registrar um usuário
2. Realizar login
3. Copiar o Access Token
4. Clicar em **Authorize** no Swagger
5. Informar o token JWT
6. Utilizar normalmente as rotas protegidas

---

# 📌 Funcionalidades

## Usuários

- Cadastro
- Login
- Autenticação JWT

## Clientes

- Cadastro
- Consulta
- Atualização
- Exclusão

## Categorias

- CRUD completo

## Produtos

- CRUD completo

## Unidades

- CRUD completo

## Estoque

- Cadastro
- Atualização
- Consulta geral
- Consulta por unidade
- Consulta por produto/unidade
- Entrada de estoque

## Pedidos

- Criação de pedidos
- Controle de itens
- Atualização de status
- Registro do canal de origem
- Consulta por canal
- Consulta por status

## Pagamentos

- Pagamento Mock
- Registro da forma de pagamento
- Código de transação

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

# 🌐 Multicanalidade

A API implementa o conceito de multicanalidade conforme o estudo de caso.

Cada pedido registra obrigatoriamente seu canal de origem através do campo:

```
canalPedido
```

Canais disponíveis:

- APP
- TOTEM
- BALCAO
- PICKUP
- WEB

Também é possível filtrar pedidos por canal e status.

Exemplo:

```
GET /pedidos?canalPedido=TOTEM&status=AGUARDANDO_PAGAMENTO
```

---

# 💳 Formas de Pagamento

Cada pedido registra a forma de pagamento escolhida.

Opções disponíveis:

- MOCK
- PIX
- CARTAO_CREDITO
- CARTAO_DEBITO
- DINHEIRO

O endpoint de pagamento utiliza um gateway simulado (Mock), retornando um código de transação para fins de teste.

---

# 📦 Banco de Dados

O projeto utiliza SQLite.

Arquivo criado automaticamente:

```
raizes.db
```

---

# 📌 Principais Endpoints

| Método | Endpoint |
|---------|----------|
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
| GET | /estoque/unidade/{id} |
| GET | /estoque/unidade/{id}/produto/{id} |
| PATCH | /estoque/{id}/entrada |
| POST | /estoque |
| GET | /pedidos |
| POST | /pedidos |
| PATCH | /pedidos/{id}/status |
| POST | /pagamentos/processar |
| GET | /fidelidade/{cliente_id} |
| POST | /fidelidade/{cliente_id}/adicionar-pontos |
| GET | /relatorios/resumo |
| GET | /relatorios/vendas |
| GET | /relatorios/estoque-baixo |

---

# 🧪 Execução dos Testes

Os testes da API foram realizados utilizando o **Postman**, conforme os requisitos da atividade prática.

## Arquivos

Na pasta:

```
postman/
```

estão disponíveis:

- raizes-api-postman-collection.json
- raizes-api-postman-environment.json

Importe ambos no Postman.

---

## Ordem recomendada

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

Antes dos testes execute:

- Criar Cliente
- Criar Categoria
- Criar Produto
- Criar Unidade
- Criar Estoque

---

## Cenários implementados

| ID | Cenário | Resultado Esperado |
|----|----------|-------------------|
| T01 | Login válido | 200 + Access Token |
| T02 | Acesso sem Token | 401 |
| T03 | Cadastro de Cliente | 200 |
| T04 | E-mail inválido | 422 |
| T05 | Pedido sem canalPedido | 422 |
| T06 | Produto inexistente | 404 |
| T07 | Consulta de estoque por unidade | 200 |
| T08 | Pedido válido | 200 |
| T09 | Estoque insuficiente | 400 |
| T10 | Pagamento Mock | 200 |
| T11 | Consulta por canal/status | 200 |
| T12 | Relatório resumo | 200 |

---

## Token JWT

O token é obtido através de:

```
POST /auth/login
```

No Postman o token é salvo automaticamente na variável:

```
{{token}}
```

Caso seja necessário configurar manualmente:

```
Authorization

Bearer Token

{{token}}
```

---

## Reiniciando o Banco

Caso deseje reiniciar os testes:

Excluir:

```
raizes.db
```

Executar novamente:

```bash
uvicorn app.main:app --reload
```

O banco será recriado automaticamente.

---

# 📋 Observações

- A documentação da API está disponível via Swagger/OpenAPI.
- Os testes encontram-se organizados em coleções do Postman.
- Todos os endpoints protegidos utilizam autenticação JWT.
- O sistema implementa multicanalidade através do campo **canalPedido**.
- Os pedidos podem ser filtrados por canal e status.
- O pagamento é processado por um gateway Mock.
- O estoque é controlado por unidade, permitindo consultas específicas por unidade e produto.

---

# ⚠️ Requisitos não implementados

## Controle de Perfis (403)

A autenticação via JWT foi implementada.

Entretanto, o controle de autorização por perfil (ADMIN, GERENTE e ATENDENTE) ainda não foi implementado.

## Logs e Auditoria

Não foi implementado mecanismo de logs e auditoria.

A prioridade do desenvolvimento foi atender ao fluxo principal do sistema, incluindo autenticação, estoque, pedidos, pagamentos, fidelidade e multicanalidade.

---

# 👨‍💻 Desenvolvedor

**Caique Reis**

Projeto desenvolvido para a disciplina **Projeto Multidisciplinar – Trilha Back-End**.

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
