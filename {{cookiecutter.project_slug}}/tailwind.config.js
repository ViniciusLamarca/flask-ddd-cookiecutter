/** @type {import('tailwindcss').Config} */
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
        success: '#28a745',
        danger: '#dc3545',
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        mono: ['Courier New', 'monospace'],
      },
    },
  },
  plugins: [],
}

