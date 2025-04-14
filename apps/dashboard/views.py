from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
from django.conf import settings
import requests
import random
from datetime import datetime, timedelta
import json
from decimal import Decimal
=======
>>>>>>> b24c1001d05a217bf2554b6cbfbce4dfc72189de

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

<<<<<<< HEAD
    def get_bcb_data(self):
        """Obtém dados do Banco Central do Brasil"""
        try:
            # INCC - Índice Nacional de Custo da Construção
            incc_url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.192/dados/ultimos/12?formato=json"
            # CUB - Custo Unitário Básico
            cub_url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.170/dados/ultimos/12?formato=json"
            
            incc_response = requests.get(incc_url)
            cub_response = requests.get(cub_url)
            
            incc_data = incc_response.json() if incc_response.ok else []
            cub_data = cub_response.json() if cub_response.ok else []
            
            return {
                'incc_data': incc_data,
                'cub_data': cub_data
            }
        except Exception as e:
            print(f"Erro ao obter dados do BCB: {str(e)}")
            return {'incc_data': [], 'cub_data': []}

    def get_material_prices(self):
        """Simula preços de materiais baseados em tendências reais"""
        materials = {
            'Cimento': {'min': 25, 'max': 35},
            'Areia': {'min': 80, 'max': 120},
            'Brita': {'min': 75, 'max': 95},
            'Tijolo': {'min': 0.75, 'max': 1.20},
            'Aço': {'min': 15, 'max': 25},
        }
        
        prices = {}
        for material, range_price in materials.items():
            base_price = random.uniform(range_price['min'], range_price['max'])
            history = []
            for i in range(6):
                variation = random.uniform(-0.05, 0.05)  # Variação de ±5%
                price = base_price * (1 + variation)
                history.append({
                    'date': (datetime.now() - timedelta(days=30*i)).strftime('%Y-%m'),
                    'price': round(price, 2)
                })
            prices[material] = history
        
        return prices

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Dados do BCB
        bcb_data = self.get_bcb_data()
        
        # Preços de materiais
        material_prices = self.get_material_prices()
        
        # Métricas principais
        context.update({
            'solicitacoes_total': -36810,
            'pedidos_andamento': -36755,
            'cotacoes_abertas': -36742,
            'itens_estoque': -36698,
            'bcb_data': bcb_data,
            'material_prices': material_prices,
            'last_update': datetime.now().strftime('%d/%m/%Y %H:%M')
        })
        
=======
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aqui você pode adicionar dados para o dashboard
>>>>>>> b24c1001d05a217bf2554b6cbfbce4dfc72189de
        return context

class SuprimentosView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/suprimentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
<<<<<<< HEAD
        
        # Simulando dados (em produção, isso viria da API do Sienge)
        solicitacoes = [
            {
                'numero': f'SOL-{random.randint(1000, 9999)}',
                'data': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%d/%m/%Y'),
                'status': random.choice(['Pendente', 'Em Análise', 'Aprovado', 'Rejeitado']),
                'valor': random.uniform(1000, 50000)
            } for _ in range(5)
        ]

        context.update({
            'solicitacoes_pendentes': random.randint(5, 15),
            'pedidos_andamento': random.randint(3, 10),
            'cotacoes_abertas': random.randint(2, 8),
            'total_estoque': random.uniform(100000, 500000),
            'ultimas_solicitacoes': solicitacoes
        })
        
=======
        # Aqui você pode adicionar dados específicos de suprimentos
>>>>>>> b24c1001d05a217bf2554b6cbfbce4dfc72189de
        return context

class OrcamentosView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/orcamentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aqui você pode adicionar dados específicos de orçamentos
        return context 