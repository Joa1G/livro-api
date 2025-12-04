from django.db import models

# [POO - Abstração & Modularidade]
# O módulo 'models' abstrai a complexidade do banco de dados.
# Não precisamos escrever SQL puro; lidamos com objetos Python.

# [POO - Herança & SuperClasse]
# A classe 'Livro' herda de 'models.Model'.
# 'models.Model' é a SuperClasse (ou Classe Base) que fornece toda a funcionalidade de ORM.
# 'Livro' é a SubClasse (ou Classe Filha) que especializa o comportamento.
class Livro(models.Model):
    # [POO - Encapsulamento & Atributos]
    # Estes são atributos de classe que definem a estrutura dos dados.
    # O Django usa 'Descritores' (um padrão avançado) para gerenciar o acesso a esses campos,
    # garantindo Proteção de Dados e validação (Acesso Controlado).
    
    # [POO - Coesão]
    # A classe tem Alta Coesão pois trata apenas dos dados do Livro.
    titulo = models.CharField(max_length=255)
    dataPublicacao = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)

    # [POO - Polimorfismo por Sobreposição (Overriding)]
    # Estamos sobrescrevendo o método '__str__' da classe base (object/Model).
    # Isso altera o comportamento padrão de como o objeto é representado como string.
    def __str__(self):
        return self.titulo
