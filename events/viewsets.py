from .models import Evento, Inscricao, Presenca, Relatorio, Usuario
from rest_framework import viewsets, permissions
from .serializers import EventoSerializer, InscricaoSerializer, PresencaSerializer, RelatorioSerializer, UsuarioSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]