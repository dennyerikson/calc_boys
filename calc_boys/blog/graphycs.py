from django.db.models import Count, Q, Sum
from django.http import JsonResponse
from .models import *
import json
from django.utils import timezone


def score_json(request):
    # score = Score.objects.filter(aluno__pessoa__user=request.user.id)\
    # .values('aluno')\
    # .annotate(value=Sum('pontos'))\
    # .annotate(acertos=Sum('acertos'))


    score = Score.objects.filter(aluno__pessoa__user=request.user.id)\
    .values('create_date')\
    .annotate(value=Sum('pontos'))\
    .annotate(acertos=Sum('acertos'))\
    .annotate(erros=Sum('erros'))\

    lista = [
        score_serializer(item)
        for item in score
    ]

    return JsonResponse({'aluno':lista})

# serialização
def score_serializer(item):
    # score = Score.objects.filter(aluno=int(item['aluno']))
    
    # print('score_serializer',item['aluno'], item['pontos'])
    # return {'nome':score[0].aluno.pessoa.user.first_name,
    return {'data':item['create_date'],
        'quantidade':item['value'],
        'acertos':item['acertos'],
        'erros':item['erros']
        }

