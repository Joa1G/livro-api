from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet

# ================================
# ARQUIVO: urls.py (da aplicação api)
# ================================
# Este arquivo define as ROTAS (caminhos) para acessar sua API.
# Quando você faz um request, Django procura aqui para saber qual View executar.


# ─────────────────────────────────────────────────────────────────────────────────────────────
# 1. CRIANDO O ROUTER
# ─────────────────────────────────────────────────────────────────────────────────────────────
# DefaultRouter é uma CLASSE do Django REST Framework.
# Instanciamos ela: router = DefaultRouter()
#
# O que faz o Router?
# - DELEGA a tarefa de criar URLs automaticamente
# - Não precisa você criar cada rota manualmente
# - Cria automaticamente: GET, POST, PUT, DELETE, etc.

router = DefaultRouter()

# ─────────────────────────────────────────────────────────────────────────────────────────────
# 2. REGISTRANDO O VIEWSET
# ─────────────────────────────────────────────────────────────────────────────────────────────
# Aqui dizemos ao Router:
# "Quando alguém acessar /livros/, use LivroViewSet"
#
# O Router AUTOMATICAMENTE cria essas rotas:
# - GET    /livros/          → lista todos os livros
# - POST   /livros/          → cria novo livro
# - GET    /livros/{id}/     → pega um livro específico
# - PATCH  /livros/{id}/     → edita um livro
# - DELETE /livros/{id}/     → deleta um livro
#
# Tudo criado AUTOMATICAMENTE sem você escrever cada uma!
# Isso é ABSTRAÇÃO.
#
# router.register(r'livros', LivroViewSet)
# - r'livros' = padrão (regex) de URL
# - LivroViewSet = qual ViewSet usar para esse padrão

router.register(r'livros', LivroViewSet)

# ─────────────────────────────────────────────────────────────────────────────────────────────
# 3. URLPATTERNS - Finalizando as rotas
# ─────────────────────────────────────────────────────────────────────────────────────────────
# urlpatterns é lista de rotas do Django.
# Aqui adicionamos todas as rotas que o Router criou.
#
# DELEGAÇÃO:
# Delegamos ao Router a responsabilidade de criar rotas.
# Apenas incluímos as rotas que ele gerou.
#
# MODULARIDADE:
# Este arquivo é INDEPENDENTE do projeto principal.
# Cada app (aplicação) tem seu próprio urls.py.
# Facilita manutenção: modificar rotas de livros não afeta rotas de autores.
#
# Exemplo de arquitetura:
# livro_api/urls.py → redireciona /api/ para api/urls.py
# api/urls.py → define rotas de livros
#
# Se um dia criar "app" de Autores:
# autor/urls.py → define rotas de autores
# livro_api/urls.py → inclui ambos
# Pronto! Completamente modular e organizado.

urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as rotas do Router
]

# ─────────────────────────────────────────────────────────────────────────────────────────────
# CONCEITOS DE POO PRESENTES NESTE ARQUIVO:
# ─────────────────────────────────────────────────────────────────────────────────────────────
# ✓ CLASSE: DefaultRouter é uma classe (instanciamos ela)
# ✓ OBJETO/INSTÂNCIA: router é um OBJETO (instância de DefaultRouter)
# ✓ DELEGAÇÃO: Router delega criação de rotas para nós
# ✓ POLIMORFISMO: LivroViewSet é um ModelViewSet (pode ser usado onde ModelViewSet é esperado)
# ✓ ABSTRAÇÃO: Router abstrai complexidade de criar URLs
# ✓ MODULARIDADE: Este arquivo é modular (independente do projeto)
# ✓ SOLID - SRP: Responsabilidade única (definir rotas)
# ✓ ENCAPSULAMENTO: Rotas encapsuladas neste arquivo
