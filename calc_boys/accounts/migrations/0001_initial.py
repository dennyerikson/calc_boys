# Generated by Django 2.0.9 on 2019-05-28 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(max_length=30)),
                ('serie', models.CharField(max_length=30)),
                ('turma', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='Pessoa')),
                ('nome', models.CharField(max_length=150)),
                ('aniversario', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Pessoa'),
        ),
    ]
