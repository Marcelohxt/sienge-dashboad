// Funções para criação de gráficos usando Plotly
function createChart(elementId, data, layout) {
    Plotly.newPlot(elementId, data, {
        ...layout,
        template: 'plotly_dark',
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: {
            color: '#a0aec0'
        },
        margin: {
            l: 50,
            r: 30,
            t: 50,
            b: 50
        }
    });
}

// Animações suaves para cards
document.addEventListener('DOMContentLoaded', function() {
    // Animação para cards
    const cards = document.querySelectorAll('.dashboard-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Toggle do sidebar
    const menuToggle = document.getElementById('menu-toggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById('wrapper').classList.toggle('toggled');
        });
    }

    // Inicialização de tooltips do Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Atualização dinâmica de números
    function animateValue(element, start, end, duration) {
        if (start === end) return;
        const range = end - start;
        const increment = end > start ? 1 : -1;
        const stepTime = Math.abs(Math.floor(duration / range));
        let current = start;
        const timer = setInterval(function() {
            current += increment;
            element.textContent = current;
            if (current == end) {
                clearInterval(timer);
            }
        }, stepTime);
    }

    // Animar números nos cards
    document.querySelectorAll('[data-value]').forEach(element => {
        const value = parseInt(element.getAttribute('data-value'));
        animateValue(element, 0, value, 1000);
    });
});

// Função para formatar valores monetários
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

// Função para formatar datas
function formatDate(date) {
    return new Intl.DateTimeFormat('pt-BR').format(new Date(date));
}

// Função para atualizar dados em tempo real (simulação)
function updateRealTimeData() {
    const cards = document.querySelectorAll('.dashboard-card');
    cards.forEach(card => {
        const valueElement = card.querySelector('.card-text');
        if (valueElement) {
            const currentValue = parseInt(valueElement.textContent);
            const newValue = currentValue + Math.floor(Math.random() * 10) - 5;
            valueElement.textContent = Math.max(0, newValue);
        }
    });
}

// Atualizar dados a cada 30 segundos
setInterval(updateRealTimeData, 30000);

// Configuração do tema escuro para gráficos
const darkTheme = {
    background: 'transparent',
    paper_bgcolor: 'transparent',
    font: {
        color: '#a0aec0'
    },
    plot_bgcolor: 'transparent',
    xaxis: {
        gridcolor: 'rgba(255,255,255,0.1)',
        zerolinecolor: 'rgba(255,255,255,0.1)'
    },
    yaxis: {
        gridcolor: 'rgba(255,255,255,0.1)',
        zerolinecolor: 'rgba(255,255,255,0.1)'
    }
};

// Função para inicializar gráficos com tema escuro
function initDarkChart(elementId, data, layout = {}) {
    Plotly.newPlot(elementId, data, {
        ...darkTheme,
        ...layout
    });
}