from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from .services.price_scraper import PriceScraperService
from .forms import MaterialQuoteForm, BulkQuoteForm
import json
import asyncio
from datetime import datetime, timedelta
import random
from django.shortcuts import render
from django.utils import timezone
from .models import IndicesConstrucao, MaterialPreco, Noticia

def dashboard(request):
    # Obtém os índices mais recentes
    try:
        indices = IndicesConstrucao.objects.latest('data')
    except IndicesConstrucao.DoesNotExist:
        # Cria dados iniciais se não existirem
        indices = IndicesConstrucao.objects.create(
            data=timezone.now().date(),
            incc=0.5,
            cub=1500.00,
            variacao_mensal=0.3
        )

    # Obtém as notícias do dia
    hoje = timezone.now().date()
    noticias_hoje = Noticia.objects.filter(data_publicacao__date=hoje).count()
    
    # Obtém as últimas notícias (limitado a 5)
    ultimas_noticias = Noticia.objects.all()[:5]
    
    # Obtém os preços dos materiais
    materiais = MaterialPreco.objects.all()

    # Dados de exemplo para tendências de preços
    materials = ['Cimento', 'Areia', 'Brita', 'Tijolo', 'Aço']
    trends = []
    
    base_date = datetime.now()
    for material in materials:
        price_history = []
        base_price = random.uniform(50, 500)
        
        for i in range(7):
            date = base_date - timedelta(days=i)
            variation = random.uniform(-5, 5)
            price = base_price + variation
            price_history.append({
                'date': date.strftime('%d/%m/%Y'),
                'price': round(price, 2)
            })
        
        trends.append({
            'material': material,
            'history': price_history,
            'current_price': round(price_history[0]['price'], 2),
            'variation': round(((price_history[0]['price'] - price_history[-1]['price']) / price_history[-1]['price']) * 100, 2)
        })

    context = {
        'indices': indices,
        'noticias_hoje': noticias_hoje,
        'ultimas_noticias': ultimas_noticias,
        'materiais': materiais,
        'price_trends': trends
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(context)
    
    return render(request, 'market_intelligence/dashboard.html', context)

class QuoteSearchView(FormView):
    template_name = 'market_intelligence/quote_search.html'
    form_class = MaterialQuoteForm
    success_url = reverse_lazy('market_intelligence:quote_search')

    def form_valid(self, form):
        try:
            material = form.cleaned_data['name']
            scraper = PriceScraperService()
            results = scraper.search_material(material)
            
            if form.cleaned_data.get('generate_report'):
                filename = scraper.generate_report(
                    results, 
                    form.cleaned_data['report_format']
                )
                return JsonResponse({
                    'success': True,
                    'results': results,
                    'report_url': f'/media/results/{filename}'
                })
            
            return JsonResponse({
                'success': True,
                'results': results
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

class BulkQuoteView(FormView):
    template_name = 'market_intelligence/bulk_quote.html'
    form_class = BulkQuoteForm
    success_url = reverse_lazy('market_intelligence:bulk_quote')

    def form_valid(self, form):
        try:
            file = form.cleaned_data['file']
            scraper = PriceScraperService()
            results = scraper.process_bulk_file(file.temporary_file_path())
            filename = scraper.generate_report(
                results.to_dict('records'),
                form.cleaned_data['report_format']
            )
            
            return JsonResponse({
                'success': True,
                'report_url': f'/media/results/{filename}'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }) 