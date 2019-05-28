from django.db import models

# Create your models here.
class Score(models.Model):
    pontos = models.CharField(max_length=10)
    acertos = models.CharField(max_length=10)
    erros = models.CharField(max_length=10)
    equacao = models.CharField(max_length=50)
