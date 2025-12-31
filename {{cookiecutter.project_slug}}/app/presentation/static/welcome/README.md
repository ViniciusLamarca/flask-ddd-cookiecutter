# Welcome Page - Arquivos Modulares

Esta pasta contém os arquivos CSS e JavaScript modulares da página de boas-vindas.

## Estrutura

```
welcome/
├── welcome.css    # Estilos principais (modular com variáveis CSS)
├── welcome.js     # JavaScript para interatividade
└── README.md      # Esta documentação
```

## Customização

### CSS - Variáveis CSS

O arquivo `welcome.css` utiliza variáveis CSS para facilitar a customização. Edite as variáveis na seção `:root`:

```css
:root {
    /* Cores Principais */
    --primary-color: #667eea;      /* Cor primária do tema */
    --secondary-color: #764ba2;     /* Cor secundária */
    --success-color: #28a745;       /* Cor de sucesso */
    --danger-color: #dc3545;        /* Cor de erro */
    
    /* Cores de Fundo */
    --bg-primary: #ffffff;
    --bg-secondary: #f8f9fa;
    --bg-dark: #2d3748;
    
    /* Espaçamentos */
    --spacing-xs: 5px;
    --spacing-sm: 10px;
    --spacing-md: 15px;
    --spacing-lg: 20px;
    --spacing-xl: 30px;
    --spacing-xxl: 40px;
    
    /* E mais... */
}
```

### Exemplo de Customização

Para mudar o tema para azul, por exemplo:

```css
:root {
    --primary-color: #3b82f6;
    --secondary-color: #1e40af;
    --gradient-primary: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
}
```

### JavaScript

O arquivo `welcome.js` contém funcionalidades interativas:

- **Animações de entrada**: Cards aparecem com fade-in
- **Copiar comandos**: Clique em qualquer comando para copiar
- **Smooth scroll**: Navegação suave entre seções

Você pode adicionar mais funcionalidades conforme necessário.

## Uso no Template

No arquivo `welcome.html`, os arquivos são referenciados assim:

```html
<link rel="stylesheet" href="{{ '{{' }} url_for('static', filename='welcome/welcome.css') {{ '}}' }}">
<script src="{{ '{{' }} url_for('static', filename='welcome/welcome.js') {{ '}}' }}"></script>
```

## Boas Práticas

1. **Mantenha as variáveis CSS organizadas**: Agrupe por categoria (cores, espaçamentos, etc.)
2. **Use nomes semânticos**: `--primary-color` ao invés de `--blue`
3. **Documente customizações**: Adicione comentários explicando o propósito
4. **Teste responsividade**: Verifique em diferentes tamanhos de tela
5. **Mantenha o JavaScript modular**: Separe funcionalidades em funções

## Estrutura CSS

O CSS está organizado em seções:

- **Variáveis CSS**: Customização fácil
- **Reset e Base**: Estilos base
- **Container Principal**: Layout principal
- **Header**: Cabeçalho da página
- **Content**: Área de conteúdo
- **Sections**: Seções de conteúdo
- **Components**: Cards, features, steps, commands
- **Footer**: Rodapé
- **Responsive**: Media queries

Cada seção está claramente marcada com comentários para fácil navegação.

