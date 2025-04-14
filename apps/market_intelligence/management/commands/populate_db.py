from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.market_intelligence.models import IndicesConstrucao, MaterialPreco, Noticia

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais'

    def handle(self, *args, **kwargs):
        # Criar índices de construção
        if not IndicesConstrucao.objects.exists():
            IndicesConstrucao.objects.create(
                data=timezone.now().date(),
                incc=0.5,
                cub=1500.00,
                variacao_mensal=0.3
            )
            self.stdout.write(self.style.SUCCESS('Índices de construção criados com sucesso!'))

        # Criar preços de materiais
        if not MaterialPreco.objects.exists():
            materiais = [
                {'material': 'Cimento', 'preco': 35.90, 'variacao': 0.5},
                {'material': 'Areia', 'preco': 120.00, 'variacao': 0.2},
                {'material': 'Brita', 'preco': 150.00, 'variacao': 0.3},
                {'material': 'Tijolo', 'preco': 1.20, 'variacao': 0.1},
                {'material': 'Aço', 'preco': 4500.00, 'variacao': 1.2},
            ]
            for material in materiais:
                MaterialPreco.objects.create(**material)
            self.stdout.write(self.style.SUCCESS('Preços de materiais criados com sucesso!'))

        # Criar notícias
        if not Noticia.objects.exists():
            noticias = [
                {
                    'titulo': 'Aumento no preço do aço impacta construção civil',
                    'descricao': 'Preços do aço registram aumento de 15% no último mês devido à demanda global.',
                    'fonte': 'Construção Mercado',
                    'link': 'https://exemplo.com/noticia1'
                },
                {
                    'titulo': 'Novos materiais sustentáveis ganham mercado',
                    'descricao': 'Materiais eco-friendly apresentam crescimento de 25% nas vendas do setor.',
                    'fonte': 'Revista Construir',
                    'link': 'https://exemplo.com/noticia2'
                },
                {
                    'titulo': 'Cimento tem queda de preço em março',
                    'descricao': 'Preço do cimento registra queda de 5% devido ao aumento da oferta.',
                    'fonte': 'Portal Construção',
                    'link': 'https://exemplo.com/noticia3'
                }
            ]
            for noticia in noticias:
                Noticia.objects.create(**noticia)
            self.stdout.write(self.style.SUCCESS('Notícias criadas com sucesso!')) 