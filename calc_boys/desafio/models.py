from django.db import models
from accounts.models import Aluno
from django.utils import timezone


def ALTERNATIVAS():
    return [
        ('a','alternativa: A'),
        ('b','alternativa: B'),
        ('c','alternativa: C'),
        ('d','alternativa: D'),
        ('e','alternativa: E')
    ]

class Resposta(models.Model):
    """ por enquanto recebe o nº do id até eu achar um meio melhor"""
    numero = models.IntegerField()
    alternativa = models.CharField(max_length=2, choices=ALTERNATIVAS())
    reposta = models.CharField(max_length=150)
    certa = models.BooleanField(default=False)

    def __str__(self):
        return '%s - alternativa:%s - resposta:%s' % (self.numero, self.alternativa, self.reposta)


class Questao(models.Model):
    pergunta = models.CharField(max_length=225)
    resposta = models.ManyToManyField(Resposta, related_name='resposta')

    def __str__(self):
        return '%s - id:%i' % (self.pergunta, self.pk)




class Desafio(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    questao = models.ManyToManyField(Questao, related_name='questao')
    nota = models.DecimalField(decimal_places=2, max_digits=7)
    nivel = models.IntegerField()
    create_date = models.DateField(
        default=timezone.now
    )
    answer_date = models.DateField()
    init_time = models.TimeField(
        auto_now=True
    )    
    final_time = models.TimeField()
    
    def __str__(self):
        return '%s' % (self.aluno)




class Des(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    questao = models.ManyToManyField(Questao, related_name='question')

    def __str__(self):
        return '%s' % (self.aluno)

