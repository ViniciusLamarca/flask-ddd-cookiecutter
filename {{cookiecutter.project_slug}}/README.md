# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## 🏗️ Arquitetura

Este projeto utiliza **Domain-Driven Design (DDD)** combinado com **Clean Architecture**, organizando o código em camadas bem definidas:

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
│   ├── database/          # Banco de dados (SQLAlchemy)
│   ├── config/          # Configurações (Dynaconf)
│   ├── logging/         # Logging (Structlog)
│   └── redis/           # Redis client (opcional)
└── presentation/        # Camada de Apresentação
    ├── api/             # API REST
    ├── cli/             # Comandos CLI
    └── middleware/       # Middlewares
```

### Princípios da Arquitetura

- **Separação de Responsabilidades**: Cada camada tem uma responsabilidade específica
- **Inversão de Dependências**: Camadas internas não dependem de camadas externas
- **Testabilidade**: Código facilmente testável através de interfaces
- **Manutenibilidade**: Estrutura clara facilita manutenção e evolução

## 🚀 Tecnologias

- **Flask**: Framework web
- **SQL Server**: Banco de dados relacional
- **SQLAlchemy**: ORM para banco de dados
- **pyodbc**: Driver ODBC para SQL Server
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
{% if cookiecutter.use_redis == "y" %}
- **Redis**: Cache distribuído e message broker
- **Sistema de Cache**: Interface abstrata com implementação Redis, incluindo decorators para cache automático
{% endif %}
{% if cookiecutter.use_websocket == "y" %}
- **Flask-SocketIO**: WebSocket support para comunicação em tempo real
- **Eventlet**: Servidor assíncrono para WebSocket
{% endif %}

## 📋 Pré-requisitos

- Python {{ cookiecutter.python_version }}+
- Poetry
- Node.js 18+ e npm (para Tailwind CSS e Alpine.js)
- Git

## 🛠️ Instalação

1. **Clone o repositório** (se aplicável):
```bash
git clone <repository-url>
cd {{ cookiecutter.project_slug }}
```

2. **Instale as dependências Python**:
```bash
poetry install
```

3. **Instale as dependências frontend (Tailwind CSS + Alpine.js)**:
```bash
npm install
npm run build
```

Ou use o script de setup:
```bash
# Linux/macOS
./scripts/setup_frontend.sh

# Windows
scripts\setup_frontend.bat
```

> 💡 **Nota**: Se Node.js não estiver instalado, você pode pular este passo e configurar depois. 
> Consulte `FRONTEND_SETUP.md` para instruções detalhadas.

4. **Configure as variáveis de ambiente**:
```bash
cp env.example .env
# Edite o arquivo .env com suas configurações
```

5. **Execute as migrations**:
```bash
poetry run flask cli migrate
```

6. **Inicie o servidor**:
```bash
poetry run flask run
```

7. **Acesse a landing page de boas-vindas**:
Abra seu navegador em `http://localhost:5000` para ver a página de boas-vindas com informações do projeto e próximos passos.

## 🎨 Customizando a Landing Page

A página de boas-vindas (`/`) utiliza CSS modular para facilitar a customização.

### Estrutura de Arquivos

```
app/presentation/
├── templates/
│   └── welcome.html          # Template HTML
└── static/
    └── welcome/
        ├── welcome.css       # Estilos principais (modular)
        ├── welcome.js        # JavaScript para interatividade
        └── README.md         # Documentação de customização
```

### Customização Rápida

1. **Modificar cores**: Edite as variáveis CSS em `app/presentation/static/welcome/welcome.css`:

```css
:root {
    --primary-color: #3b82f6;    /* Sua cor primária */
    --secondary-color: #1e40af;   /* Sua cor secundária */
    --success-color: #10b981;     /* Cor de sucesso */
}
```

2. **Adicionar estilos customizados**: Crie um arquivo adicional e adicione no template:

