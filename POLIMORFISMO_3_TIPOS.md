# 🎭 OS 3 TIPOS DE POLIMORFISMO

## Polimorfismo = "Muitas Formas"

Polimorfismo significa que a MESMA AÇÃO pode ter COMPORTAMENTOS DIFERENTES dependendo do contexto.

Existem **3 tipos principais** de polimorfismo:

---

## 1️⃣ SOBREPOSIÇÃO (Overriding) - POLIMORFISMO POR HERANÇA

### O que é?
A SUBCLASSE **muda completamente** o comportamento de um método da SUPERCLASSE.

### Características:
- ✓ Mesmo nome de método na classe PAI e na classe FILHA
- ✓ Comportamento DIFERENTE (completamente novo)
- ✓ Relacionado com HERANÇA
- ✓ Requer que a classe PAI tenha o método

### Como Identificar:
```
Classe PAI: def metodo() → retorna X
Classe FILHA: def metodo() → retorna Y (DIFERENTE!)
```

### Exemplo NO SEU CÓDIGO:

```python
# ═══════════════════════════════════════════════════════════
# SUPERCLASSE (models.Model)
# ═══════════════════════════════════════════════════════════

# models.Model tem __str__ que retorna:
# "<Livro object (1)>"  ← Genérico e não legível!


# ═══════════════════════════════════════════════════════════
# SUBCLASSE (Livro) - SOBREPÕE __str__
# ═══════════════════════════════════════════════════════════

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    
    def __str__(self):  # ← MESMO NOME DO PAI
        return self.titulo  # ← COMPORTAMENTO COMPLETAMENTE DIFERENTE!


# ═══════════════════════════════════════════════════════════
# RESULTADO DA SOBREPOSIÇÃO
# ═══════════════════════════════════════════════════════════

livro = Livro.objects.get(id=1)

# ANTES (sem sobreposição):
# print(str(livro))  → "<Livro object (1)>"

# DEPOIS (com sobreposição):
# print(str(livro))  → "O Senhor dos Anéis"
```

### Outros Exemplos:

```python
# ═══════════════════════════════════════════════════════════
# Imagine uma classe Autor
# ═══════════════════════════════════════════════════════════

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):  # ← Mesmo método, comportamento DIFERENTE!
        return self.nome  # ← Retorna nome do autor


# ═══════════════════════════════════════════════════════════
# E uma classe Usuario
# ═══════════════════════════════════════════════════════════

class Usuario(models.Model):
    email = models.CharField(max_length=255)
    
    def __str__(self):  # ← Mesmo método, comportamento DIFERENTE!
        return self.email  # ← Retorna email do usuário


# ═══════════════════════════════════════════════════════════
# POLIMORFISMO EM AÇÃO
# ═══════════════════════════════════════════════════════════

livro = Livro.objects.get(id=1)
autor = Autor.objects.get(id=1)
usuario = Usuario.objects.get(id=1)

print(str(livro))      # "O Senhor dos Anéis"   ← Comportamento do Livro
print(str(autor))      # "J.R.R. Tolkien"       ← Comportamento do Autor
print(str(usuario))    # "joao@email.com"       ← Comportamento do Usuário

# MESMO MÉTODO __str__, 3 COMPORTAMENTOS DIFERENTES!
# ISSO É POLIMORFISMO POR SOBREPOSIÇÃO!
```

---

## 2️⃣ SOBRECARGA (Overloading) - POLIMORFISMO POR PARÂMETROS

### O que é?
A MESMA FUNÇÃO/MÉTODO pode fazer **COISAS DIFERENTES** dependendo dos **PARÂMETROS** recebidos.

### Características:
- ✓ Mesmo nome de método
- ✓ DIFERENTES PARÂMETROS (quantidade ou tipo)
- ✓ Comportamento DIFERENTE baseado nos parâmetros
- ✓ NÃO relacionado com herança

### Como Identificar:
```
def metodo()             → Caso 1
def metodo(param1)       → Caso 2
def metodo(param1, param2) → Caso 3

Mesma função, DIFERENTES PARÂMETROS = DIFERENTES COMPORTAMENTOS
```

### ⚠️ IMPORTANTE - Python vs Java/C++

