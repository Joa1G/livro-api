from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer

# ================================
# ARQUIVO: views.py
# ================================
# Este arquivo define AÇÕES que sua API pode fazer.
# É aqui que acontecem operações:
# - Listar livros
# - Criar livro
# - Buscar um livro
# - Editar livro
# - Deletar livro


class LivroViewSet(viewsets.ModelViewSet):
    """
    ╔════════════════════════════════════════════════════════════════════════════════════════╗
    ║                        CONCEITOS DE POO PRESENTES                      ║
    ╚════════════════════════════════════════════════════════════════════════════════════════╝
    """
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 1. CLASSE
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # "LivroViewSet" é uma CLASSE.
    # É um molde para lidar com requisições HTTP de livros.
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 2. HERANÇA MÚLTIPLA & MIXINS
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # LivroViewSet herda de viewsets.ModelViewSet
    #
    # Herança MÚLTIPLA? O que é isso?
    # Normalmente uma classe herda de UMA superclasse.
    # Herança múltipla = uma classe herda de VÁRIAS superclasses!
    #
    # ModelViewSet não é apenas uma classe, é na verdade várias classes
    # combinadas (chamadas MIXINS).
    #
    # MIXIN = é uma mini-classe que fornece UMA funcionalidade específica.
    # ModelViewSet combina:
    #   - CreateModelMixin → fornece método .create() (POST)
    #   - RetrieveModelMixin → fornece método .retrieve() (GET um)
    #   - UpdateModelMixin → fornece método .update() (PUT)
    #   - DestroyModelMixin → fornece método .destroy() (DELETE)
    #   - ListModelMixin → fornece método .list() (GET todos)
    #
    # LivroViewSet HERDA de tudo isso!
    # Tem TODOS esses métodos automaticamente.
    #
    # É como herdar de várias famílias:
    # - Da família do Criar, você herda o jeito de criar
    # - Da família do Buscar, você herda o jeito de buscar
    # - Da família do Editar, você herda o jeito de editar
    # - Da família do Deletar, você herda o jeito de deletar
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 3. INTERFACE & CONTRATO
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # Uma INTERFACE é como um CONTRATO.
    # Um contrato diz: "Você DEVE ter esses métodos"
    #
    # ModelViewSet define uma interface:
    # "Qualquer ViewSet deve ter: list, create, retrieve, update, destroy"
    #
    # LivroViewSet IMPLEMENTA esse contrato.
    # Herda os métodos e os implementa.
    #
    # Por quê interface é importante?
    # - O Django sabe que LivroViewSet tem esses métodos
    # - O Django sabe como tratar qualquer ViewSet que implemente essa interface
    # - Qualquer novo ViewSet que você criar será tratado igual
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 4. ATRIBUTOS DE CLASSE
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # Atributos = dados que a classe tem.
    # ATRIBUTOS DE CLASSE = são compartilhados por toda a classe.
    #
    # Pense assim:
    # - Se cada OBJETO tivesse seu queryset, seria diferente para cada livro
    # - Como queryset é DE CLASSE, é igual para todos os livros
    # - Todos acessam os mesmos livros do banco
    
    # Significa: "Quando alguém pedir livros, use todos os livros do banco"
    # Livro.objects.all() = "Pega TODOS os livros da classe Livro"
    queryset = Livro.objects.all()
    
    # Significa: "Use o LivroSerializer para converter dados"
    # Assim Django sabe como transformar Livro ↔ JSON
    serializer_class = LivroSerializer
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 5. POLIMORFISMO DE SUBTIPO (Polymorphism by Subtyping)
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # POLIMORFISMO DE SUBTIPO = usar subclasses no lugar de superclasses.
    #
    # ModelViewSet é a SUPERCLASSE (genérica).
    # LivroViewSet é a SUBCLASSE (específica).
    #
    # O Django escreve código assim:
    # "Qualquer ModelViewSet pode ser usado aqui"
    #
    # Você passa LivroViewSet (que É UM ModelViewSet).
    # O Django aceita porque:
    # LivroViewSet É UM ModelViewSet (herança)
    # LivroViewSet É UM subtipo de ModelViewSet
    #
    # Django não precisa saber que é LivroViewSet especificamente.
    # Ele trata como ModelViewSet e funciona!
    #
    # Por quê?
    # - ModelViewSet define um CONTRATO (interface)
    # - LivroViewSet segue esse CONTRATO
    # - Qualquer classe que siga o contrato funciona
    #
    # Exemplo:
    # - AutorViewSet também herda de ModelViewSet
    # - Django trata AutorViewSet e LivroViewSet igual
    # - Ambos são subtipos de ModelViewSet
    # - POLIMORFISMO = mesma ação (listar, criar) funciona em tipos diferentes
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 6. DELEGAÇÃO
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # DELEGAÇÃO = passar responsabilidade para outro objeto.
    #
    # LivroViewSet DELEGA tarefas:
    # - Delegação ao Serializer: "Convert dados pra mim"
    # - Delegação ao Model: "Salve dados no banco pra mim"
    # - Delegação ao Router: "Crie as rotas pra mim"
    #
    # Não faz tudo sozinho, passa responsabilidades!
    # Isso é BOAS PRÁTICAS (divisão de responsabilidades).
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 7. ABSTRAÇÃO
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # ABSTRAÇÃO = esconder complexidade.
    #
    # ModelViewSet ABSTRAI complexidade:
    # - Você não escreve como fazer GET manual
    # - Você não escreve como validar dados manual
    # - Você não escreve como salvar manual
    #
    # Apenas define queryset e serializer_class.
    # ModelViewSet cuida do resto!
    # Isso é ABSTRAÇÃO.
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 8. SOLID: Single Responsibility Principle (SRP)
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # LivroViewSet tem responsabilidade:
    # "Coordenar requisições HTTP de livros"
    #
    # O que ela NÃO faz:
    # - Não valida dados (responsabilidade do Serializer)
    # - Não salva no banco (responsabilidade do Model)
    # - Não define URLs (responsabilidade do urls.py)
    #
    # Cada classe ESPECIALIZADA em uma coisa!
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # RESUMO DO QUE TEMOS AQUI:
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # ✓ CLASSE: LivroViewSet (molde para ações HTTP)
    # ✓ HERANÇA MÚLTIPLA: Herda de ModelViewSet (que herda de vários Mixins)
    # ✓ SUPERCLASSE: viewsets.ModelViewSet
    # ✓ SUBCLASSE: LivroViewSet
    # ✓ INTERFACE/CONTRATO: Implementa interface do ModelViewSet
    # ✓ ATRIBUTOS DE CLASSE: queryset e serializer_class
    # ✓ POLIMORFISMO DE SUBTIPO: LivroViewSet é um ModelViewSet
    # ✓ DELEGAÇÃO: Passa responsabilidades para Serializer e Model
    # ✓ ABSTRAÇÃO: Esconde complexidade de HTTP
    # ✓ SOLID - SRP: Responsabilidade única (coordenar requisições)