```html
<link rel="stylesheet" href="{{ '{{' }} url_for('static', filename='welcome/welcome.css') {{ '}}' }}">
<link rel="stylesheet" href="{{ '{{' }} url_for('static', filename='welcome/custom.css') {{ '}}' }}">
```

3. **Ver exemplos**: Consulte `app/presentation/static/welcome/README.md` para documentação completa.

### Variáveis CSS Disponíveis

- `--primary-color`: Cor principal do tema
- `--secondary-color`: Cor secundária do tema
- `--success-color`: Cor de sucesso (features habilitadas)
- `--danger-color`: Cor de erro (features desabilitadas)
- `--bg-light`: Cor de fundo clara
- `--text-dark`: Cor de texto escura
- `--spacing-*`: Espaçamentos (small, medium, large)
- `--border-radius`: Raio de borda

Consulte `app/presentation/static/welcome/README.md` para documentação completa.

## 🎨 Tailwind CSS e Alpine.js

O projeto inclui **Tailwind CSS** e **Alpine.js** configurados localmente (sem CDN).

### Estrutura Frontend

```
app/presentation/
├── static/
│   ├── css/
│   │   ├── input.css      # Arquivo de entrada do Tailwind
│   │   └── output.css     # CSS compilado (gerado)
│   └── js/
│       └── alpine.js       # Alpine.js (copiado de node_modules)
└── templates/
    └── welcome.html       # Template usando Tailwind + Alpine.js
```

### Configuração

1. **Instalar dependências**:
```bash
npm install
```

2. **Compilar Tailwind CSS**:
```bash
npm run build:css
```

3. **Modo watch (desenvolvimento)**:
```bash
npm run watch:css
```

### Customização do Tailwind

Edite `tailwind.config.js` para customizar o tema:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#667eea',
          dark: '#764ba2',
        },
      },
    },
  },
}
```

### Uso do Tailwind CSS

Use classes utilitárias do Tailwind diretamente nos templates:

```html
<div class="bg-blue-500 text-white p-4 rounded-lg">
    Conteúdo estilizado
</div>
```

### Uso do Alpine.js

Alpine.js permite adicionar interatividade sem escrever JavaScript separado:

```html
<div x-data="{ open: false }">
    <button @click="open = !open">Toggle</button>
    <div x-show="open">Conteúdo visível</div>
</div>
```

### Scripts Disponíveis

- `npm run build:css` - Compila Tailwind CSS uma vez
- `npm run watch:css` - Compila Tailwind CSS em modo watch
- `npm run build` - Build completo (atualmente apenas CSS)

### Exemplo Completo

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <link rel="stylesheet" href="{{ '{{' }} url_for('static', filename='css/output.css') {{ '}}' }}">
</head>
<body>
    <div x-data="{ count: 0 }" class="p-8">
        <button @click="count++" class="bg-blue-500 text-white px-4 py-2 rounded">
            Clicou <span x-text="count"></span> vezes
        </button>
    </div>
    <script defer src="{{ '{{' }} url_for('static', filename='js/alpine.js') {{ '}}' }}"></script>
</body>
</html>
```

## 🔒 Qualidade de Código e Padrões

Este projeto possui **configurações rigorosas** para garantir qualidade e consistência do código.

### Ferramentas de Qualidade

- **Ruff**: Linter rápido e moderno (substitui Flake8, isort, etc)
- **MyPy**: Type checking estrito
- **Black**: Formatação automática
- **Pre-commit**: Hooks Git para validação automática
- **EditorConfig**: Padronização entre editores
- **Pylint**: Análise estática adicional (opcional)

### Configurações Aplicadas

#### Type Hints Obrigatórios
- Todas as funções devem ter type hints
- Return types obrigatórios
- Uso de `Any` desencorajado

#### Regras de Linting
- Máximo 100 caracteres por linha
- Máximo 7 argumentos por função
- Máximo 50 statements por função
- Máximo 12 branches por função
- Máximo 6 returns por função
- Nomes descritivos (sem variáveis de uma letra)
- Sem imports não utilizados
- Sem magic numbers/strings
- Sem try/except vazios