**Java/C++ suportam sobrecarga real:**
```java
// Java - Verdadeira Sobrecarga
void imprimir(int x) { ... }
void imprimir(String x) { ... }
void imprimir(double x) { ... }

imprimir(5);        // Chama void imprimir(int)
imprimir("Olá");    // Chama void imprimir(String)
imprimir(3.14);     // Chama void imprimir(double)
```

**Python NÃO suporta sobrecarga dessa forma!**

Mas podemos SIMULAR usando parâmetros opcionais `*args` e `**kwargs`:

### Exemplo NO SEU CÓDIGO:

```python
# ═══════════════════════════════════════════════════════════
# SOBRECARGA - Mesmo método, DIFERENTES PARÂMETROS
# ═══════════════════════════════════════════════════════════

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    dataPublicacao = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)
    
    def descricao(self, incluir_edicao=False):
        """
        SOBRECARGA - Mesmo método, comportamentos DIFERENTES
        
        Sem parâmetro:      descricao()
        Com parâmetro:      descricao(True)
        """
        base = f"{self.titulo} ({self.dataPublicacao})"
        
        if incluir_edicao:
            return f"{base} - Edição {self.edicao}"
        
        return base


# ═══════════════════════════════════════════════════════════
# USANDO A SOBRECARGA
# ═══════════════════════════════════════════════════════════

livro = Livro.objects.get(id=1)

# Chamando SEM parâmetro:
print(livro.descricao())
# Output: "O Senhor dos Anéis (29/07/1954)"

# Chamando COM parâmetro:
print(livro.descricao(incluir_edicao=True))
# Output: "O Senhor dos Anéis (29/07/1954) - Edição 1"

# MESMO MÉTODO, COMPORTAMENTOS DIFERENTES!
# ISSO É POLIMORFISMO POR SOBRECARGA!
```

### Outro Exemplo - Com Múltiplos Parâmetros:

```python
class Livro(models.Model):
    def formatar_info(self, formato="curto"):
        """
        SOBRECARGA - Mesmo método, DIFERENTES FORMATOS
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


# ═══════════════════════════════════════════════════════════
# USANDO COM DIFERENTES PARÂMETROS
# ═══════════════════════════════════════════════════════════

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
# ISSO É POLIMORFISMO POR SOBRECARGA!
```

### Usando *args para Sobrecarga Real:

```python
class Calculadora:
    def somar(self, *numeros):
        """
        SOBRECARGA com *args
        Pode receber qualquer quantidade de argumentos
        """
        return sum(numeros)


calc = Calculadora()

# 2 números:
print(calc.somar(5, 3))  # 8

# 3 números:
print(calc.somar(5, 3, 2))  # 10

# 5 números:
print(calc.somar(1, 2, 3, 4, 5))  # 15

# MESMO MÉTODO, QUANTIDADES DIFERENTES DE PARÂMETROS!
```

---

## 3️⃣ SUBTIPO (Subtyping) - POLIMORFISMO POR HERANÇA

### O que é?
Uma SUBCLASSE pode ser usada **ONDE A SUPERCLASSE É ESPERADA**.

É o polimorfismo de substituição: você substitui o PAI pelo FILHO e funciona!

### Características:
- ✓ Baseado em HERANÇA
- ✓ Subclasse é um SUBTIPO da superclasse
- ✓ Pode substituir a superclasse em qualquer lugar
- ✓ O código que usa a superclasse trabalha com o subtipo

### Como Identificar:
```
class Pai:
    def metodo(self):
        pass

class Filho(Pai):  # ← Filho herda de Pai
    def metodo(self):
        pass

# Em qualquer lugar que aceitasse Pai, agora aceita Filho também!
```

### Exemplo NO SEU CÓDIGO:

