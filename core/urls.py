from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'mensagem': 'API de Tarefas está funcionando!',
        'endpoints': {
            'admin': '/admin/',
            'api_tarefas': '/api/tarefas/',
            'tarefas_pendentes': '/api/tarefas/pendentes/',
            'tarefas_concluidas': '/api/tarefas/concluidas/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tarefas.urls')),
    path('', home, name='home'),
]

# Customizando admin
admin.site.site_header = 'Administração do Sistema de Tarefas'
admin.site.site_title = 'Sistema de Tarefas'
admin.site.index_title = 'Bem-vindo ao Sistema de Tarefas'