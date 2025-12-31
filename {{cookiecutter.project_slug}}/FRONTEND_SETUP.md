# Setup Frontend - Tailwind CSS + Alpine.js

Este projeto utiliza **Tailwind CSS** e **Alpine.js** instalados localmente (sem CDN).

## 🚀 Setup Rápido

### Opção 1: Script Automatizado

**Linux/macOS:**
```bash
chmod +x scripts/setup_frontend.sh
./scripts/setup_frontend.sh
```

**Windows:**
```cmd
scripts\setup_frontend.bat
```

### Opção 2: Manual

1. **Instalar dependências npm**:
```bash
npm install
```

2. **Compilar Tailwind CSS**:
```bash
npm run build:css
```

3. **Copiar Alpine.js** (se necessário):
```bash
# Linux/macOS
cp node_modules/alpinejs/dist/alpine.min.js app/presentation/static/js/alpine.js

# Windows
copy node_modules\alpinejs\dist\alpine.min.js app\presentation\static\js\alpine.js
```

## 📦 Estrutura

```
app/presentation/static/
├── css/
│   ├── input.css      # Entrada Tailwind (edite aqui)
│   └── output.css     # CSS compilado (gerado automaticamente)
└── js/
    └── alpine.js      # Alpine.js (copiado de node_modules)
```

## 🔨 Comandos Disponíveis

- `npm run build:css` - Compila Tailwind CSS uma vez
- `npm run watch:css` - Compila Tailwind CSS em modo watch (desenvolvimento)
- `npm run build` - Build completo

## ⚙️ Configuração

### Tailwind CSS

Edite `tailwind.config.js` para customizar:

```javascript
module.exports = {
  content: [
    "./app/presentation/templates/**/*.html",
    "./app/presentation/static/**/*.js",
  ],
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

### Arquivo de Entrada CSS

Edite `app/presentation/static/css/input.css` para adicionar estilos customizados:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
    .btn-custom {
        @apply bg-primary text-white px-4 py-2 rounded;
    }
}
```

## 🎯 Uso nos Templates

### Tailwind CSS

```html
<div class="bg-blue-500 text-white p-4 rounded-lg shadow-lg">
    Conteúdo estilizado
</div>
```

### Alpine.js

```html
<div x-data="{ count: 0 }">
    <button @click="count++">Clicou <span x-text="count"></span> vezes</button>
</div>
<script defer src="{{ '{{' }} url_for('static', filename='js/alpine.js') {{ '}}' }}"></script>
```

## 📝 Notas Importantes

1. **Sempre compile o Tailwind** após modificar `input.css` ou templates
2. **Use `watch:css`** durante desenvolvimento para recompilação automática
3. **O arquivo `output.css`** é gerado automaticamente - não edite diretamente
4. **Alpine.js** deve ser incluído com `defer` para melhor performance

## 🔍 Troubleshooting

### Tailwind não está funcionando

1. Verifique se `output.css` foi gerado
2. Execute `npm run build:css` novamente
3. Verifique se o template está importando `output.css`

### Alpine.js não está funcionando

1. Verifique se o arquivo `app/presentation/static/js/alpine.js` existe
2. Se não existir, copie de `node_modules/alpinejs/dist/alpine.min.js`
3. Verifique se o script está incluído com `defer`

## 📚 Documentação

- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Alpine.js Docs](https://alpinejs.dev/)