```python
# ═══════════════════════════════════════════════════════════
# SUPERCLASSE
# ═══════════════════════════════════════════════════════════

class ModelViewSet(viewsets.ViewSetBase):
    """Classe genérica para ViewSets"""
    def list(self):
        pass
    def create(self):
        pass
    def retrieve(self):
        pass


# ═══════════════════════════════════════════════════════════
# SUBCLASSE - É UM SUBTIPO de ModelViewSet
# ═══════════════════════════════════════════════════════════

class LivroViewSet(viewsets.ModelViewSet):
    """LivroViewSet É UM ModelViewSet"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    # Herda os métodos: list(), create(), retrieve()
    # Pode sobrepor se quiser:
    # def retrieve(self):
    #     # Comportamento customizado


# ═══════════════════════════════════════════════════════════
# POLIMORFISMO DE SUBTIPO EM AÇÃO
# ═══════════════════════════════════════════════════════════

# Django escreve código assim:
def processar_viewset(viewset):
    """Função que aceita QUALQUER ModelViewSet"""
    
    # Como LivroViewSet É UM ModelViewSet,
    # pode ser usado aqui sem problemas!
    return viewset.list()


# Usando com LivroViewSet (que É UM ModelViewSet):
livro_viewset = LivroViewSet()
resultado = processar_viewset(livro_viewset)  # ✓ Funciona!


# Se criarmos outro ViewSet:
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# AutorViewSet também É UM ModelViewSet
autor_viewset = AutorViewSet()
resultado = processar_viewset(autor_viewset)  # ✓ Também funciona!


# ═══════════════════════════════════════════════════════════
# POR QUÊ SUBTIPO?
# ═══════════════════════════════════════════════════════════

# Django não precisa saber que é LivroViewSet ou AutorViewSet
# Ele sabe que ambos SÃO ModelViewSet
# Ambos SÃO subtipos de ModelViewSet
# Portanto, qualquer um funciona!
```

### Outro Exemplo - Com Serializers:

```python
# ═══════════════════════════════════════════════════════════
# SUPERCLASSE
# ═══════════════════════════════════════════════════════════

class Serializer:
    """Classe genérica para Serializers"""
    def serialize(self):
        pass
    def deserialize(self):
        pass


# ═══════════════════════════════════════════════════════════
# SUBCLASSES - São SUBTIPOS de Serializer
# ═══════════════════════════════════════════════════════════

class LivroSerializer(Serializer):
    """LivroSerializer É UM Serializer"""
    pass

class AutorSerializer(Serializer):
    """AutorSerializer É UM Serializer"""
    pass

class UsuarioSerializer(Serializer):
    """UsuarioSerializer É UM Serializer"""
    pass


# ═══════════════════════════════════════════════════════════
# CÓDIGO QUE ACEITA QUALQUER SUBTIPO
# ═══════════════════════════════════════════════════════════

def processar_dados(serializer):
    """Aceita QUALQUER Serializer"""
    # Como todos SÃO Serializers, todos funcionam aqui!
    return serializer.serialize()


# Todos funcionam porque SÃO SUBTIPOS de Serializer:
processar_dados(LivroSerializer())    # ✓ Funciona!
processar_dados(AutorSerializer())    # ✓ Funciona!
processar_dados(UsuarioSerializer())  # ✓ Funciona!
```

---

## 📊 COMPARAÇÃO DOS 3 TIPOS

| TIPO | O QUE É | BASEADO EM | EXEMPLO |
|------|---------|-----------|---------|
| **SOBREPOSIÇÃO** | Classe FILHA muda método da SUPERCLASSE | HERANÇA | `__str__()` em Livro vs Model |
| **SOBRECARGA** | Mesmo método com DIFERENTES PARÂMETROS | PARÂMETROS | `descricao()` vs `descricao(True)` |
| **SUBTIPO** | Subclasse pode substituir a superclasse | HERANÇA | LivroViewSet no lugar de ModelViewSet |

---

## 🎓 RESUMO

### 1️⃣ SOBREPOSIÇÃO
```python
class Livro(Model):
    def __str__(self):  # MESMO NOME
        return self.titulo  # COMPORTAMENTO DIFERENTE
```
**Uso:** Customizar comportamento herdado

---

### 2️⃣ SOBRECARGA
```python
class Livro(Model):
    def descricao(self, incluir_edicao=False):  # DIFERENTES PARÂMETROS
        # Comportamento muda conforme os parâmetros
```
**Uso:** Um método com múltiplas variações

---

### 3️⃣ SUBTIPO
```python
class LivroViewSet(ModelViewSet):  # LivroViewSet É UM ModelViewSet
    pass

# Pode ser usado onde ModelViewSet é esperado
```
**Uso:** Substituir superclasse por subclasse em qualquer contexto

---

## ✅ NO SEU CÓDIGO

✓ **SOBREPOSIÇÃO** - Em `models.py` com `__str__()`
✓ **SOBRECARGA** - Em `models.py` com `descricao()` e `formatar_info()`
✓ **SUBTIPO** - Em `views.py` com `LivroViewSet(ModelViewSet)`

**Seu código demonstra os 3 tipos de polimorfismo!** 🎉
