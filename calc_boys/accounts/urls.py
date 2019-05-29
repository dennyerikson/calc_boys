from django.urls import path
from . import views

from .views import (
    PessoaCreateView,
    PessoaListView,
    AlunoCreateView,
    AlunoListView,
)



app_name = 'accounts'

urlpatterns = [
    # path('', PessoaListView.as_view(), name='pessoa-list' ),
    # path('pessoacreate/', PessoaListView.as_view(), name='pessoa-create' ),
    
    # path('alunolist/', AlunoListView.as_view(), name='aluno-list' ),
    path('alunocreate', AlunoCreateView.as_view(), name='aluno-create' ),
]