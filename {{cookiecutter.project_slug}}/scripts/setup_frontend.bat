@echo off
REM Setup script for frontend dependencies - Windows

echo 🚀 Setting up frontend dependencies...

REM Check if Node.js is installed
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Node.js is not installed. Please install Node.js first.
    echo    Visit: https://nodejs.org/
    exit /b 1
)

REM Check if npm is installed
where npm >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ npm is not installed. Please install npm first.
    exit /b 1
)

echo ✅ Node.js version:
node --version
echo ✅ npm version:
npm --version

REM Install dependencies
echo 📦 Installing npm dependencies...
call npm install

REM Build assets
echo 🔨 Building assets...
call npm run build:css

REM Copy Alpine.js
if exist "node_modules\alpinejs\dist\alpine.min.js" (
    copy /Y "node_modules\alpinejs\dist\alpine.min.js" "app\presentation\static\js\alpine.js"
    echo ✅ Alpine.js copied
)

echo ✅ Frontend setup completed!

