from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calc/<str:operador>/', views.calc, name='calc'),
    path('score/<int:id>/', views.score, name='score'),
]