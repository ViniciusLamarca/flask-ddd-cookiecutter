#!/bin/bash
# Build script for frontend assets (Tailwind CSS + Alpine.js)

set -e

echo "🔨 Building frontend assets..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing npm dependencies..."
    npm install
fi

# Build Tailwind CSS
echo "🎨 Building Tailwind CSS..."
npm run build:css

# Copy Alpine.js from node_modules
echo "📦 Copying Alpine.js..."
if [ -f "node_modules/alpinejs/dist/alpine.min.js" ]; then
    cp node_modules/alpinejs/dist/alpine.min.js app/presentation/static/js/alpine.js
    echo "✅ Alpine.js copied successfully"
else
    echo "⚠️  Alpine.js not found in node_modules. Please run 'npm install' first."
fi

echo "✅ Build completed successfully!"

