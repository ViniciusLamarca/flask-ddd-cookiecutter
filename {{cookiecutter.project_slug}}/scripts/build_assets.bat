@echo off
REM Build script for frontend assets (Tailwind CSS + Alpine.js) - Windows

echo 🔨 Building frontend assets...

REM Check if node_modules exists
if not exist "node_modules" (
    echo 📦 Installing npm dependencies...
    call npm install
)

REM Build Tailwind CSS
echo 🎨 Building Tailwind CSS...
call npm run build:css

REM Copy Alpine.js from node_modules
echo 📦 Copying Alpine.js...
if exist "node_modules\alpinejs\dist\alpine.min.js" (
    copy /Y "node_modules\alpinejs\dist\alpine.min.js" "app\presentation\static\js\alpine.js"
    echo ✅ Alpine.js copied successfully
) else (
    echo ⚠️  Alpine.js not found in node_modules. Please run 'npm install' first.
)

echo ✅ Build completed successfully!