#### Segurança
- Detecção de secrets hardcoded
- Análise de segurança (Bandit)
- Validação de chaves privadas

### Uso das Ferramentas

#### Formatação
```bash
# Formatar código com Black
poetry run black .

# Ou com Ruff
poetry run ruff format .
```

#### Linting
```bash
# Verificar código com Ruff
poetry run ruff check .

# Corrigir automaticamente
poetry run ruff check . --fix
```

#### Type Checking
```bash
# Verificar tipos com MyPy
poetry run mypy app
```

#### Pre-commit Hooks
```bash
# Instalar hooks
poetry run pre-commit install

# Executar manualmente
poetry run pre-commit run --all-files
```

### Configuração do Editor

O projeto inclui configurações para VS Code:
- `.vscode/settings.json` - Configurações do editor
- `.vscode/extensions.json` - Extensões recomendadas
- `.vscode/launch.json` - Configurações de debug
- `.vscode/tasks.json` - Tarefas automatizadas

### Padrões de Código

Consulte `CODE_STANDARDS.md` para:
- Regras absolutas (nunca faça isso)
- Padrões obrigatórios
- Exemplos de boas práticas
- Checklist antes de commitar

### Validação Automática

Os pre-commit hooks validam automaticamente:
- ✅ Formatação (Black/Ruff)
- ✅ Linting (Ruff)
- ✅ Type checking (MyPy)
- ✅ Trailing whitespace
- ✅ End of file newline
- ✅ YAML/JSON/TOML válidos
- ✅ Merge conflicts
- ✅ Debug statements
- ✅ Secrets hardcoded
- ✅ Arquivos grandes

**Código que não passa na validação não pode ser commitado.**

## 📝 Comandos CLI

O projeto inclui um sistema CLI similar ao Artisan do Laravel:

### Migrations

```bash
# Executar migrations
poetry run flask cli migrate

# Criar nova migration
poetry run flask cli migrate:create "create users table"

# Executar migration específica
poetry run flask cli migrate --revision abc123
```

### Seed

```bash
# Popular banco de dados
poetry run flask cli seed
```

### Criar Componentes

```bash
# Criar novo domínio
poetry run flask cli create:domain users

# Criar caso de uso
poetry run flask cli create:use-case create-user --domain users

# Criar entidade
poetry run flask cli create:entity user --domain users

# Criar repositório
poetry run flask cli create:repository user --domain users

# Criar model SQLAlchemy
poetry run flask cli create:model user

# Criar controller
poetry run flask cli create:controller users --version v1
```

## 🧪 Testes

```bash
# Executar todos os testes
poetry run pytest

# Executar com coverage
poetry run pytest --cov=app --cov-report=html

# Executar testes específicos
poetry run pytest tests/unit/
poetry run pytest tests/integration/
```

## 🔍 Qualidade de Código

### Linting e Formatação

```bash
# Verificar código com Ruff
poetry run ruff check .

# Formatar código com Ruff
poetry run ruff format .

# Verificar tipos com MyPy
poetry run mypy app

# Formatar com Black
poetry run black .
```

### Pre-commit Hooks

```bash
# Instalar hooks
poetry run pre-commit install

# Executar hooks manualmente
poetry run pre-commit run --all-files
```

## 🔒 Segurança

### Executar Localmente

```bash
# SAST com Bandit
poetry run bandit -r app

# SCA com Safety
poetry export -f requirements.txt --output requirements.txt --without-hashes
poetry run safety check --file requirements.txt
```

## 📦 Estrutura de Projeto

### Domain Layer

Contém a lógica de negócio pura, sem dependências externas:

- **Entities**: Objetos de negócio com identidade
- **Value Objects**: Objetos imutáveis que representam conceitos de domínio
- **Repositories**: Interfaces para acesso a dados
- **Services**: Lógica de negócio que não pertence a uma entidade específica

### Application Layer

Orquestra casos de uso e coordena a camada de domínio:

