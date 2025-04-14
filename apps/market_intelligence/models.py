from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MarketNews(models.Model):
    title = models.CharField(max_length=255)
    source = models.CharField(max_length=100)
    url = models.URLField()
    published_date = models.DateTimeField()
    category = models.CharField(max_length=50)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

class ConstructionIndex(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    reference_date = models.DateField()
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['-reference_date']

class MaterialPrice(models.Model):
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    supplier = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        ordering = ['-last_update']

class MaterialQuote(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome do Material')
    description = models.TextField(blank=True, verbose_name='Descrição')
    unit = models.CharField(max_length=50, verbose_name='Unidade')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class QuoteResult(models.Model):
    material_quote = models.ForeignKey(MaterialQuote, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255, verbose_name='Loja')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    url = models.URLField(verbose_name='Link do Produto')
    store_contact = models.CharField(max_length=255, blank=True, verbose_name='Contato da Loja')
    region = models.CharField(max_length=100, blank=True, verbose_name='Região')
    available = models.BooleanField(default=True, verbose_name='Disponível')
    scraped_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['price']

class BulkQuoteUpload(models.Model):
    file = models.FileField(upload_to='quotes/', verbose_name='Arquivo')
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_file = models.FileField(upload_to='results/', blank=True, null=True)

class IndicesConstrucao(models.Model):
    data = models.DateField(default=timezone.now)
    incc = models.DecimalField(max_digits=5, decimal_places=2)  # INCC do mês
    cub = models.DecimalField(max_digits=8, decimal_places=2)   # CUB/m²
    variacao_mensal = models.DecimalField(max_digits=5, decimal_places=2)  # Variação mensal
    
    class Meta:
        ordering = ['-data']
        verbose_name = 'Índice da Construção'
        verbose_name_plural = 'Índices da Construção'

    def __str__(self):
        return f"Índices de {self.data.strftime('%m/%Y')}"

class MaterialPreco(models.Model):
    material = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    variacao = models.DecimalField(max_digits=5, decimal_places=2)
    data_atualizacao = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['material']
        verbose_name = 'Preço de Material'
        verbose_name_plural = 'Preços de Materiais'

    def __str__(self):
        return f"{self.material} - R$ {self.preco}"

class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    descricao = models.TextField()
    fonte = models.CharField(max_length=100)
    link = models.URLField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    def __str__(self):
        return self.titulo 