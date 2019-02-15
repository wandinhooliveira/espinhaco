from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ultimas', views.ultimas, name='ultimas'),
    path('<slug:slug>/', views.noticia, name='noticia'),
]