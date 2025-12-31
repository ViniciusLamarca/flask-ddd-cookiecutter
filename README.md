# Flask DDD + Clean Architecture Cookiecutter Template

Template Cookiecutter para criar projetos Flask com arquitetura DDD + Clean Architecture, similar ao Artisan do Laravel.

## 🚀 Uso

### Instalação do Cookiecutter

```bash
pip install cookiecutter
```

### Gerar Novo Projeto

```bash
cookiecutter https://github.com/ViniciusLamarca/flask-ddd-cookiecutter
```

Ou clone o repositório e use localmente:

```bash
git clone https://github.com/ViniciusLamarca/flask-ddd-cookiecutter.git
cd flask-ddd-cookiecutter
cookiecutter .
```

### Perguntas do Template

O template fará as seguintes perguntas:

1. **project_name**: Nome do projeto (ex: "My Flask Project")
2. **project_slug**: Slug do projeto (gerado automaticamente do nome)
3. **project_description**: Descrição do projeto
4. **author_name**: Nome do autor
5. **author_email**: Email do autor
6. **use_redis**: Se deseja incluir suporte ao Redis (y/n)
7. **use_websocket**: Se deseja incluir suporte ao WebSocket (y/n)
8. **python_version**: Versão do Python (padrão: 3.11)

### Exemplo de Uso

```bash
$ cookiecutter https://github.com/ViniciusLamarca/flask-ddd-cookiecutter

project_name [My Flask Project]: E-commerce API
project_slug [e-commerce-api]: 
project_description [A Flask application with DDD and Clean Architecture]: API para e-commerce
author_name [Your Name]: João Silva
author_email [your.email@example.com]: joao@example.com
use_redis [y]: y
use_websocket [y]: y
python_version [3.11]: 3.11
```

## 📦 O que o Template Inclui

- ✅ Estrutura DDD + Clean Architecture completa
- ✅ Flask com factory pattern
- ✅ SQL Server + SQLAlchemy + Alembic para ORM e migrations
- ✅ Pydantic para validação
- ✅ Structlog para logging estruturado
- ✅ Dynaconf para configurações
- ✅ Poetry para gerenciamento de dependências
- ✅ Ruff + MyPy para linting e type checking
- ✅ Black para formatação
- ✅ Sistema CLI similar ao Artisan
- ✅ Suporte opcional ao Redis (com sistema de cache abstrato)
- ✅ Suporte opcional ao WebSocket (Flask-SocketIO)
- ✅ Tailwind CSS + Alpine.js (instalados localmente, sem CDN)
- ✅ Pre-commit hooks
- ✅ EditorConfig para padronização
- ✅ Configurações VS Code
- ✅ Landing page de boas-vindas

## 🎯 Comandos CLI Disponíveis

Após gerar o projeto:

```bash
cd <project-slug>
poetry install
npm install
npm run build
poetry run pre-commit install
poetry run flask cli migrate
poetry run flask cli create:domain users
poetry run flask cli create:use-case create-user --domain users
poetry run flask cli create:controller users --version v1
# ... etc
```

## 📚 Documentação

Consulte o README.md gerado no projeto para documentação completa.

## 🎨 Frontend (Tailwind CSS + Alpine.js)

O template inclui Tailwind CSS e Alpine.js configurados localmente:

- **Tailwind CSS**: Framework CSS utility-first
- **Alpine.js**: Framework JavaScript leve e reativo
- **Build automatizado**: Scripts npm para compilação
- **Sem CDN**: Tudo instalado localmente

Após gerar o projeto, execute:
```bash
npm install
npm run build
```

Consulte `FRONTEND_SETUP.md` no projeto gerado para detalhes.

## 🔒 Qualidade de Código

O template inclui configurações rigorosas para garantir qualidade:

- **Ruff**: Linter rápido e moderno
- **MyPy**: Type checking estrito
- **Black**: Formatação automática
- **Pre-commit**: Hooks Git para validação automática
- **EditorConfig**: Padronização entre editores

## 🏗️ Arquitetura

O template utiliza **Domain-Driven Design (DDD)** combinado com **Clean Architecture**:

```
app/
├── domain/              # Camada de Domínio (DDD)
│   ├── entities/        # Entidades de domínio
│   ├── value_objects/   # Value Objects
│   ├── repositories/    # Interfaces de repositório
│   └── services/        # Serviços de domínio
├── application/         # Camada de Aplicação
│   ├── use_cases/       # Casos de uso
│   ├── dto/             # Data Transfer Objects
│   └── interfaces/      # Interfaces de aplicação
├── infrastructure/      # Camada de Infraestrutura
│   ├── database/        # Banco de dados (SQLAlchemy)
│   ├── config/          # Configurações (Dynaconf)
│   ├── logging/         # Logging (Structlog)
│   ├── redis/           # Redis client (opcional)
│   └── cache/           # Sistema de cache (opcional)
└── presentation/        # Camada de Apresentação
    ├── api/             # API REST
    ├── cli/             # Comandos CLI
    ├── websocket/       # WebSocket handlers (opcional)
    └── templates/        # Templates HTML
```

## 🛠️ Tecnologias

- **Flask**: Framework web
- **SQL Server**: Banco de dados relacional
- **SQLAlchemy**: ORM para banco de dados
- **Alembic**: Migrations
- **Pydantic**: Validação de dados
- **Structlog**: Logging estruturado
- **Dynaconf**: Gerenciamento de configurações
- **Poetry**: Gerenciamento de dependências
- **Ruff**: Linter e formatter
- **MyPy**: Type checking
- **Black**: Code formatter
- **Pytest**: Framework de testes
- **Tailwind CSS**: Framework CSS utility-first
- **Alpine.js**: Framework JavaScript leve e reativo
- **Pre-commit**: Git hooks para qualidade de código
- **EditorConfig**: Padronização entre editores

## 📝 Licença

Este template é fornecido como está, livre para uso em projetos pessoais e comerciais.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 👤 Autor

**Vinicius Lamarca**

- GitHub: [@ViniciusLamarca](https://github.com/ViniciusLamarca)

## ⭐ Star History

Se este template foi útil para você, considere dar uma ⭐ no repositório!

