# 🎯 EXEMPLOS PRÁTICOS DE POO NO SEU CÓDIGO

## 1. CLASSE E OBJETO/INSTÂNCIA

### O que é CLASSE?
Uma CLASSE é um MOLDE. Um OBJETO é uma cópia pronta do molde.

```python
# ═══════════════════════════════════════════════════════════
# CLASSE = O molde (não é real ainda)
# ═══════════════════════════════════════════════════════════

class Livro(models.Model):  # ← CLASSE Livro
    titulo = models.CharField(max_length=255)
    dataPublicacao = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)


# ═══════════════════════════════════════════════════════════
# OBJETO/INSTÂNCIA = A cópia real pronta
# ═══════════════════════════════════════════════════════════

# Criando OBJETOS/INSTÂNCIAS a partir da CLASSE Livro:

livro1 = Livro(
    titulo="O Senhor dos Anéis",
    dataPublicacao="29/07/1954",
    edicao="1"
)
# livro1 é uma INSTÂNCIA (um objeto real de Livro)

livro2 = Livro(
    titulo="Harry Potter",
    dataPublicacao="26/06/1997",
    edicao="1"
)
# livro2 é outra INSTÂNCIA (outro objeto real de Livro)

# Mesmo molde (classe), mas OBJETOS DIFERENTES!
print(livro1.titulo)  # "O Senhor dos Anéis"
print(livro2.titulo)  # "Harry Potter"
```

---

## 2. ATRIBUTOS

### O que são ATRIBUTOS?
ATRIBUTOS são as CARACTERÍSTICAS/DADOS de um objeto.

```python
class Livro(models.Model):
    # Esses são ATRIBUTOS
    titulo = models.CharField(max_length=255)           # ATRIBUTO
    dataPublicacao = models.CharField(max_length=50)    # ATRIBUTO
    edicao = models.CharField(max_length=50)            # ATRIBUTO


# ACESSANDO ATRIBUTOS:
livro = Livro.objects.get(id=1)

print(livro.titulo)           # Acessar ATRIBUTO
print(livro.dataPublicacao)   # Acessar ATRIBUTO
print(livro.edicao)           # Acessar ATRIBUTO


# MODIFICANDO ATRIBUTOS:
livro.titulo = "Novo Título"  # Mudar ATRIBUTO
livro.save()                  # Salvar mudanças no banco
```

---

## 3. MÉTODOS

### O que são MÉTODOS?
MÉTODOS são as AÇÕES que um objeto pode fazer.

```python
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    dataPublicacao = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)
    
    # MÉTODO - Uma ação que Livro pode fazer
    def __str__(self):
        return self.titulo


# USANDO MÉTODOS:
livro = Livro.objects.get(id=1)

# Chamando o método __str__
print(str(livro))      # Chama __str__() automaticamente
# Output: "Nome do Livro"

# Django também usa __str__ em vários lugares
# Por exemplo, no admin do Django mostra o título, não "<Livro object (1)>"
```

---

## 4. HERANÇA E SUPERCLASSE/SUBCLASSE

### O que é HERANÇA?
HERANÇA = receber todos os poderes de uma classe PAI.

```python
# ═══════════════════════════════════════════════════════════
# models.Model é a SUPERCLASSE (PAI)
# Livro é a SUBCLASSE (FILHO)
# ═══════════════════════════════════════════════════════════

class Livro(models.Model):  # ← Livro HERDA de models.Model
    titulo = models.CharField(max_length=255)
    dataPublicacao = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)


# Livro HERDA automaticamente esses MÉTODOS de models.Model:

livro = Livro()

# Esses métodos vêm de models.Model (SUPERCLASSE):
livro.save()              # Herança: salvar no banco
livro.delete()            # Herança: deletar do banco
Livro.objects.all()       # Herança: pegar todos
Livro.objects.filter()    # Herança: filtrar
Livro.objects.get(id=1)   # Herança: pegar um específico


# Se tivesse escrito tudo manualmente:
class LivroSemHeranca:
    def save(self):
        # Código complicado para salvar...
        pass
    def delete(self):
        # Código complicado para deletar...
        pass
    # ... centenas de linhas de código ...

# COM HERANÇA = 3 linhas!
# SEM HERANÇA = 300 linhas! 😅
```

---

## 5. POLIMORFISMO, SOBREPOSIÇÃO E SOBRECARGA

