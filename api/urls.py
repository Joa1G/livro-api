from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet

# [POO - Delegação]
# O Router é responsável por determinar qual View deve tratar uma requisição.
# Nós delegamos a ele a tarefa de criar as rotas URL automaticamente.
router = DefaultRouter()
router.register(r'livros', LivroViewSet)

# [POO - Modularidade]
# Este arquivo define as rotas específicas deste módulo (app).
# Ele é independente do projeto principal, facilitando a manutenção.
urlpatterns = [
    path('', include(router.urls)),
]
