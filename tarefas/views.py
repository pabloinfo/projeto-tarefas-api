from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Tarefa
from .serializers import TarefaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    @action(detail=True, methods=['patch'])
    def marcar_concluida(self, request, pk=None):
        tarefa = self.get_object()
        tarefa.status = 'concluida'
        tarefa.save()
        serializer = self.get_serializer(tarefa)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pendentes(self, request):
        tarefas = Tarefa.objects.filter(status='pendente')
        serializer = self.get_serializer(tarefas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def concluidas(self, request):
        tarefas = Tarefa.objects.filter(status='concluida')
        serializer = self.get_serializer(tarefas, many=True)
        return Response(serializer.data)