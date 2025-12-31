#!/bin/bash
# Setup script for frontend dependencies

set -e

echo "🚀 Setting up frontend dependencies..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    echo "   Visit: https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"

# Install dependencies
echo "📦 Installing npm dependencies..."
npm install

# Build assets
echo "🔨 Building assets..."
npm run build:css

# Copy Alpine.js
if [ -f "node_modules/alpinejs/dist/alpine.min.js" ]; then
    cp node_modules/alpinejs/dist/alpine.min.js app/presentation/static/js/alpine.js
    echo "✅ Alpine.js copied"
fi

echo "✅ Frontend setup completed!"

