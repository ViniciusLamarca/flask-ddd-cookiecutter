# Padrões de Código e Regras de Qualidade

Este documento define os padrões de código e regras que **DEVEM** ser seguidas para garantir qualidade e consistência.

## 🚫 Regras Absolutas - NUNCA Faça Isso

### 1. Type Hints Obrigatórios
```python
# ❌ ERRADO
def process_data(data):
    return data.upper()

# ✅ CORRETO
def process_data(data: str) -> str:
    return data.upper()
```

### 2. Sem `any` ou `Any` sem Justificativa
```python
# ❌ ERRADO
def process(data: Any) -> Any:
    pass

# ✅ CORRETO
def process(data: dict[str, str]) -> dict[str, int]:
    pass
```

### 3. Sem Imports Não Utilizados
```python
# ❌ ERRADO
from typing import List, Dict, Tuple  # Tuple não é usado

# ✅ CORRETO
from typing import List, Dict
```

### 4. Sem Variáveis de Uma Letra (exceto em loops)
```python
# ❌ ERRADO
def calculate(x, y):
    z = x + y
    return z

# ✅ CORRETO
def calculate(first_number: int, second_number: int) -> int:
    result = first_number + second_number
    return result

# ✅ CORRETO (loops)
for i in range(10):
    print(i)
```

### 5. Sem Funções Sem Documentação
```python
# ❌ ERRADO
def get_user(id):
    return User.query.get(id)

# ✅ CORRETO
def get_user(user_id: int) -> User | None:
    """
    Retrieve a user by ID.
    
    Args:
        user_id: The user identifier
    
    Returns:
        User instance or None if not found
    """
    return User.query.get(user_id)
```

### 6. Sem Magic Numbers/Strings
```python
# ❌ ERRADO
if status == 200:
    process()

# ✅ CORRETO
HTTP_OK = 200
if status == HTTP_OK:
    process()
```

### 7. Sem Try/Except Vazios
```python
# ❌ ERRADO
try:
    risky_operation()
except:
    pass

# ✅ CORRETO
try:
    risky_operation()
except SpecificError as e:
    logger.error("Operation failed", error=str(e))
    raise
```

### 8. Sem Print Statements (exceto em CLI/scripts)
```python
# ❌ ERRADO
def process_data():
    print("Processing...")
    # código

# ✅ CORRETO
import structlog
logger = structlog.get_logger()

def process_data():
    logger.info("Processing data")
    # código
```

### 9. Sem Hardcoded Secrets/Passwords
```python
# ❌ ERRADO
password = "admin123"
api_key = "sk-1234567890"

# ✅ CORRETO
password = os.getenv("ADMIN_PASSWORD")
api_key = settings.API_KEY
```

### 10. Sem Funções Muito Longas ou Complexas
```python
# ❌ ERRADO - Função com 100+ linhas

# ✅ CORRETO - Quebrar em funções menores
def process_user_data(user_data: dict) -> User:
    validated_data = validate_user_data(user_data)
    user = create_user(validated_data)
    send_welcome_email(user)
    return user
```

## ✅ Padrões Obrigatórios

### Type Hints
- **SEMPRE** use type hints em funções e métodos
- **SEMPRE** use return types
- **SEMPRE** use `|` para union types (Python 3.10+)
- **NUNCA** use `Any` sem justificativa em comentário

### Nomenclatura
- **snake_case** para funções, variáveis, métodos
- **PascalCase** para classes
- **UPPER_CASE** para constantes
- Nomes descritivos e semânticos

### Documentação
- **SEMPRE** documente funções públicas
- Use docstrings no formato Google ou NumPy
- Documente parâmetros e retornos

### Estrutura de Código
- Máximo 100 caracteres por linha
- Máximo 7 argumentos por função
- Máximo 50 statements por função
- Máximo 12 branches por função
- Máximo 6 returns por função

### Imports
- Ordem: stdlib, third-party, local
- Um import por linha (exceto `from typing`)
- Use `from typing import` para type hints
- Evite `import *`

