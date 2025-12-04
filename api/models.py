from django.db import models

# ================================
# ARQUIVO: models.py
# ================================
# Este arquivo define como os dados (Livros) serão estruturados e armazenados.


class Livro(models.Model):
    """
    ╔════════════════════════════════════════════════════════════════════════════════════════╗
    ║                        CONCEITOS DE POO PRESENTES                      ║
    ╚════════════════════════════════════════════════════════════════════════════════════════╝
    """
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 1. CLASSE
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # "Livro" é uma CLASSE.
    # Uma classe é um MOLDE ou BLUEPRINT para criar objetos.
    # Pense em uma classe como um molde de bolo:
    #   - O molde (classe) define o formato
    #   - O bolo pronto (objeto/instância) é feito a partir do molde
    # Aqui definimos que todo Livro terá: título, dataPublicação e edição
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 2. HERANÇA & SUPERCLASSE
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # Livro HERDA de models.Model
    #
    # O que significa herança?
    # - models.Model é a SUPERCLASSE (ou classe PAI/BASE)
    # - Livro é a SUBCLASSE (ou classe FILHA)
    #
    # Herança = Livro recebe TODOS os poderes de models.Model
    # O Django criou models.Model com funcionalidades para:
    #   - Conectar ao banco de dados
    #   - Salvar dados
    #   - Buscar dados
    #   - Deletar dados
    #
    # Livro HERDA tudo isso automaticamente, sem precisar reescrever!
    # 
    # Exemplo real:
    # - Model (superclasse) é como uma planta genérica de uma casa
    # - Livro (subclasse) é uma casa específica que segue essa planta
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 3. ATRIBUTOS
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # Atributos são CARACTERÍSTICAS ou DADOS de uma classe.
    # Cada livro tem essas características:
    
    # ABSTRAÇÃO: Não nos preocupamos com SQL interno.
    # CharField é uma ABSTRAÇÃO que esconde a complexidade do banco.
    # Simplesmente dizemos "um livro tem um título" e o Django cuida do resto.
    titulo = models.CharField(max_length=255)           # Texto até 255 caracteres
    dataPublicacao = models.CharField(max_length=50)    # Texto até 50 caracteres
    edicao = models.CharField(max_length=50)            # Texto até 50 caracteres
    
    # ENCAPSULAMENTO: Esses atributos ficam "dentro" da classe.
    # Você não acessa diretamente o banco de dados.
    # Você trabalha com o objeto Livro e deixa o Django gerenciar.
    # Isso PROTEGE os dados e garante consistência.
    # 
    # COESÃO (Alta Coesão):
    # A classe Livro só cuida de dados de LIVRO.
    # Não mistura dados de Livro com dados de Usuário ou Autor.
    # Isso facilita manutenção e entendimento do código.
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 4. MÉTODO - Sobreposição (POLIMORFISMO POR OVERRIDING)
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # Um MÉTODO é uma ação que um objeto pode fazer.
    # Métodos são funções DENTRO da classe.
    
    def __str__(self):
        """
        Este é um MÉTODO ESPECIAL chamado __str__ (dunder-str).
        
        ═══════════════════════════════════════════════════════════════════════════════════════
        1. SOBREPOSIÇÃO = POLIMORFISMO POR OVERRIDING (Override Method)
        ═══════════════════════════════════════════════════════════════════════════════════════
        
        A classe PAI (models.Model) já tinha um método __str__ que retornava
        algo genérico como: "<Livro object (1)>"
        
        Nós SOBRESCREVEMOS (override) esse método para fazer algo DIFERENTE:
        Agora retorna o título do livro de forma legível.
        
        COMO IDENTIFICAR SOBREPOSIÇÃO?
        ✓ Mesmo nome do método na classe PAI e na classe FILHA: __str__ em ambas
        ✓ Comportamento DIFERENTE: pai retorna genérico, filho retorna específico
        ✓ A classe FILHA substitui completamente o comportamento do PAI
        
        EXEMPLO:
        - Classe PAI (Model): __str__() → "<Livro object (1)>"
        - Classe FILHA (Livro): __str__() → "O Senhor dos Anéis"
        
        ISSO É POLIMORFISMO POR SOBREPOSIÇÃO!
        """
        return self.titulo
    
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 2. SOBRECARGA = POLIMORFISMO POR SOBRECARGA (Overload Method)
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # Sobrecarga = mesmo nome de método com DIFERENTES PARÂMETROS
    # 
    # NOTA: Python NÃO suporta sobrecarga tradicional (como Java/C++)
    # Mas podemos simular com *args e **kwargs!
    
    def descricao(self, incluir_edicao=False):
        """
        SOBRECARGA = mesmo método, COMPORTAMENTOS DIFERENTES baseado em PARÂMETROS
        
        COMO IDENTIFICAR SOBRECARGA?
        ✓ Mesmo nome do método: descricao()
        ✓ DIFERENTES PARÂMETROS: com/sem incluir_edicao
        ✓ COMPORTAMENTOS DIFERENTES: retorna coisas diferentes dependendo dos parâmetros
        
        EXEMPLO DE USO:
        livro = Livro.objects.get(id=1)
        
        livro.descricao()  # Sem parâmetro
        # Retorna: "O Senhor dos Anéis (29/07/1954)"
        
        livro.descricao(incluir_edicao=True)  # Com parâmetro
        # Retorna: "O Senhor dos Anéis (29/07/1954) - Edição 1"
        
        ISSO É POLIMORFISMO POR SOBRECARGA!
        (simulada no Python com parâmetros opcionais)
        """
        base = f"{self.titulo} ({self.dataPublicacao})"
        
        if incluir_edicao:
            return f"{base} - Edição {self.edicao}"
        
        return base
    
    
    def formatar_info(self, formato="curto"):
        """
        OUTRO EXEMPLO DE SOBRECARGA
        
        Mesmo método, DIFERENTES FORMATOS baseado no parâmetro 'formato'
        
        EXEMPLO DE USO:
        livro = Livro.objects.get(id=1)
        
        livro.formatar_info()  # Padrão: curto
        # Retorna: "Livro: O Senhor dos Anéis"
        
        livro.formatar_info(formato="longo")
        # Retorna: "Livro: O Senhor dos Anéis | Data: 29/07/1954 | Edição: 1"
        
        livro.formatar_info(formato="json")
        # Retorna: JSON com todos os dados
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
        
        else:
            return f"Livro: {self.titulo}"
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # RESUMO DO QUE TEMOS AQUI:
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # ✓ CLASSE: Livro (é um molde/blueprint)
    # ✓ HERANÇA: Livro herda de models.Model
    # ✓ SUPERCLASSE: models.Model (pai que dá poderes)
    # ✓ SUBCLASSE: Livro (filho que especializa)
    # ✓ ATRIBUTOS: titulo, dataPublicacao, edicao (dados do livro)
    # ✓ MÉTODOS: __str__ (ação que o livro pode fazer)
    # ✓ ENCAPSULAMENTO: Dados protegidos dentro da classe
    # ✓ ABSTRAÇÃO: CharField abstrai complexidade do banco
    # ✓ COESÃO ALTA: Só cuida de dados de livro
    # ✓ POLIMORFISMO: __str__ se comporta diferente em diferentes classes
