from django.db import models

# Create your models here.
class Pessoa(models.Model):
    foto = models.ImageField(upload_to='Pessoa')
    nome = models.CharField(max_length=150)
    aniversario = models.DateField()

    def __str__(self):
        return self.nome



class Aluno(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    sala = models.CharField(max_length=30)
    serie = models.CharField(max_length=30)
    turma = models.CharField(max_length=30)

    def __str__(self):
        return self.pessoa.nome


    """ mais pra frente criar signals para add user"""