from django.db import models
from accounts.models import Aluno
from django.utils import timezone
import os


# Create your models here.
class Score(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    pontos = models.CharField(max_length=10)
    acertos = models.CharField(max_length=10)
    erros = models.CharField(max_length=10)
    equacao = models.CharField(max_length=50)

    create_date = models.DateField(
        default=timezone.now
    )


    def __str__(self):
        return 'Nome: %s - pontos: %s' % (self.aluno, self.pontos)



def upload_path_handler(instance, filename):
    subpasta = 'herois' if str(instance.tipo) == 'heroi' else 'viloes'
    return "Personagem/%s/%s" % (instance.subpasta, filename)

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

    def path(self, filename):
        if self.tipo == 'heroi':
            path = 'pesronagem/herois/'
        else:
            path = 'pesronagem/viloes/'

        extension = os.path.splitext(filename)[-1]
        return '%s/new_name%s' % (path, extension,)

    foto = models.ImageField(upload_to=path)


    def __str__(self):
        return '%s - %s' % (self.tipo, self.nome)

        
  