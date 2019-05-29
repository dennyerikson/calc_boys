from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Pessoa, Aluno
from .forms import PessoaModelForm, AlunoModelForm


class PessoaObjectMixin(object):
    model = Pessoa

    def get_object(self):
        id_ = self.kwargs.get('id')
        obj = None
        if id_ is not None:
            obj = get_object_or_404(Pessoa, id=id_)
        return obj



class PessoaCreateView(CreateView):
    template_name = 'accounts/pessoa_create.html'
    queryset = Pessoa.objects.all()
    form_class = PessoaModelForm

    def form_invalid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:pessoa-list')


class PessoaListView(ListView):
    template_name = 'accounts/pessoa_list.html'
    queryset=Pessoa.objects.all()




"""### Aluno Views ###"""
"""### Aaltera essa ideia assim que possivel ###"""

class AlunoObjectMixin(object):
    model = Aluno

    def get_object(self):
        id_ = self.kwargs.get('id')
        obj = None
        if id_ is not None:
            obj = get_object_or_404(Aluno, id=id_)
        return obj



class AlunoCreateView(CreateView):
    template_name = 'accounts/aluno_create.html'
    queryset = Aluno.objects.all()
    form_class = AlunoModelForm

    def form_invalid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:aluno-list')


class AlunoListView(ListView):
    template_name = 'accounts/aluno_list.html'
    queryset=Aluno.objects.all()