- **Use Cases**: Operações específicas da aplicação
- **DTOs**: Estruturas de dados para transferência entre camadas
- **Interfaces**: Contratos para camada de aplicação

### Infrastructure Layer

Implementações concretas de tecnologias externas:

- **Database**: SQLAlchemy models e implementações de repositórios
- **Config**: Configurações com Dynaconf
- **Logging**: Setup de logging estruturado
{% if cookiecutter.use_redis == "y" %}
- **Redis**: Cliente Redis para cache e message broker
{% endif %}

### Presentation Layer

Interfaces com o mundo externo:

- **API**: Endpoints REST
- **CLI**: Comandos de linha de comando
- **Middleware**: Tratamento de erros e middlewares

## 🔧 Configuração

### Variáveis de Ambiente

O projeto usa Dynaconf para gerenciamento de configurações. Variáveis podem ser definidas em:

1. Arquivo `.env` (desenvolvimento)
2. Arquivo `app/infrastructure/config/settings.toml`
3. Variáveis de ambiente do sistema

Principais variáveis:

```env
FLASK_ENV=development
FLASK_DEBUG=true
SECRET_KEY=your-secret-key
# SQL Server connection string
# Format: mssql+pyodbc://username:password@server:port/database?driver=ODBC+Driver+17+for+SQL+Server
DATABASE_URL=mssql+pyodbc://sa:YourPassword@localhost:1433/YourDatabase?driver=ODBC+Driver+17+for+SQL+Server
{% if cookiecutter.use_redis == "y" %}
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=
REDIS_DB=0
{% endif %}
```

### Ambientes

O Dynaconf suporta múltiplos ambientes:

- `development`: Desenvolvimento local
- `testing`: Testes automatizados
- `production`: Produção

Defina o ambiente através da variável `FLASK_ENV`.

## 📊 Logging

O projeto usa Structlog para logging estruturado:

```python
import structlog

logger = structlog.get_logger()

logger.info("User created", user_id=123, email="user@example.com")
```

Logs são formatados em JSON em produção e de forma legível em desenvolvimento.

{% if cookiecutter.use_redis == "y" %}
## 💾 Cache

O projeto inclui um sistema de cache abstrato com implementação usando **Redis**, seguindo os princípios de Clean Architecture.

### Arquitetura de Cache

- **Interface**: `app/application/interfaces/cache.py` - Contrato abstrato de cache
- **Implementação**: `app/infrastructure/cache/redis_cache.py` - Implementação Redis
- **Decorators**: `app/infrastructure/cache/decorators.py` - Decorators para cache automático

### Uso Básico

```python
from app.infrastructure.cache.redis_cache import get_cache

cache = get_cache()

# Armazenar valor
cache.set("user:123", {"name": "John", "email": "john@example.com"}, ttl=300)

# Recuperar valor
user = cache.get("user:123")

# Verificar existência
if cache.exists("user:123"):
    print("User exists in cache")

# Deletar
cache.delete("user:123")

# Incrementar/Decrementar
cache.increment("counter:visits", amount=1)
cache.decrement("counter:visits", amount=1)
```

### Decorators de Cache

#### @cached - Cache automático de resultados

```python
from app.infrastructure.cache.decorators import cached

@cached(ttl=300)  # Cache por 5 minutos
def expensive_operation(user_id: int) -> dict:
    # Esta função será executada apenas se o resultado não estiver em cache
    return {"data": "expensive computation", "user_id": user_id}

# Primeira chamada - executa função e armazena em cache
result1 = expensive_operation(123)

# Segunda chamada - retorna do cache
result2 = expensive_operation(123)  # Não executa a função novamente
```

#### @cache_key - Cache com chave customizada

```python
from app.infrastructure.cache.decorators import cache_key

@cache_key("user:{user_id}:profile", ttl=600)
def get_user_profile(user_id: int) -> dict:
    return {"user_id": user_id, "profile": "..."}

# Cache key será: "user:123:profile"
profile = get_user_profile(123)
```

