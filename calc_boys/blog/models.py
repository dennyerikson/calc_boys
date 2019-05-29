from django.db import models

# Create your models here.
class Score(models.Model):
    pontos = models.CharField(max_length=10)
    acertos = models.CharField(max_length=10)
    erros = models.CharField(max_length=10)
    equacao = models.CharField(max_length=50)


class Personagem(models.Model):
    def TIPO():
        T = [
            ('heroi','Super-Herói'),
            ('vilao','Super-Vilão'),
        ]
        return T

    tipo = models.CharField(max_length=20, choices=TIPO())
    nome = models.CharField(max_length=100)
    fala = models.TextField(max_length=120)
    foto = models.ImageField(upload_to='personagem')

