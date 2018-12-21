from django.shortcuts import render
from random import randint

ultimo_numero = 0
n1 = 0
n2 = 0
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
    heroi = 'heroi'+str(randint(1,30))+'.png'
    viloes ='vilao'+str(randint(1,8))+'.png'

    if ultimo_numero == 0:
        ultimo_numero = 0
        n1, n2 = aleatorio()
        opc = str(n1)+operador+str(n2)
        ultimo_numero = eval(opc)
        print(ultimo_numero)
    else:
        resp = request.GET.get('resp')  
        if resp:
            ultimo_numero
            resp = int(resp)
            if resp == ultimo_numero:
                msg = acertou[randint(0,len(acertou)-1)]
                ultimo_numero = 0
            else:
                msg = errou[randint(0,len(errou)-1)]
                vilao = ultimo_numero
        else:
            msg = ""
            ultimo_numero = 0

    context = {'operador':operador,'n1':n1, 'n2':n2 ,'calc':ultimo_numero, 'msg':msg , 'vilao':vilao, 'viloes':viloes, 'heroi':heroi}
    return render(request, 'blog/calc.html', context)

def aleatorio():
    n1 = randint(0,20)
    n2 = randint(0,20)
    return n1, n2