#### @invalidate_cache - Invalidar cache após operação

```python
from app.infrastructure.cache.decorators import invalidate_cache

@invalidate_cache("user:{user_id}:profile")
def update_user_profile(user_id: int, data: dict) -> dict:
    # Após atualizar, o cache será invalidado
    return update_profile_in_db(user_id, data)

# Após executar, o cache "user:123:profile" será deletado
update_user_profile(123, {"name": "New Name"})
```

### Exemplo Completo

```python
from app.infrastructure.cache.decorators import cached, invalidate_cache
from app.infrastructure.cache.redis_cache import get_cache

class UserService:
    @cached(ttl=300, key_prefix="user_profile")
    def get_user_profile(self, user_id: int) -> dict:
        # Busca do banco de dados
        return {"user_id": user_id, "name": "John"}
    
    @invalidate_cache("user_profile:user:{user_id}:*")
    def update_user_profile(self, user_id: int, data: dict) -> dict:
        # Atualiza no banco e invalida cache
        return update_in_database(user_id, data)
    
    def clear_user_cache(self, user_id: int):
        cache = get_cache()
        cache.clear(f"user_profile:user:{user_id}:*")
```

### Configuração

O cache usa as mesmas configurações do Redis definidas em `app/infrastructure/config/settings.toml`:

```toml
[redis]
host = "@env REDIS_HOST"
port = "@int @env REDIS_PORT"
password = "@env REDIS_PASSWORD"
db = 0
decode_responses = true
```

### Serialização

O cache suporta dois métodos de serialização:

- **JSON** (padrão): Para objetos simples (dict, list, str, int, float, bool)
- **Pickle**: Para objetos Python complexos (classes customizadas)

```python
from app.infrastructure.cache.redis_cache import RedisCache

# Cache com JSON (padrão)
cache_json = RedisCache(serializer="json")

# Cache com Pickle
cache_pickle = RedisCache(serializer="pickle")
```

### Limpeza de Cache

```python
from app.infrastructure.cache.redis_cache import get_cache

cache = get_cache()

# Limpar todas as chaves com prefixo
cache.clear()  # Limpa todas as chaves com prefixo padrão "cache:"

# Limpar chaves com padrão específico
cache.clear("user:*")  # Limpa todas as chaves que começam com "cache:user:"
```

{% endif %}

{% if cookiecutter.use_websocket == "y" %}
## 🔌 WebSocket

O projeto utiliza **Flask-SocketIO** para suporte a WebSocket, permitindo comunicação em tempo real entre cliente e servidor.

### Configuração

As configurações do WebSocket estão em `app/infrastructure/config/settings.toml`:

```toml
[socketio]
cors_allowed_origins = "*"  # Origens permitidas para CORS
async_mode = "eventlet"     # Modo assíncrono (eventlet, gevent, threading)
logger = false              # Habilitar logs do SocketIO
engineio_logger = false     # Habilitar logs do EngineIO
ping_timeout = 60           # Timeout para ping (segundos)
ping_interval = 25          # Intervalo entre pings (segundos)
```

### Uso

#### No Servidor

```python
from app.infrastructure.websocket.socketio import get_socketio

socketio = get_socketio()

# Emitir evento para todos os clientes
socketio.emit('event_name', {'data': 'value'})

# Emitir evento para um cliente específico
socketio.emit('event_name', {'data': 'value'}, room=session_id)

# Emitir evento para uma sala específica
socketio.emit('event_name', {'data': 'value'}, room='room_name')
```

#### Handlers de Eventos

Os handlers de eventos estão em `app/presentation/websocket/events.py`:

```python
from flask_socketio import emit

@socketio.on('my_event')
def handle_my_event(data):
    emit('my_response', {'data': data})
```

#### Namespaces

Namespaces permitem organizar eventos em diferentes contextos. Exemplo em `app/presentation/websocket/namespaces.py`:

