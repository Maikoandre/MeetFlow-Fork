from rest_framework import serializers
from .models import Evento, Inscricao, Presenca, Relatorio, Usuario

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inscricao
        fields = '__all__'

class PresencaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Presenca
        fields = '__all__'

class RelatorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'