### O que é POLIMORFISMO?
"Muitas formas" - mesma ação, comportamentos DIFERENTES.

### O que é SOBREPOSIÇÃO (Overriding)?
Mudar o comportamento de um método do PAI.

### O que é SOBRECARGA (Overloading)?
Mesmo método com DIFERENTES PARÂMETROS

**⚠️ IMPORTANTE:** Existem **3 TIPOS de Polimorfismo**:
1. **SOBREPOSIÇÃO** - Classe filha muda método do pai
2. **SOBRECARGA** - Mesmo método com diferentes parâmetros
3. **SUBTIPO** - Subclasse substitui superclasse

**Veja o arquivo `POLIMORFISMO_3_TIPOS.md` para detalhes completos!**

```python
# ═══════════════════════════════════════════════════════════
# 1. SOBREPOSIÇÃO (Overriding)
# ═══════════════════════════════════════════════════════════

# SUPERCLASSE (models.Model)
# models.Model tem __str__ que retorna:
# "<Livro object (1)>"  ← Não é legível!


# SUBCLASSE (Livro) - SOBRESCREVENDO __str__

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    
    def __str__(self):  # ← SOBREPOSIÇÃO (mesmo nome do pai)
        return self.titulo  # ← Comportamento DIFERENTE do pai!


# RESULTADO:
livro = Livro.objects.get(id=1)
print(str(livro))  # Antes: "<Livro object (1)>"
                   # Depois: "Nome do Livro"  ← Muito melhor!


# ═══════════════════════════════════════════════════════════
# 2. SOBRECARGA (Overloading)
# ═══════════════════════════════════════════════════════════

# Mesmo método, DIFERENTES PARÂMETROS = COMPORTAMENTOS DIFERENTES

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    dataPublicacao = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)
    
    def descricao(self, incluir_edicao=False):
        """SOBRECARGA - Mesmo método, comportamentos DIFERENTES"""
        base = f"{self.titulo} ({self.dataPublicacao})"
        
        if incluir_edicao:
            return f"{base} - Edição {self.edicao}"
        
        return base


# USANDO COM DIFERENTES PARÂMETROS:
livro = Livro.objects.get(id=1)

# SEM parâmetro:
print(livro.descricao())
# Output: "O Senhor dos Anéis (29/07/1954)"

# COM parâmetro:
print(livro.descricao(incluir_edicao=True))
# Output: "O Senhor dos Anéis (29/07/1954) - Edição 1"

# MESMO MÉTODO, COMPORTAMENTOS DIFERENTES!


class Livro(models.Model):
    def formatar_info(self, formato="curto"):
        """
        OUTRO EXEMPLO DE SOBRECARGA
        Mesmo método, DIFERENTES FORMATOS
        """
        if formato == "curto":
            return f"Livro: {self.titulo}"
        
        elif formato == "longo":
            return f"Livro: {self.titulo} | Data: {self.dataPublicacao} | Edição: {self.edicao}"
        
        elif formato == "json":
            import json
            return json.dumps({
                "titulo": self.titulo,
                "dataPublicacao": self.dataPublicacao,
                "edicao": self.edicao
            })


# USANDO COM DIFERENTES FORMATOS:
livro = Livro.objects.get(id=1)

# Formato curto:
print(livro.formatar_info())
# "Livro: O Senhor dos Anéis"

# Formato longo:
print(livro.formatar_info(formato="longo"))
# "Livro: O Senhor dos Anéis | Data: 29/07/1954 | Edição: 1"

# Formato JSON:
print(livro.formatar_info(formato="json"))
# {"titulo": "O Senhor dos Anéis", "dataPublicacao": "29/07/1954", "edicao": "1"}

# MESMO MÉTODO, 3 COMPORTAMENTOS DIFERENTES!


# ═══════════════════════════════════════════════════════════
# 3. SUBTIPO (Subtyping)
# ═══════════════════════════════════════════════════════════

# Subclasse pode ser usada ONDE a superclasse é esperada

class LivroViewSet(viewsets.ModelViewSet):
    # LivroViewSet É UM ModelViewSet
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


# Django escreve código assim:
def processar_viewset(viewset):
    """Aceita QUALQUER ModelViewSet"""
    return viewset.list()  # Chama método de ModelViewSet


# Pode passar LivroViewSet:
livro_viewset = LivroViewSet()
processar_viewset(livro_viewset)  # ✓ Funciona!
# Porque LivroViewSet É UM ModelViewSet


# ═══════════════════════════════════════════════════════════
# POLIMORFISMO EM AÇÃO
# ═══════════════════════════════════════════════════════════

# Imagine outros modelos:

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):  # ← Mesmo método, comportamento DIFERENTE!
        return self.nome


class Usuario(models.Model):
    email = models.CharField(max_length=255)
    
    def __str__(self):  # ← Mesmo método, comportamento DIFERENTE!
        return self.email


# Mesmo método __str__ em diferentes classes:
livro = Livro.objects.get(id=1)
autor = Autor.objects.get(id=1)
usuario = Usuario.objects.get(id=1)

print(str(livro))      # Livro: retorna título
print(str(autor))      # Autor: retorna nome
print(str(usuario))    # Usuário: retorna email

# POLIMORFISMO = mesma ação (__str__) com resultados DIFERENTES!
```

