from django.shortcuts import render, redirect
from random import randint
from blog.models import Score



ultimo_numero = 0
n1 = 0
n2 = 0
lista_herois=[]
pontos = 0
acertos =0
erros=0

# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {})

#Somar
def calc(request, operador):   
    acertou = ['Muito bem super prodigio!','Parabéns! Precisamos de alguém assim', 'Bom trabalho boy','Você é 10 vezes mais inteligente que o Hulk']
    errou = ['Haha! tente novamente','Achou que ia me derroar facil', 'Fique mais forte para me enfrentar','É só isso, me mostre seu poder']
    global ultimo_numero
    global n1
    global n2
    msg = ""
    vilao = ''
    global lista_herois
    global pontos
    global acertos
    global erros
    

    heroi = 'heroi'+str(nao_repetir(randint(1,30), lista_herois))+'.png'    
    viloes ='vilao'+str(randint(1,8))+'.png'
    
    if pontos < 30:

        if ultimo_numero == 0:
            ultimo_numero = 0
            n1, n2 = aleatorio(operador)
            opc = str(n1)+operador+str(n2)
            ultimo_numero = eval(opc)
        else:
            resp = request.GET.get('resp')  
            if resp:
                ultimo_numero
                resp = int(resp)
                if resp == ultimo_numero:
                    msg = acertou[randint(0,len(acertou)-1)]
                    lista_herois.append(heroi)
                    pontos += 10
                    acertos += 1
                    ultimo_numero = 0
                else:
                    msg = errou[randint(0,len(errou)-1)]
                    pontos -= 5
                    erros += 1
                    vilao = ultimo_numero
            else:
                msg = ""
                ultimo_numero = 0
    else:
        if pontos > 0:
            score = Score.objects.create(
                pontos = pontos,
                acertos = acertos,
                erros = erros,
                equacao = operador
            )
        score.save()

        ultimo_numero = 0
        pontos = 0
        erros = 0
        acertos = 0

        print('id score ',score.id)
        return redirect('/score/%i' % (score.id))

    context = {
        'operador':operador,'n1':n1, 'n2':n2 ,'calc':ultimo_numero,
        'msg':msg , 'vilao':vilao, 'viloes':viloes, 'heroi':heroi,
        'pontos':pontos}
    return render(request, 'blog/calc.html', context)

def aleatorio(operador):
    n1 = randint(10,20) if operador=='-' or operador=='/' else randint(0,20)
    n2 = randint(0,10) if operador=='-' or operador=='/' else randint(0,20)
    return n1, n2

def nao_repetir(numero, lista):
    if numero in lista:
        numero = randint(1,30)
        print('lista_h',len( lista_herois))
    
    return numero
    

def score(request, id):
    context={}

    score = Score.objects.get(id=id)
    
    context['pontos']=score.pontos
    context['acertos']=score.acertos
    context['erros']=score.erros
    context['equacao']=score.equacao

    return render(request, 'blog/score.html', context)





