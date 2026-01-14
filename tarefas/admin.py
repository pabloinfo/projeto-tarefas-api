from django.contrib import admin
from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'data_criacao', 'data_conclusao')
    list_filter = ('status', 'data_criacao')
    search_fields = ('titulo', 'descricao')
    ordering = ('-data_criacao',)
    readonly_fields = ('data_criacao', 'data_atualizacao')

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'status')
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao', 'data_conclusao'),
            'classes': ('collapse',)
        }),
    )