// Função para animar números
function animateNumber(element, target) {
    const duration = 2000; // 2 segundos
    const start = 0;
    const increment = target / (duration / 16); // 60 FPS
    let current = start;

    const animate = () => {
        current += increment;
        if (current >= target) {
            element.textContent = target.toLocaleString();
            return;
        }
        element.textContent = Math.floor(current).toLocaleString();
        requestAnimationFrame(animate);
    };

    animate();
}

// Função para formatar moeda
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

// Configuração padrão para gráficos com tema escuro
const defaultChartConfig = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'top',
            labels: {
                color: '#e5e7eb'
            }
        }
    },
    scales: {
        x: {
            grid: {
                color: 'rgba(255, 255, 255, 0.1)'
            },
            ticks: {
                color: '#e5e7eb'
            }
        },
        y: {
            grid: {
                color: 'rgba(255, 255, 255, 0.1)'
            },
            ticks: {
                color: '#e5e7eb'
            }
        }
    }
};

// Função para criar gráfico com tema escuro
function createDarkThemeChart(ctx, data) {
    return new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            ...defaultChartConfig,
            interaction: {
                intersect: false,
                mode: 'index'
            },
            plugins: {
                ...defaultChartConfig.plugins,
                tooltip: {
                    enabled: true,
                    mode: 'index',
                    intersect: false,
                    callbacks: {
                        label: function(context) {
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            label += context.parsed.y.toFixed(2);
                            return label;
                        }
                    }
                }
            }
        }
    });
}

// Adicionar efeito hover nos cards do dashboard
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.metric-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Inicializar tooltips do Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}); 
