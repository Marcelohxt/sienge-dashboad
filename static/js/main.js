// Função para animação de números
function animateNumber(element, start, end, duration) {
    let current = start;
    const range = end - start;
    const increment = end > start ? 1 : -1;
    const stepTime = Math.abs(Math.floor(duration / range));
    
    const timer = setInterval(() => {
        current += increment;
        element.textContent = current.toLocaleString();
        if (current == end) {
            clearInterval(timer);
        }
    }, stepTime);
}

// Função para formatar valores monetários
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

// Configuração padrão para gráficos
const chartDefaults = {
    layout: {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: {
            color: '#a0aec0'
        },
        margin: {
            l: 50,
            r: 20,
            t: 30,
            b: 50
        }
    }
};

// Função para criar gráficos com tema escuro
function createDarkThemeChart(element, data, customLayout = {}) {
    const layout = {
        ...chartDefaults.layout,
        ...customLayout,
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: {
            color: '#a0aec0'
        },
        xaxis: {
            gridcolor: 'rgba(255,255,255,0.1)',
            linecolor: 'rgba(255,255,255,0.1)'
        },
        yaxis: {
            gridcolor: 'rgba(255,255,255,0.1)',
            linecolor: 'rgba(255,255,255,0.1)'
        }
    };

    Plotly.newPlot(element, data, layout, {
        responsive: true,
        displayModeBar: false
    });
}

// Inicialização quando o documento estiver pronto
document.addEventListener('DOMContentLoaded', function() {
    // Animar números nos cards
    document.querySelectorAll('[data-animate-number]').forEach(element => {
        const end = parseInt(element.getAttribute('data-animate-number'));
        animateNumber(element, 0, end, 1000);
    });

    // Adicionar efeito hover nos cards
    document.querySelectorAll('.dashboard-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}); 