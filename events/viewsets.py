from .models import Evento, Inscricao, Presenca, Relatorio, Usuario
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import EventoSerializer, InscricaoSerializer, PresencaSerializer, RelatorioSerializer, UsuarioSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Inscricao.objects.all()
        evento = self.request.query_params.get('evento')
        participante = self.request.query_params.get('participante')
        if evento is not None:
            queryset = queryset.filter(evento_id=evento)
        if participante is not None:
            queryset = queryset.filter(participante_id=participante)
        return queryset

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

    @action(detail=False, methods=['get'])
    def me(self, request):
        try:
            usuario = Usuario.objects.get(user=request.user)
            serializer = self.get_serializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({"detail": "Profile not found"}, status=404)