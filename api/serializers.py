from rest_framework import serializers
from .models import Livro

# [POO - SOLID: Single Responsibility Principle (SRP)]
# Esta classe tem uma responsabilidade única: converter objetos Livro para JSON e vice-versa.
# Ela não lida com banco de dados (Model) nem com requisições HTTP (View).

# [POO - Herança & Reutilização de Código]
# Herdamos de 'ModelSerializer', que já implementa a lógica padrão de serialização.
# Isso evita repetição de código (DRY - Don't Repeat Yourself).
class LivroSerializer(serializers.ModelSerializer):
    # [POO - Metaclasse & Configuração]
    # A classe interna 'Meta' é usada para configurar o comportamento da classe externa.
    # É uma forma de encapsular a configuração.
    class Meta:
        # [POO - Acoplamento]
        # Aqui temos um acoplamento necessário com o modelo 'Livro' para que o serializer saiba o que processar.
        model = Livro
        fields = '__all__'