---

## 6. ENCAPSULAMENTO

### O que é ENCAPSULAMENTO?
Proteger dados DENTRO da classe.

```python
# ═══════════════════════════════════════════════════════════
# DADOS PROTEGIDOS (ENCAPSULAMENTO)
# ═══════════════════════════════════════════════════════════

class Livro(models.Model):
    # Os atributos estão PROTEGIDOS dentro da classe
    titulo = models.CharField(max_length=255)  # Protegido!
    dataPublicacao = models.CharField(max_length=50)  # Protegido!
    edicao = models.CharField(max_length=50)  # Protegido!


# FORMA CORRETA - através do objeto:
livro = Livro.objects.get(id=1)
print(livro.titulo)  # ✓ Correto - acesso controlado


# FORMA ERRADA - diretamente no banco:
import sqlite3
db = sqlite3.connect('db.sqlite3')
cursor = db.cursor()
cursor.execute("SELECT * FROM api_livro")  # ✗ Errado!
# Isso quebra a proteção e pode causar inconsistências


# ═══════════════════════════════════════════════════════════
# POR QUÊ ENCAPSULAMENTO?
# ═══════════════════════════════════════════════════════════

# 1. SEGURANÇA - dados não podem ser acessados diretamente
# 2. CONSISTÊNCIA - Django valida antes de salvar
# 3. FLEXIBILIDADE - se mudar de banco, o código não quebra
# 4. MANUTENIBILIDADE - fácil debugar porque tudo passa por um ponto
```

---

## 7. ABSTRAÇÃO

### O que é ABSTRAÇÃO?
Esconder a complexidade, mostrar apenas o necessário.

```python
# ═══════════════════════════════════════════════════════════
# SEM ABSTRAÇÃO - Complexo demais! 😫
# ═══════════════════════════════════════════════════════════

import sqlite3
db = sqlite3.connect('db.sqlite3')
cursor = db.cursor()

# Fazer um simples GET? Upa 10 linhas de SQL complexo!
sql = """
SELECT id, titulo, dataPublicacao, edicao 
FROM api_livro 
WHERE id = ? 
LIMIT 1
"""
cursor.execute(sql, (1,))
resultado = cursor.fetchone()
livro_data = {
    'id': resultado[0],
    'titulo': resultado[1],
    'dataPublicacao': resultado[2],
    'edicao': resultado[3]
}
# Cansativo e propenso a erros! 😅


# ═══════════════════════════════════════════════════════════
# COM ABSTRAÇÃO - Simples! 😄
# ═══════════════════════════════════════════════════════════

# Django ABSTRAI a complexidade de SQL:
livro = Livro.objects.get(id=1)  # ← Uma linha!
# Fim!

# Django cuidou de tudo:
# - Conectar ao banco
# - Escrever SQL certo
# - Buscar dados
# - Converter para Python
# - Retornar objeto


# ═══════════════════════════════════════════════════════════
# MAIS EXEMPLOS DE ABSTRAÇÃO
# ═══════════════════════════════════════════════════════════

# Listar todos:
livros = Livro.objects.all()  # ← Uma linha!

# Filtrar:
livros = Livro.objects.filter(titulo="Python")  # ← Uma linha!

# Deletar:
livro.delete()  # ← Uma linha!

# Tudo é SIMPLES porque Django ABSTRAI a complexidade!
```

---

## 8. DELEGAÇÃO

### O que é DELEGAÇÃO?
Passar a responsabilidade para alguém que sabe fazer.

