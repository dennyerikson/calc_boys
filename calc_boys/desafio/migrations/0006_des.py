# Generated by Django 2.0.9 on 2019-06-12 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_pessoa_user'),
        ('desafio', '0005_desafio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Des',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Aluno')),
            ],
        ),
    ]
