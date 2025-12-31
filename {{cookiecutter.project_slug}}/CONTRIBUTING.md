# Guia de Contribuição

Obrigado por considerar contribuir para este projeto! Este guia ajudará você a entender como contribuir de forma eficaz.

## 🚀 Começando

1. **Clone o repositório**
2. **Instale as dependências**:
   ```bash
   poetry install
   npm install
   ```

3. **Configure o ambiente**:
   ```bash
   cp .env.example .env
   # Edite .env com suas configurações
   ```

4. **Instale os pre-commit hooks**:
   ```bash
   poetry run pre-commit install
   ```

## 📋 Processo de Contribuição

### 1. Criar uma Branch

```bash
git checkout -b feature/nome-da-feature
# ou
git checkout -b fix/nome-do-bug
```

### 2. Desenvolver

- Siga os padrões de código definidos em `CODE_STANDARDS.md`
- Escreva código limpo e bem documentado
- Adicione testes para novas funcionalidades
- Mantenha a cobertura de testes alta

### 3. Validar Localmente

Antes de fazer commit, execute:

```bash
# Formatação
poetry run black .

# Linting
poetry run ruff check . --fix

# Type checking
poetry run mypy app

# Testes
poetry run pytest

# Pre-commit (valida tudo)
poetry run pre-commit run --all-files
```

### 4. Commitar

Os pre-commit hooks validarão automaticamente seu código. Se algo falhar:

1. Corrija os problemas
2. Tente commitar novamente

**Nunca pule os hooks com `--no-verify`!**

### 5. Push e Pull Request

```bash
git push origin feature/nome-da-feature
```

Crie um Pull Request descrevendo:
- O que foi feito
- Por que foi feito
- Como testar
- Screenshots (se aplicável)

## ✅ Checklist de Pull Request

- [ ] Código segue `CODE_STANDARDS.md`
- [ ] Type hints em todas as funções
- [ ] Docstrings em funções públicas
- [ ] Testes adicionados/atualizados
- [ ] Todos os testes passando
- [ ] Linting passou (Ruff)
- [ ] Type checking passou (MyPy)
- [ ] Formatação aplicada (Black)
- [ ] Pre-commit hooks passaram
- [ ] Documentação atualizada (se necessário)
- [ ] Sem warnings ou erros

## 🎯 Padrões de Código

### Type Hints Obrigatórios

```python
# ❌ ERRADO
def process(data):
    return data.upper()

# ✅ CORRETO
def process(data: str) -> str:
    return data.upper()
```

### Documentação

```python
def create_user(email: str, name: str) -> User:
    """
    Create a new user.
    
    Args:
        email: User email address
        name: User full name
    
    Returns:
        Created User instance
    
    Raises:
        ValueError: If email is invalid
    """
    # ...
```

### Nomenclatura

- `snake_case` para funções, variáveis, métodos
- `PascalCase` para classes
- `UPPER_CASE` para constantes
- Nomes descritivos e semânticos

### Estrutura

- Máximo 100 caracteres por linha
- Máximo 7 argumentos por função
- Máximo 50 statements por função
- Funções pequenas e focadas

## 🧪 Testes

### Executar Testes

```bash
# Todos os testes
poetry run pytest

# Com cobertura
poetry run pytest --cov=app --cov-report=html

# Testes específicos
poetry run pytest tests/unit/test_user.py

# Modo verbose
poetry run pytest -v
```

### Escrever Testes

```python
import pytest
from app.domain.entities.user import User


def test_create_user():
    """Test user creation."""
    user = User(email="test@example.com", name="Test User")
    assert user.email == "test@example.com"
    assert user.name == "Test User"
```

## 📝 Commits

Use mensagens de commit descritivas:

```bash
# ✅ BOM
git commit -m "feat: add user authentication"
git commit -m "fix: resolve database connection issue"
git commit -m "docs: update API documentation"

# ❌ RUIM
git commit -m "fix"
git commit -m "update"
git commit -m "changes"
```

### Convenção de Commits

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação (não afeta código)
- `refactor:` Refatoração
- `test:` Testes
- `chore:` Tarefas de manutenção

## 🔍 Code Review

Todas as contribuições passam por code review. Seja receptivo a feedback e esteja aberto a melhorias.

### Critérios de Review

- Código segue padrões
- Funcionalidade funciona corretamente
- Testes adequados
- Documentação atualizada
- Sem regressões

## ❓ Dúvidas?

Se tiver dúvidas, abra uma issue ou entre em contato com os mantenedores.

## 🙏 Obrigado!

Sua contribuição é muito valorizada. Obrigado por ajudar a melhorar este projeto!