### Error Handling
- **SEMPRE** capture exceções específicas
- **SEMPRE** logue erros
- **SEMPRE** forneça contexto útil
- **NUNCA** silencie erros sem motivo

## 🔍 Ferramentas de Validação

### Pre-commit Hooks
Execute antes de cada commit:
```bash
poetry run pre-commit run --all-files
```

### Linting
```bash
# Ruff (rápido e moderno)
poetry run ruff check .

# MyPy (type checking)
poetry run mypy app
```

### Formatação
```bash
# Black (formatação automática)
poetry run black .

# Ruff format (alternativa)
poetry run ruff format .
```

## 📋 Checklist Antes de Commitar

- [ ] Type hints em todas as funções
- [ ] Docstrings em funções públicas
- [ ] Sem imports não utilizados
- [ ] Sem variáveis de uma letra (exceto loops)
- [ ] Sem magic numbers/strings
- [ ] Sem try/except vazios
- [ ] Sem print statements (exceto CLI)
- [ ] Sem hardcoded secrets
- [ ] Funções não muito longas (< 50 statements)
- [ ] Código formatado (Black/Ruff)
- [ ] Linting passou (Ruff)
- [ ] Type checking passou (MyPy)
- [ ] Pre-commit hooks passaram

## 🎯 Exemplos de Boas Práticas

### Função Bem Escrita
```python
from typing import Optional
import structlog

logger = structlog.get_logger()


def create_user(
    email: str,
    name: str,
    age: int | None = None
) -> User:
    """
    Create a new user in the system.
    
    Args:
        email: User email address (must be unique)
        name: User full name
        age: User age (optional)
    
    Returns:
        Created User instance
    
    Raises:
        ValueError: If email is invalid or already exists
        DatabaseError: If database operation fails
    """
    if not email or "@" not in email:
        raise ValueError("Invalid email address")
    
    logger.info("Creating user", email=email, name=name)
    
    try:
        user = User(email=email, name=name, age=age)
        db.session.add(user)
        db.session.commit()
        logger.info("User created successfully", user_id=user.id)
        return user
    except IntegrityError as e:
        logger.error("User creation failed", error=str(e))
        db.session.rollback()
        raise ValueError("Email already exists") from e
```

### Classe Bem Escrita
```python
from dataclasses import dataclass
from typing import Protocol


class UserRepository(Protocol):
    """Repository interface for user operations."""
    
    def find_by_id(self, user_id: int) -> User | None:
        """Find user by ID."""
        ...
    
    def save(self, user: User) -> User:
        """Save user."""
        ...


@dataclass
class User:
    """User domain entity."""
    
    id: int | None
    email: str
    name: str
    age: int | None = None
    
    def is_adult(self) -> bool:
        """Check if user is an adult."""
        return self.age is not None and self.age >= 18
```

## 🚨 Regras Específicas por Camada

### Domain Layer
- **NUNCA** importe de camadas externas
- **SEMPRE** use dataclasses ou classes simples
- **SEMPRE** defina interfaces (Protocol) para repositórios

### Application Layer
- **SEMPRE** use DTOs para transferência de dados
- **SEMPRE** valide entrada
- **NUNCA** acesse banco de dados diretamente

### Infrastructure Layer
- **SEMPRE** implemente interfaces da camada de domínio
- **SEMPRE** trate erros de infraestrutura
- **NUNCA** exponha detalhes de implementação

### Presentation Layer
- **SEMPRE** valide entrada com Pydantic
- **SEMPRE** retorne status codes apropriados
- **NUNCA** coloque lógica de negócio

## 📚 Referências

- [PEP 8](https://pep8.org/) - Style Guide for Python Code
- [PEP 484](https://peps.python.org/pep-0484/) - Type Hints
- [PEP 257](https://peps.python.org/pep-0257/) - Docstring Conventions
- [Clean Code Python](https://github.com/zedr/clean-code-python)

## ⚠️ Penalidades

Código que não segue estes padrões será:
1. Rejeitado em code review
2. Bloqueado por pre-commit hooks
3. Marcado como falha no CI/CD

**Não há exceções. Qualidade é não negociável.**

