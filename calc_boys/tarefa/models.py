from django.db import models
from matematica.models import Problema
from accounts.models import Aluno
from django.utils import timezone


# Create your models here.
class Tarefa(models.Model):
    materia = models.CharField(max_length=100)
    exercicio = models.ForeignKey(Problema, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    create_date = models.DateField(
        default=timezone.now
    )
    finish_date = models.DateField()
    hora_init = models.TimeField()
    hora_finish = models.TimeField()

    def __str__(self):
        return '%s - %s' % (self.materia, str(self.create_date))

