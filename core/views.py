from django.shortcuts import render, get_object_or_404
from .models import Noticia
import random

# Create your views here.
def index(request):

	noticias = Noticia.objects.all().order_by('-data')[:6]
	capa = Noticia.objects.filter(prioridade=1).order_by('-data')[:1]
	slide = Noticia.objects.filter(prioridade=1).order_by('-data')[1:7]
	destaque1 = random.choice(slide)
	destaque2 = random.choice(slide)
	while destaque2 == destaque1:
		destaque2 = random.choice(noticias)

	return render(request, 'core/index.html', {'noticias': noticias,'capa': capa, 'slide': slide, 'destaque1': destaque1,'destaque2': destaque2 })

def noticia(request, slug):

	noticia = get_object_or_404(Noticia, slug=slug)
	return render(request, 'core/noticia.html',{'noticia': noticia})

def ultimas(request):

	noticias = Noticia.objects.all().order_by('-data')
	return render(request, 'core/ultimas.html',{'noticias': noticias})

def contato(request):
	return render(request, 'core/contato.html',{})

def galeria(request):
	noticias = Noticia.objects.all().order_by('-data')
	return render(request, 'core/galeria.html',{'noticias': noticias})

def geral(request):
	noticias = Noticia.objects.filter(categoria='Geral').order_by('-data')
	return render(request, 'core/ultimas.html', {'noticias': noticias})

def politica(request):
	noticias = Noticia.objects.filter(categoria='Política').order_by('-data')
	return render(request, 'core/ultimas.html', {'noticias': noticias})

def policia(request):
	noticias = Noticia.objects.filter(categoria='Polícia').order_by('-data')
	return render(request, 'core/ultimas.html', {'noticias': noticias})

def entretenimento(request):
	noticias = Noticia.objects.filter(categoria='Entretenimento').order_by('-data')
	return render(request, 'core/ultimas.html', {'noticias': noticias})