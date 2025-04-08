from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import random

class MarketIntelligenceView(LoginRequiredMixin, TemplateView):
    template_name = 'market_intelligence/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Dados de exemplo para visualização inicial
        context['news'] = self.get_sample_news()
        context['indices'] = self.get_sample_indices()
        context['prices'] = self.get_sample_prices()
        
        return context

    def get_sample_news(self):
        # Dados de exemplo para notícias
        return [
            {
                'title': 'Construção Civil registra crescimento no primeiro trimestre',
                'source': 'CBIC',
                'summary': 'O setor da construção civil apresentou crescimento significativo...',
                'published_date': datetime.now() - timedelta(days=1),
                'url': '#'
            },
            {
                'title': 'Novos índices de custos da construção são divulgados',
                'source': 'Sinduscon',
                'summary': 'Os novos índices mostram variação importante nos custos...',
                'published_date': datetime.now() - timedelta(days=2),
                'url': '#'
            },
            {
                'title': 'Inovações tecnológicas impactam o setor da construção',
                'source': 'PiniWeb',
                'summary': 'Novas tecnologias estão transformando o modo de construir...',
                'published_date': datetime.now() - timedelta(days=3),
                'url': '#'
            }
        ]

    def get_sample_indices(self):
        # Dados de exemplo para índices
        return {
            'labels': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
            'datasets': [
                {
                    'name': 'INCC',
                    'data': [0.8, 1.2, 0.9, 1.1, 1.3]
                },
                {
                    'name': 'CUB',
                    'data': [1.1, 0.9, 1.2, 1.0, 1.4]
                }
            ]
        }

    def get_sample_prices(self):
        # Dados de exemplo para preços de materiais
        return [
            {'material': 'Cimento', 'price': 32.50, 'variation': '+2.5%'},
            {'material': 'Aço', 'price': 22.80, 'variation': '-1.2%'},
            {'material': 'Concreto', 'price': 350.00, 'variation': '+0.8%'},
            {'material': 'Tijolos', 'price': 1.20, 'variation': '+1.5%'},
            {'material': 'Areia', 'price': 120.00, 'variation': '+0.3%'}
        ] 