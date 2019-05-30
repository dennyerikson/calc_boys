# Generated by Django 2.0.9 on 2019-05-30 01:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matematica', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('create_date', models.DateField(default=django.utils.timezone.now)),
                ('finish_date', models.DateField()),
                ('hora_init', models.TimeField()),
                ('hora_finish', models.TimeField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Aluno')),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matematica.Problema')),
            ],
        ),
    ]
