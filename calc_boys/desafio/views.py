from django.shortcuts import render
from .forms import QuestaoForm
from .models import Desafio, Resposta, Des


# Create your views here.
def Desafio(request):
    context={}

    context['desafio'] = Des.objects.filter(aluno_id=1)


    # context['questoes'] = context['desafio'].questao.all()[0]
    # context['opc_radios'] = context['questoes'].resposta.all()
    # HTTP GET variables
    opc_radio = request.GET.copy()

    if opc_radio:
        for d in context['desafio']:
            for q in d.questao.all():
                for r in q.resposta.all(): # testar if com IN 
                    if r.certa:
                        if opc_radio[str('radio'+str(r.numero))] == str(r.alternativa):
                            print('Acertou')
                        else:
                            print('errou')

                        """ criar redirect e migrar para teste """

    return render(request, 'desafio/desafio.html', context)




def Score(request):
    context={}

    return render(request, 'desafio/desafio_score.html', context)
