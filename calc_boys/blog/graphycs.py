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


# def curso_not_js(request):
#     curso = Post.objects.filter(curso__iendswith='- N')\
#     .values('curso')\
#     .annotate(value=Count('curso'))

#     lista = [
#         post_serializer(item)
#         for item in curso
#     ]
#     return JsonResponse({'cursos':lista})

# def confirm_sala_js(request):
#     sala = Post.objects.all()\
#         .values('sala')\
#         .annotate(confirm=Count('confirm', filter=Q(confirm=True)))

#     lista = [
#         # conf_serializerS(item)
#         conf_serializer(item)
#         for item in sala
#     ]
#     return JsonResponse({'salas': lista})

# def confirm_curM_js(request):
#     sala = Post.objects.filter(curso__iendswith='- M')\
#         .values('curso')\
#         .annotate(value=Count('confirm', filter=Q(confirm=True)))

#     lista = [
#         # conf_serializerS(item)
#         post_serializer(item)
#         for item in sala
#     ]
#     return JsonResponse({'cursos': lista})

# def confirm_curN_js(request):
#     sala = Post.objects.filter(curso__iendswith='- N')\
#         .values('curso')\
#         .annotate(value=Count('confirm', filter=Q(confirm=True)))

#     lista = [
#         # conf_serializerS(item)
#         post_serializer(item)
#         for item in sala
#     ]
#     return JsonResponse({'cursos': lista})

# def print_js(request):
#     lista = [
#         {'data':'VG-20/10/18', 'impresso':(600 * 8)},
#         {'data':'VG-24/11/18', 'impresso':(600 * 8)},
#         {'data':'VG-19/01/19', 'impresso':(350 * 8)},
#         ]
#     return JsonResponse({'print':lista})

# # serialização
# def post_serializer(item):
#     return {'curso':item['curso'], 'quantidade':item['value']}

# def conf_serializer(item):
#     return {'sala':'Sala '+item['sala'], 'confirmados':item['confirm']}

# """
# vg-20/10 inscritos 5166 confirmados: presentes:305
# vg-24/11 inscritos 6000 confirmados:600 presentes:415
# """