```python
from flask_socketio import Namespace, emit

class MyNamespace(Namespace):
    def on_connect(self):
        emit('connected', {'message': 'Connected'})
    
    def on_custom_event(self, data):
        emit('custom_response', {'received': data})
```

### Cliente de Exemplo

Um exemplo de cliente HTML está disponível em `app/presentation/websocket/example_client.html`. Para testar:

1. Inicie o servidor: `poetry run flask run`
2. Abra o arquivo `example_client.html` no navegador
3. Conecte-se e teste os eventos

### Executar com WebSocket

Para executar o servidor com suporte a WebSocket:

```bash
# Desenvolvimento
poetry run flask run

# Ou usando SocketIO diretamente
poetry run python -c "from app import create_app; from app.infrastructure.websocket.socketio import get_socketio; app = create_app(); socketio = get_socketio(); socketio.run(app, host='0.0.0.0', port=5000)"
```

### Produção

Para produção, use um servidor WSGI/ASGI compatível com WebSocket, como:
- **Gunicorn** com workers eventlet/gevent
- **uWSGI** com suporte a WebSocket
- **Nginx** como reverse proxy

Exemplo com Gunicorn:

```bash
gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5000 app:create_app
```

{% endif %}

## 🗄️ Database

O projeto utiliza **SQL Server** como banco de dados, utilizando **pyodbc** como driver.

### Pré-requisitos

1. **SQL Server** instalado e rodando
2. **ODBC Driver 17 for SQL Server** (ou versão mais recente) instalado
   - Windows: Geralmente já incluído ou disponível no site da Microsoft
   - Linux: `sudo apt-get install unixodbc-dev` e instalar o driver ODBC
   - macOS: `brew install unixodbc` e instalar o driver ODBC

### Configuração da Connection String

A connection string do SQL Server segue o formato:

```
mssql+pyodbc://username:password@server:port/database?driver=ODBC+Driver+17+for+SQL+Server
```

Exemplos:

```env
# Local SQL Server
DATABASE_URL=mssql+pyodbc://sa:YourPassword@localhost:1433/YourDatabase?driver=ODBC+Driver+17+for+SQL+Server

# SQL Server com autenticação Windows (Windows apenas)
DATABASE_URL=mssql+pyodbc://server/database?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes

# SQL Server remoto
DATABASE_URL=mssql+pyodbc://username:password@192.168.1.100:1433/YourDatabase?driver=ODBC+Driver+17+for+SQL+Server
```

### Migrations

```bash
# Criar migration
poetry run flask cli migrate:create "description"

# Aplicar migrations
poetry run flask cli migrate

# Reverter migration
alembic downgrade -1
```

### Models

Models SQLAlchemy devem ser criados em `app/infrastructure/database/models/`:

```python
from app.infrastructure.database.session import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.getdate(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.getdate(), onupdate=db.func.getdate(), nullable=False)
```

**Nota**: SQL Server usa `db.func.getdate()` para timestamps ao invés de `datetime.utcnow()`.

## 📚 Exemplos

### Criar um Domínio Completo

```bash
# 1. Criar domínio
poetry run flask cli create:domain products

# 2. Criar entidade
poetry run flask cli create:entity product --domain products

# 3. Criar repositório
poetry run flask cli create:repository product --domain products

# 4. Criar caso de uso
poetry run flask cli create:use-case create-product --domain products

# 5. Criar model
poetry run flask cli create:model product

# 6. Criar controller
poetry run flask cli create:controller products --version v1
```

### Exemplo de Use Case

```python
from app.domain.repositories.product_repository import ProductRepository
from app.domain.entities.product import Product

class CreateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository
    
    def execute(self, name: str, price: float) -> Product:
        product = Product(name=name, price=price)
        return self.repository.save(product)
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 👤 Autor

**{{ cookiecutter.author_name }}**

- Email: {{ cookiecutter.author_email }}

## 🙏 Agradecimentos

- Flask community
- DDD e Clean Architecture communities
- Todos os mantenedores das bibliotecas utilizadas

