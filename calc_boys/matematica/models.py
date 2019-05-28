from django.db import models
from django.utils import timezone

# Create your models here.
class Problema(models.Model):
    enunciado = models.TextField(max_length=225)
    resposta = models.CharField(max_length=100)
    ponto = models.CharField(max_length=10)
    tempo = models.CharField(max_length=10)

    create_date = models.DateTimeField(
        default=timezone.now
    )

