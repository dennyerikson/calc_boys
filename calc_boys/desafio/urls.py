from django.urls import path
from .views import Desafio, Score


urlpatterns=[
    path('', Desafio, name='desafio'),
    path('score/', Score, name='score'),
]