```python
# ═══════════════════════════════════════════════════════════
# views.py (LivroViewSet) - NÃO faz tudo sozinho!
# ═══════════════════════════════════════════════════════════

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    
    # Quando recebe um POST (criar novo livro):
    # O ViewSet NÃO faz tudo sozinho
    # Ele DELEGA:
    #   - "Serializer, converta JSON para Livro pra mim"
    #   - "Model, salve no banco pra mim"
    #   - "Serializer, converta Livro para JSON pra mim"


# ═══════════════════════════════════════════════════════════
# Sem delegação seria assim:
# ═══════════════════════════════════════════════════════════

class LivroViewSetSemDelegacao:
    def criar_livro(self, dados_json):
        # Eu mesmo converto JSON:
        livro_dict = json.loads(dados_json)  # 😫 Eu faço
        
        # Eu mesmo valido:
        if not livro_dict.get('titulo'):  # 😫 Eu faço
            raise ValueError("Título obrigatório")
        
        # Eu mesmo crio objeto:
        livro = Livro(  # 😫 Eu faço
            titulo=livro_dict['titulo'],
            dataPublicacao=livro_dict['dataPublicacao'],
            edicao=livro_dict['edicao']
        )
        
        # Eu mesmo salvo:
        livro.save()  # 😫 Eu faço
        
        # Eu mesmo converto volta para JSON:
        resultado = {  # 😫 Eu faço
            'id': livro.id,
            'titulo': livro.titulo,
            'dataPublicacao': livro.dataPublicacao,
            'edicao': livro.edicao
        }
        return json.dumps(resultado)


# COM DELEGAÇÃO = 3 linhas!
# SEM DELEGAÇÃO = 30 linhas! 😱
```

---

## 9. INTERFACE / CONTRATO

### O que é INTERFACE / CONTRATO?
Uma promessa de quais métodos uma classe TEM.

```python
# ═══════════════════════════════════════════════════════════
# ModelViewSet define um CONTRATO (interface)
# ═══════════════════════════════════════════════════════════

# "Se você herdar de ModelViewSet, você DEVE ter esses métodos:"
# - list()       → Listar todos
# - create()     → Criar novo
# - retrieve()   → Pegar um
# - update()     → Editar
# - destroy()    → Deletar


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    # ↑ LivroViewSet IMPLEMENTA o contrato de ModelViewSet
    # ↑ Tem TODOS os métodos prometidos


# ═══════════════════════════════════════════════════════════
# POR QUÊ INTERFACE / CONTRATO?
# ═══════════════════════════════════════════════════════════

# Django sabe que qualquer ViewSet tem esses métodos:
# Django pode tratar todos igual!
# Django não precisa saber que é LivroViewSet especificamente.


# Exemplo:

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    # AutorViewSet também implementa o mesmo contrato

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # UsuarioViewSet também implementa o mesmo contrato


# Django trata todos IGUAL porque implementam o CONTRATO!
# ISSO É INTERFACE / CONTRATO em ação!
```

---

## 10. HERANÇA MÚLTIPLA / MIXINS

### O que é HERANÇA MÚLTIPLA?
Uma classe herda de VÁRIAS superclasses.

### O que é MIXIN?
Uma mini-classe que fornece UMA funcionalidade específica.

```python
# ═══════════════════════════════════════════════════════════
# ModelViewSet é na verdade VÁRIOS classes combinadas
# ═══════════════════════════════════════════════════════════

# Internamente, ModelViewSet é algo assim:

class CreateModelMixin:
    """Fornece método create() para criar (POST)"""
    def create(self, request):
        # Código para criar...
        pass


class RetrieveModelMixin:
    """Fornece método retrieve() para buscar um (GET /id)"""
    def retrieve(self, request, pk=None):
        # Código para buscar um...
        pass


class UpdateModelMixin:
    """Fornece método update() para editar (PUT)"""
    def update(self, request, pk=None):
        # Código para editar...
        pass


class DestroyModelMixin:
    """Fornece método destroy() para deletar (DELETE)"""
    def destroy(self, request, pk=None):
        # Código para deletar...
        pass


class ListModelMixin:
    """Fornece método list() para listar (GET)"""
    def list(self, request):
        # Código para listar...
        pass


# ModelViewSet combina TODOS:
class ModelViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    ViewSetBase
):
    """HERANÇA MÚLTIPLA - herda de vários Mixins"""
    pass


# ═══════════════════════════════════════════════════════════
# LivroViewSet HERDA de tudo isso!
# ═══════════════════════════════════════════════════════════

class LivroViewSet(viewsets.ModelViewSet):
    # Automaticamente tem TODOS esses métodos:
    # - create() - de CreateModelMixin
    # - retrieve() - de RetrieveModelMixin
    # - update() - de UpdateModelMixin
    # - destroy() - de DestroyModelMixin
    # - list() - de ListModelMixin


# ═══════════════════════════════════════════════════════════
# POR QUÊ HERANÇA MÚLTIPLA / MIXINS?
# ═══════════════════════════════════════════════════════════

# Em vez de escrever 500 linhas de código:
# Você apenas herda e tem TUDO!

# É como herdar de VÁRIOS pais e receber características de todos!
```

