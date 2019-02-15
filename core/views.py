from django.shortcuts import render, get_object_or_404
from .models import Noticia
import random

# Create your views here.
def index(request):

	noticias = Noticia.objects.all().order_by('-data')[:7]
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
