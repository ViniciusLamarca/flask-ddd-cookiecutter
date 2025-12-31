/**
 * Welcome Page JavaScript
 * 
 * Este arquivo contém a lógica JavaScript da página de boas-vindas.
 * Adicione aqui qualquer interatividade desejada.
 * 
 * Exemplo de uso:
 * - Animações de entrada
 * - Interações com elementos
 * - Validações de formulários (se houver)
 */

(function() {
    'use strict';

    /**
     * Inicialização quando o DOM estiver pronto
     */
    document.addEventListener('DOMContentLoaded', function() {
        console.log('Welcome page loaded');
        
        // Exemplo: Adicionar animação de fade-in nos cards
        animateCards();
        
        // Exemplo: Adicionar interatividade aos comandos
        setupCommandInteraction();
    });

    /**
     * Anima os cards com fade-in
     */
    function animateCards() {
        const cards = document.querySelectorAll('.info-card, .feature, .step');
        
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 100);
        });
    }

    /**
     * Adiciona interatividade aos comandos (copiar ao clicar)
     */
    function setupCommandInteraction() {
        const commands = document.querySelectorAll('.command');
        
        commands.forEach(command => {
            command.style.cursor = 'pointer';
            command.title = 'Clique para copiar';
            
            command.addEventListener('click', function() {
                const text = this.textContent.trim();
                copyToClipboard(text);
                showCopyFeedback(this);
            });
        });
    }

    /**
     * Copia texto para a área de transferência
     */
    function copyToClipboard(text) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(() => {
                console.log('Comando copiado:', text);
            });
        } else {
            // Fallback para navegadores mais antigos
            const textArea = document.createElement('textarea');
            textArea.value = text;
            textArea.style.position = 'fixed';
            textArea.style.opacity = '0';
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
        }
    }

    /**
     * Mostra feedback visual ao copiar
     */
    function showCopyFeedback(element) {
        const originalBg = element.style.backgroundColor;
        element.style.backgroundColor = '#28a745';
        element.style.transition = 'background-color 0.3s ease';
        
        setTimeout(() => {
            element.style.backgroundColor = originalBg || '';
        }, 300);
    }

    /**
     * Exemplo: Smooth scroll para seções
     */
    function setupSmoothScroll() {
        const links = document.querySelectorAll('a[href^="#"]');
        
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId && targetId !== '#') {
                    const target = document.querySelector(targetId);
                    if (target) {
                        e.preventDefault();
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                }
            });
        });
    }

})();

