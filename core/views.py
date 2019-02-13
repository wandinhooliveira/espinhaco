from django.shortcuts import render
from .models import Noticia
import random

# Create your views here.
def index(request):

	noticias = Noticia.objects.all().order_by('data')[:9]
	capa = Noticia.objects.filter(prioridade=1).order_by('data')[:1]
	slide = Noticia.objects.filter(prioridade=1).order_by('data')[1:7]
	destaque1 = random.choice(noticias)
	destaque2 = random.choice(noticias)
	while destaque2 == destaque1:
		destaque2 = random.choice(noticias)

	return render(request, 'core/index.html', {'noticias': noticias,'capa': capa, 'slide': slide, 'destaque1': destaque1,'destaque2': destaque2 })