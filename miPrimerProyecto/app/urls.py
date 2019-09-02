from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sumar/<numero1>/<numero2>', views.sumar, name='sumar'),
    path('restar/<numero1>/<numero2>', views.restar, name='restar'),
    path('multiplicar/<numero1>/<numero2>', views.multiplicar, name='multiplicar'),
]
