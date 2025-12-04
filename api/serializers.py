from rest_framework import serializers
from .models import Livro

# ================================
# ARQUIVO: serializers.py
# ================================
# Este arquivo converte dados entre Python e JSON.
# Quando você envia dados pela API, eles vêm em JSON.
# Quando salva no banco, precisa ser um objeto Python.
# O Serializer faz essa TRADUÇÃO.


class LivroSerializer(serializers.ModelSerializer):
    """
    ╔════════════════════════════════════════════════════════════════════════════════════════╗
    ║                        CONCEITOS DE POO PRESENTES                      ║
    ╚════════════════════════════════════════════════════════════════════════════════════════╝
    """
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 1. CLASSE
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # "LivroSerializer" é uma CLASSE.
    # É um molde/blueprint para converter dados de Livro.
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 2. HERANÇA & SUPERCLASSE
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # LivroSerializer HERDA de serializers.ModelSerializer
    #
    # - ModelSerializer é a SUPERCLASSE (classe PAI)
    # - LivroSerializer é a SUBCLASSE (classe FILHA)
    #
    # ModelSerializer já vem com métodos prontos para:
    #   - Converter objeto Python para JSON (serialize)
    #   - Converter JSON para objeto Python (deserialize)
    #   - Validar dados
    #
    # LivroSerializer REUTILIZA tudo isso!
    # Não precisa reescrever a lógica de conversão.
    #
    # PRINCÍPIO: DRY (Don't Repeat Yourself)
    # Reutilizamos código da superclasse em vez de reescrever.
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 3. CLASSE INTERNA (Meta)
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # "Meta" é uma classe DENTRO de outra classe.
    # É uma forma de ENCAPSULAR configurações.
    #
    # ENCAPSULAMENTO: A configuração fica organizadinha dentro de Meta.
    # Separa CONFIGURAÇÃO de LÓGICA.
    # Padrão de design usado pelo Django.
    
    class Meta:
        """
        Aqui dizemos qual modelo usar e quais campos incluir na conversão.
        """
        
        # ACOPLAMENTO:
        # Aqui temos um ACOPLAMENTO NECESSÁRIO.
        #
        # ACOPLAMENTO = Dependência entre classes.
        # Duas fortes: classe A depende muito de classe B
        # Duas fracas: classe A pouco depende de classe B
        #
        # Aqui temos acoplamento NECESSÁRIO porque:
        # - LivroSerializer PRECISA saber qual modelo está traduzindo
        # - Sem saber qual é o modelo, não consegue converter
        #
        # Isso é BOM! Nem sempre acoplamento é ruim.
        # O importante é MINIMIZAR acoplamento desnecessário.
        
        # Diz: "Use a classe Livro como referência"
        model = Livro
        
        # Diz: "Inclua TODOS os campos da classe Livro"
        # '__all__' significa "tudo"
        fields = '__all__'
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # 4. SOLID: Single Responsibility Principle (SRP)
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # RESPONSABILIDADE ÚNICA = A classe faz UMA coisa bem feita.
    #
    # LivroSerializer tem UMA responsabilidade:
    # "Converter Livro ↔ JSON"
    #
    # O que ela NÃO faz:
    # - Não salva no banco (responsabilidade do Model)
    # - Não trata requisições HTTP (responsabilidade da View)
    # - Não cria URLs (responsabilidade do URLs)
    #
    # Isso facilita manutenção:
    # - Se quebrar conversão JSON → culpa do Serializer
    # - Se quebrar salvamento no banco → culpa do Model
    # - Se quebrar rota HTTP → culpa da View
    #
    # Cada classe cuida de uma coisa, fica fácil debugar!
    
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # RESUMO DO QUE TEMOS AQUI:
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # ✓ CLASSE: LivroSerializer (molde para conversão)
    # ✓ HERANÇA: Herda de ModelSerializer
    # ✓ SUPERCLASSE: serializers.ModelSerializer
    # ✓ SUBCLASSE: LivroSerializer
    # ✓ ENCAPSULAMENTO: Configuração encapsulada em Meta
    # ✓ ACOPLAMENTO NECESSÁRIO: Depende de Livro
    # ✓ SOLID - SRP: Responsabilidade única (converter)
    # ✓ REUTILIZAÇÃO: Não reescreve lógica do pai
