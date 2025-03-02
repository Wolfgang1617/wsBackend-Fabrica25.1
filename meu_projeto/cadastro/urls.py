from django.urls import path, include
from . import views
from .views import UsuarioViewSet, FilmeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'filmes', FilmeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),

]