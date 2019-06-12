from django import forms
from .models import Questao, Resposta, ALTERNATIVAS
from django.contrib.admin import widgets
from django.forms.widgets import RadioSelect, Select



class QuestaoForm(forms.Form):
    pergunta = forms.TextInput()
    
    ESCOLHA = forms.MultipleChoiceField(
        choices=((choice.alternativa, choice.alternativa+') '+choice.reposta)
            for choice in Resposta.objects.filter(numero=1)
        ),
        required = True,
        widget=forms.RadioSelect(
            # renderer=HorizontalRadioRenderer
            attrs={
                'class' : 'myfieldclass'
                # 'style': 'display: inline-block; margin-right: 10px; margin-left: 10px; float: left;'
            }
        ),        
    )