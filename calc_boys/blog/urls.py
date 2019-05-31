from django.urls import path
from . import views
from .graphycs import *



urlpatterns = [
    path('', views.home, name='home'),
    path('calc/<str:operador>/', views.calc, name='calc'),
    path('score/<int:id>/', views.score, name='score'),
    path('score_graphs/', views.score_graphs, name='score_graphs'),

    path('score_json/', score_json),
]