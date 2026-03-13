# 🎬 MovieAPI

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135.1-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8%2B-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)

API REST para **cadastrar, listar, atualizar e remover filmes** usando **FastAPI + SQLAlchemy + MySQL**.

Se você nunca viu FastAPI, sem medo: este projeto foi feito para ser **fácil de rodar** e **fácil de entender**. 🙂

## ✨ O que tem aqui

- 🚀 FastAPI com documentação automática: `GET /docs` (Swagger) e `GET /redoc`
- 🧱 Arquitetura em camadas (controller/service/model/schema)
- ✅ Validação com Pydantic v2
- 🗄️ SQLAlchemy ORM com MySQL via `pymysql`

## 🧭 Como o código está organizado

Fluxo:

`Request -> Controller (rotas) -> Service (regras/CRUD) -> Model (ORM) -> Schema (resposta)`

Pastas principais:

- 🧷 `app/main.py`: cria a aplicação FastAPI e registra as rotas
- 🧭 `app/controllers/movie_controller.py`: endpoints `/movies/...` e erros HTTP
- 🧰 `app/services/movie_service.py`: lógica de CRUD e acesso ao banco
- 🧱 `app/models/movie_model.py`: modelo ORM `Movie`
- 🧾 `app/schemas/movie_schema.py`: schemas Pydantic (Create/Update/Response)
- 🔌 `app/database/connection.py`: conexão MySQL (engine + `SessionLocal`)

## 🗃️ Banco de dados

Tabela `movies`:

- `id` (int, PK, autoincrement)
- `title` (varchar(50))
- `year` (int)
- `genre` (varchar(20))

SQL mínimo para criar:

```sql
CREATE DATABASE IF NOT EXISTS moviesapi;
USE moviesapi;

CREATE TABLE IF NOT EXISTS movies (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(50) NOT NULL,
  year INT NOT NULL,
  genre VARCHAR(20) NOT NULL
);
```

🔧 Conexão do banco (ajuste aqui se necessário): `app/database/connection.py`

- `DB_USER` (padrão: `root`)
- `DB_PASSWORD` (padrão: vazio)
- `DB_HOST` (padrão: `localhost`)
- `DB_NAME` (padrão: `moviesapi`)

## 🔗 Endpoints

Base local: `http://127.0.0.1:8000`

| Método | Rota | O que faz |
|---|---|---|
| GET | `/` | Lista todos os filmes |
| POST | `/movies/` | Cria um filme |
| GET | `/movies/{movie_id}` | Busca filme por ID |
| PUT | `/movies/{movie_id}` | Atualiza filme por ID (parcial) |
| DELETE | `/movies/{movie_id}` | Remove filme por ID |

## 🧾 Schemas (exemplos)

`MovieCreate`

```json
{ "title": "The Matrix", "year": 1999, "genre": "Sci-Fi" }
```

`MovieUpdate` (tudo opcional)

```json
{ "genre": "Action" }
```

`MovieResponse`

```json
{ "id": 1, "title": "The Matrix", "year": 1999, "genre": "Sci-Fi" }
```

## 🚀 Rodando localmente (Windows / PowerShell)

### 1) ✅ Dependências

- MySQL em execução (local ou remoto)
- Python (no Windows, o comando `py` costuma existir)

### 2) 📦 Instalar pacotes

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3) ▶️ Subir a API

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Abra no navegador:

- 📚 Swagger UI: `http://127.0.0.1:8000/docs`
- 📘 ReDoc: `http://127.0.0.1:8000/redoc`

## 🧪 Testando rapidinho (cURL)

Criar um filme:

```bash
curl -X POST "http://127.0.0.1:8000/movies/" \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"The Matrix\",\"year\":1999,\"genre\":\"Sci-Fi\"}"
```

Listar todos:

```bash
curl "http://127.0.0.1:8000/"
```

Buscar por ID:

```bash
curl "http://127.0.0.1:8000/movies/1"
```

Atualizar (parcial):

```bash
curl -X PUT "http://127.0.0.1:8000/movies/1" \
  -H "Content-Type: application/json" \
  -d "{\"genre\":\"Action\"}"
```

Remover:

```bash
curl -X DELETE "http://127.0.0.1:8000/movies/1"
```

## 🛠️ Notas (para quem está curioso)

- 🧾 `app/database/connection.py` usa `echo=True`: o SQL aparece no console (ótimo para debug)
- 🧼 O service abre/fecha sessão por operação: `create/get/update/delete` ficam bem diretos

## 🆘 Dúvidas comuns

**1) Está dando erro de conexão com o MySQL**

- Confira `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` em `app/database/connection.py`
- Garanta que o banco `moviesapi` e a tabela `movies` existem (SQL acima)

**2) Onde vejo todos os endpoints bonitinhos?**

- `http://127.0.0.1:8000/docs`

## 🧭 Próximas melhorias (se quiser deixar “nível produção”)

- 🔐 Ler credenciais de `.env` (ao invés de hardcode)
- 🧪 Testes com `pytest`
- 🐳 Docker Compose (API + MySQL)
- 🔎 Paginação e filtros (ano/gênero/título)
