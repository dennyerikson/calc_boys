# Generated by Django 2.0.9 on 2019-06-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0002_resposta_alternativa'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='certa',
            field=models.BooleanField(default=False),
        ),
    ]
