from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ultimas', views.ultimas, name='ultimas'),
    path('<slug:slug>/', views.noticia, name='noticia'),
    path('contato', views.contato, name='contato'),
    path('galeria', views.galeria, name='galeria'),
    path('geral', views.geral, name='geral'),
    path('politica', views.politica, name='politica'),
    path('policia', views.policia, name='policia'),
    path('entretenimento', views.entretenimento, name='entretenimento'),
]