# Generated by Django 2.0.9 on 2019-06-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='alternativa',
            field=models.CharField(choices=[('a', 'alternativa: A'), ('b', 'alternativa: B'), ('c', 'alternativa: C'), ('d', 'alternativa: D'), ('e', 'alternativa: E')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]