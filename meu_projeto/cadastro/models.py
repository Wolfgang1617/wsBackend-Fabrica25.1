from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    aniversario = models.DateField()

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.CharField(max_length=4)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='filmes')

    def __str__(self):
        return self.titulo

# Create your models here.
