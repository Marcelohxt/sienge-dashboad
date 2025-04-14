from django.contrib import admin
from .models import IndicesConstrucao, MaterialPreco, Noticia

@admin.register(IndicesConstrucao)
class IndicesConstrucaoAdmin(admin.ModelAdmin):
    list_display = ('data', 'incc', 'cub', 'variacao_mensal')
    list_filter = ('data',)
    date_hierarchy = 'data'

@admin.register(MaterialPreco)
class MaterialPrecoAdmin(admin.ModelAdmin):
    list_display = ('material', 'preco', 'variacao', 'data_atualizacao')
    list_filter = ('data_atualizacao',)
    search_fields = ('material',)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fonte', 'data_publicacao')
    list_filter = ('fonte', 'data_publicacao')
    search_fields = ('titulo', 'descricao')
    date_hierarchy = 'data_publicacao' 