---

## 11. SOLID - SRP (Single Responsibility Principle)

### O que é SOLID - SRP?
Cada classe TEM UMA responsabilidade só!

```python
# ═══════════════════════════════════════════════════════════
# ✓ CORRETO - Cada classe com UMA responsabilidade
# ═══════════════════════════════════════════════════════════

# models.py - Responsabilidade: Definir estrutura de dados
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    dataPublicacao = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)


# serializers.py - Responsabilidade: Converter JSON ↔ Livro
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


# views.py - Responsabilidade: Coordenar requisições HTTP
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


# urls.py - Responsabilidade: Definir rotas
router = DefaultRouter()
router.register(r'livros', LivroViewSet)


# ═══════════════════════════════════════════════════════════
# ✗ ERRADO - Misturar responsabilidades
# ═══════════════════════════════════════════════════════════

class LivroTudo:
    """ERRADO! Faz TUDO sozinho"""
    
    def __init__(self):
        # Responsabilidade 1: Dados
        self.titulo = ""
        self.dataPublicacao = ""
        self.edicao = ""
    
    def converter_para_json(self):
        # Responsabilidade 2: Conversão
        return json.dumps({...})
    
    def validar(self):
        # Responsabilidade 3: Validação
        if not self.titulo:
            raise ValueError(...)
    
    def tratar_requisicao_http(self, request):
        # Responsabilidade 4: HTTP
        if request.method == 'POST':
            # ...
            pass
    
    def gerar_rota_url(self):
        # Responsabilidade 5: URL
        return "/livros/"
    
    # Isso é uma BAGUNÇA! 😫


# ═══════════════════════════════════════════════════════════
# POR QUÊ SRP?
# ═══════════════════════════════════════════════════════════

# 1. FÁCIL DE ENTENDER - cada arquivo faz uma coisa
# 2. FÁCIL DE DEBUGAR - sabe exatamente onde procurar o erro
# 3. FÁCIL DE TESTAR - testa cada responsabilidade separadamente
# 4. FÁCIL DE MANTER - modificar uma coisa não quebra outra
# 5. REUTILIZAÇÃO - pode usar classes em outros projetos
```

---

## 🎓 CONCLUSÃO

Você viu que seu código usa MUITOS conceitos de POO de forma ELEGANTE:

1. ✓ CLASSE - Livro, LivroSerializer, LivroViewSet
2. ✓ OBJETO - router
3. ✓ ATRIBUTOS - titulo, dataPublicacao, edicao
4. ✓ MÉTODOS - __str__(), create(), list(), etc
5. ✓ HERANÇA - de Model, ModelSerializer, ModelViewSet
6. ✓ SUPERCLASSE/SUBCLASSE - Model/Livro, ModelSerializer/LivroSerializer
7. ✓ POLIMORFISMO - __str__() em diferentes classes
8. ✓ SOBREPOSIÇÃO - __str__() sobrescreve comportamento do pai
9. ✓ ENCAPSULAMENTO - atributos protegidos
10. ✓ ABSTRAÇÃO - CharField, ModelViewSet, Router
11. ✓ COESÃO - cada arquivo cuida de uma coisa
12. ✓ ACOPLAMENTO - dependências necessárias e razoáveis
13. ✓ DELEGAÇÃO - ViewSet delega para Serializer e Model
14. ✓ INTERFACE - ModelViewSet define contrato
15. ✓ HERANÇA MÚLTIPLA - ModelViewSet herda de vários Mixins
16. ✓ SOLID - SRP - cada classe tem uma responsabilidade

**Seu código está MUITO bem escrito!** 🎉
