from django.contrib import admin
from .models import (
    Cliente, 
    Projeto, 
    Fornecedor, 
    Material, 
    Orcamento, 
    SolicitacaoCompra, 
    Cotacao, 
    PedidoCompra
)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'created_at')
    search_fields = ('nome', 'email')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cliente', 'data_inicio', 'data_fim', 'status')
    list_filter = ('status',)
    search_fields = ('nome', 'cliente__nome')

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'email', 'telefone')
    search_fields = ('nome', 'cnpj')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade', 'preco_unitario', 'quantidade_estoque')
    search_fields = ('nome',)

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'valor_total', 'valor_realizado', 'data', 'status')
    list_filter = ('status',)
    search_fields = ('projeto__nome',)

@admin.register(SolicitacaoCompra)
class SolicitacaoCompraAdmin(admin.ModelAdmin):
    list_display = ('numero', 'projeto', 'material', 'quantidade', 'status', 'valor')
    list_filter = ('status',)
    search_fields = ('numero', 'projeto__nome')

@admin.register(Cotacao)
class CotacaoAdmin(admin.ModelAdmin):
    list_display = ('solicitacao', 'fornecedor', 'valor_unitario', 'prazo_entrega', 'status')
    list_filter = ('status',)
    search_fields = ('solicitacao__numero', 'fornecedor__nome')

@admin.register(PedidoCompra)
class PedidoCompraAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cotacao', 'data_pedido', 'data_entrega', 'status', 'valor_total')
    list_filter = ('status',)
    search_fields = ('numero', 'cotacao__solicitacao__numero') 