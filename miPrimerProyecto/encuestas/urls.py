from django.urls import path

from . import views

urlpatterns = [
    path('' , views.index, name='index'),
    path('<int:pregunta_id>/', views.detalle, name='detalle'),
    path('<int:pregunta_id>/resultados/', views.resultados, name='resultados'),
    path('<int:pregunta_id>/vote/', views.votar, name='vote'),
    path('sumar/<pregunta_id>/<numero>', views.sumar, name='sumar'),
    path('restar/<pregunta_id>/<numero>', views.restar, name='restar'),
    path('multiplicar/<pregunta_id>/<numero>', views.multiplicar, name='multiplicar'),
]
