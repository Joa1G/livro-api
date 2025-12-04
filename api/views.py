from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer

# [POO - Herança Múltipla & Mixins]
# 'ModelViewSet' herda de várias classes (Mixins) que fornecem comportamentos específicos
# (CreateModelMixin, RetrieveModelMixin, etc). Isso é um exemplo de composição de comportamentos via herança.

# [POO - Interface & Contrato]
# O ViewSet define uma interface padrão para interagir com a API (list, create, retrieve, update, destroy).
# Qualquer classe que implemente essa interface pode ser usada pelo Router.
class LivroViewSet(viewsets.ModelViewSet):
    # [POO - Polimorfismo de Subtipo]
    # O ViewSet espera um 'queryset' e um 'serializer_class'.
    # Ao fornecer nossas implementações específicas (Livro e LivroSerializer),
    # o comportamento genérico do ModelViewSet se adapta aos nossos tipos específicos.
    
    # [POO - Atributos de Classe]
    # Definimos o estado inicial da view.
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
