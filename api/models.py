from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    dataPublicacao = models.CharField(max_length=50)  # Using CharField as requested
    edicao = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
