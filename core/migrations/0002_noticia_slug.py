# Generated by Django 2.0.13 on 2019-02-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
