# Instruções para Publicar no GitHub

## Passo 1: Autenticar no GitHub CLI

```bash
gh auth login
```

Siga as instruções para autenticar. Escolha:
- GitHub.com
- HTTPS
- Autenticar via navegador (recomendado)

## Passo 2: Criar Repositório Público

```bash
gh repo create ViniciusLamarca/flask-ddd-cookiecutter --public --source=. --remote=origin --description "Flask DDD + Clean Architecture Cookiecutter Template - Similar to Laravel Artisan"
```

## Passo 3: Fazer Push

```bash
git push -u origin main
```

## Alternativa: Criar Manualmente

Se preferir criar o repositório manualmente no GitHub:

1. Acesse https://github.com/new
2. Nome do repositório: `flask-ddd-cookiecutter`
3. Descrição: `Flask DDD + Clean Architecture Cookiecutter Template - Similar to Laravel Artisan`
4. Visibilidade: **Público**
5. Não inicialize com README, .gitignore ou licença (já temos)
6. Clique em "Create repository"
7. Execute:

```bash
git remote add origin https://github.com/ViniciusLamarca/flask-ddd-cookiecutter.git
git branch -M main
git push -u origin main
```

## Após Publicar

O template estará disponível para uso via:

```bash
cookiecutter https://github.com/ViniciusLamarca/flask-ddd-cookiecutter
```

