#!/bin/bash
# Script para publicar o template no GitHub
# Execute: chmod +x publish.sh && ./publish.sh

echo "🚀 Publicando Flask DDD Cookiecutter Template no GitHub..."
echo ""

# Verificar se gh está instalado
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) não está instalado!"
    echo "   Instale em: https://cli.github.com/"
    exit 1
fi

# Verificar autenticação
echo "🔐 Verificando autenticação GitHub..."
if ! gh auth status &> /dev/null; then
    echo "❌ Você não está autenticado no GitHub CLI!"
    echo ""
    echo "Execute o seguinte comando para autenticar:"
    echo "   gh auth login"
    echo ""
    echo "Ou execute este script novamente após autenticar."
    exit 1
fi

echo "✅ Autenticado!"
echo ""

# Criar repositório
echo "📦 Criando repositório público no GitHub..."
gh repo create ViniciusLamarca/flask-ddd-cookiecutter \
    --public \
    --source=. \
    --remote=origin \
    --description "Flask DDD + Clean Architecture Cookiecutter Template - Similar to Laravel Artisan"

if [ $? -ne 0 ]; then
    echo "❌ Erro ao criar repositório!"
    echo "   Verifique se o repositório já existe ou se há problemas de permissão."
    exit 1
fi

echo "✅ Repositório criado!"
echo ""

# Fazer push
echo "📤 Fazendo push do código..."
git push -u origin main

if [ $? -ne 0 ]; then
    echo "❌ Erro ao fazer push!"
    exit 1
fi

echo ""
echo "✅ Template publicado com sucesso!"
echo ""
echo "🌐 Repositório: https://github.com/ViniciusLamarca/flask-ddd-cookiecutter"
echo ""
echo "📝 Para usar o template:"
echo "   cookiecutter https://github.com/ViniciusLamarca/flask-ddd-cookiecutter"
echo ""

