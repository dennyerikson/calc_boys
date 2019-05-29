from django import forms
from .models import Pessoa, Aluno
from django.contrib.admin import widgets


class PessoaModelForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'foto', 'nome', 'aniversario',
        ]

        widgets={
            'nome':forms.TextInput(attrs={
                'placeholder':'Nome completo'
            })
        }



class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'pessoa', 'sala', 'serie', 'turma'
        ]

        widgets={
            'sala':forms.TextInput(attrs={
                'placeholder':'Nº da sala'
            })
        }