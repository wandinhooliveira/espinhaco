# Generated by Django 2.0.13 on 2019-02-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190213_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
