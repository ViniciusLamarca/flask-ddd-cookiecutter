# Flask DDD + Clean Architecture Cookiecutter Template

Template Cookiecutter para criar projetos Flask com arquitetura DDD + Clean Architecture, similar ao Artisan do Laravel.

## 🚀 Uso

### Instalação do Cookiecutter

```bash
pip install cookiecutter
```

### Gerar Novo Projeto

```bash
cookiecutter <caminho-para-este-template>
```

Ou se estiver usando diretamente:

```bash
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
$ cookiecutter .

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
- ✅ SQLAlchemy + Alembic para ORM e migrations
- ✅ Pydantic para validação
- ✅ Structlog para logging estruturado
- ✅ Dynaconf para configurações
- ✅ Poetry para gerenciamento de dependências
- ✅ Ruff + MyPy para linting e type checking
- ✅ Black para formatação
- ✅ Sistema CLI similar ao Artisan
- ✅ Suporte opcional ao Redis
- ✅ Suporte opcional ao WebSocket (Flask-SocketIO)
- ✅ Tailwind CSS + Alpine.js (instalados localmente, sem CDN)
- ✅ Pre-commit hooks

## 🎯 Comandos CLI Disponíveis

Após gerar o projeto:

```bash
cd <project-slug>
poetry install
poetry run flask cli migrate
poetry run flask cli create:domain users
poetry run flask cli create:use-case create-user --domain users
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

## 🔧 Personalização

Você pode personalizar o template editando:

- `cookiecutter.json`: Variáveis do template
- `hooks/post_gen_project.py`: Scripts pós-geração
- Arquivos em `{{cookiecutter.project_slug}}/`: Estrutura do projeto


