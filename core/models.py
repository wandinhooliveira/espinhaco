from django.db import models
from django.utils import timezone

# Create your models here.
class Noticia(models.Model):
	autor = models.CharField(max_length=200, default='Zé Geraldo')
	titulo = models.CharField(max_length=300)
	slug = models.SlugField(max_length=100, blank=True)
	subtitulo = models.CharField(max_length=50, blank=True)
	categoria = models.CharField(max_length=30, default='Geral')
	foto = models.CharField(max_length=20, blank=True)
	texto = models.TextField()
	tags = models.CharField(max_length=200)
	data = models.DateTimeField(default=timezone.now)
	prioridade = models.IntegerField(default=3)

	def __str__(self):
		return self.titulo

	# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def artigo_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(artigo_pre_save, sender=Noticia)

