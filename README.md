# API de Filmes

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-green.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)](https://www.sqlalchemy.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)

Uma API RESTful robusta e escalável para gerenciar um banco de dados de filmes, construída com FastAPI e SQLAlchemy. Este projeto demonstra as melhores práticas no desenvolvimento de APIs, incluindo separação adequada de responsabilidades, validação de dados e integração com banco de dados.

## 🚀 Funcionalidades

- **Operações CRUD**: Criar, Ler, Atualizar e Deletar filmes
- **Validação de Dados**: Esquemas Pydantic para validação de requisições/respostas
- **Integração com Banco de Dados**: ORM SQLAlchemy com MySQL
- **Tratamento de Erros**: Tratamento abrangente de exceções HTTP
- **Documentação da API**: Documentação Swagger UI gerada automaticamente
- **Arquitetura Modular**: Separação limpa entre controladores, serviços, modelos e esquemas

## 🛠 Tecnologias

- **Backend**: Python 3.8+
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Banco de Dados**: MySQL
- **Validação**: Pydantic
- **Driver**: PyMySQL

## 📁 Estrutura do Projeto

```
movieAPI/
├── app/
│   ├── main.py                 # Ponto de entrada da aplicação FastAPI
│   ├── controllers/
│   │   └── movie_controller.py # Endpoints da API para operações com filmes
│   ├── services/
│   │   └── movie_service.py    # Camada de lógica de negócio
│   ├── models/
│   │   └── movie_model.py      # Modelos de banco de dados SQLAlchemy
│   ├── schemas/
│   │   └── movie_schema.py     # Esquemas Pydantic para requisições/respostas
│   ├── database/
│   │   └── connection.py       # Configuração do banco de dados e gerenciamento de sessão
│   └── utils/                  # Funções utilitárias (se houver)
├── .venv/                      # Ambiente virtual
├── README.md                   # Documentação do projeto
└── requirements.txt            # Dependências Python
```

## 🔧 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- MySQL 8.0 ou superior
- Git

### Configuração

1. **Clone o repositório**
   ```bash
   git clone https://github.com/yourusername/movieAPI.git
   cd movieAPI
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**
   - Crie um banco de dados MySQL chamado `moviesapi`
   - Atualize as credenciais do banco em `app/database/connection.py` se necessário
   - A aplicação criará automaticamente as tabelas necessárias na primeira execução

5. **Execute a aplicação**
   ```bash
   uvicorn app.main:app --reload
   ```

A API estará disponível em `http://localhost:8000`

## 📖 Uso

### Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Endpoint raiz com status da API |
| POST | `/movies/` | Criar um novo filme |
| GET | `/movies/{movie_id}` | Obter um filme por ID |
| PUT | `/movies/{movie_id}` | Atualizar um filme por ID |
| DELETE | `/movies/{movie_id}` | Deletar um filme por ID |

### Exemplos de Requisições

**Criar um Filme**
```bash
curl -X POST "http://localhost:8000/movies/" \
     -H "Content-Type: application/json" \
     -d '{"title": "Inception", "year": 2010, "genre": "Sci-Fi"}'
```

**Obter um Filme**
```bash
curl -X GET "http://localhost:8000/movies/1"
```

### Documentação da API

Visite `http://localhost:8000/docs` para a documentação interativa do Swagger UI.

## 🧪 Testes

```bash
# Execute com pytest (se testes forem adicionados)
pytest
```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do repositório
2. Crie uma branch de funcionalidade (`git checkout -b feature/FuncionalidadeIncrivel`)
3. Faça commit das suas mudanças (`git commit -m 'Adiciona alguma FuncionalidadeIncrivel'`)
4. Faça push para a branch (`git push origin feature/FuncionalidadeIncrivel`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Seu Nome**  
- GitHub: [@Reynanz](https://github.com/Reynanz)
- LinkedIn: [Reynan Santana](https://linkedin.com/in/reynan-santana)


---

⭐ Se este projeto foi útil para você, por favor dê uma estrela!
