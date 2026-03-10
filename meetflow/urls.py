from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from events.viewsets import EventoViewSet, InscricaoViewSet, PresencaViewSet, RelatorioViewSet, UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'users', UsuarioViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'inscricoes', InscricaoViewSet)
router.register(r'presencas', PresencaViewSet)
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
