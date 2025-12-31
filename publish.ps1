# Script para publicar o template no GitHub
# Execute: .\publish.ps1

Write-Host "🚀 Publicando Flask DDD Cookiecutter Template no GitHub..." -ForegroundColor Cyan
Write-Host ""

# Verificar se gh está instalado
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "❌ GitHub CLI (gh) não está instalado!" -ForegroundColor Red
    Write-Host "   Instale em: https://cli.github.com/" -ForegroundColor Yellow
    exit 1
}

# Verificar autenticação
Write-Host "🔐 Verificando autenticação GitHub..." -ForegroundColor Yellow
$authStatus = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Você não está autenticado no GitHub CLI!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Execute o seguinte comando para autenticar:" -ForegroundColor Yellow
    Write-Host "   gh auth login" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Ou execute este script novamente após autenticar." -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Autenticado!" -ForegroundColor Green
Write-Host ""

# Criar repositório
Write-Host "📦 Criando repositório público no GitHub..." -ForegroundColor Yellow
gh repo create ViniciusLamarca/flask-ddd-cookiecutter `
    --public `
    --source=. `
    --remote=origin `
    --description "Flask DDD + Clean Architecture Cookiecutter Template - Similar to Laravel Artisan"

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro ao criar repositório!" -ForegroundColor Red
    Write-Host "   Verifique se o repositório já existe ou se há problemas de permissão." -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Repositório criado!" -ForegroundColor Green
Write-Host ""

# Fazer push
Write-Host "📤 Fazendo push do código..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro ao fazer push!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "✅ Template publicado com sucesso!" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Repositório: https://github.com/ViniciusLamarca/flask-ddd-cookiecutter" -ForegroundColor Cyan
Write-Host ""
Write-Host "📝 Para usar o template:" -ForegroundColor Yellow
Write-Host "   cookiecutter https://github.com/ViniciusLamarca/flask-ddd-cookiecutter" -ForegroundColor Cyan
Write-Host ""

