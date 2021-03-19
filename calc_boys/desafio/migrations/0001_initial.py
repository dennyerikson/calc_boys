# Generated by Django 2.0.9 on 2019-06-11 14:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_pessoa_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desafio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=7)),
                ('nivel', models.IntegerField()),
                ('create_date', models.DateField(default=django.utils.timezone.now)),
                ('answer_date', models.DateField()),
                ('init_time', models.TimeField(auto_now=True)),
                ('final_time', models.TimeField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('reposta', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='questao',
            name='resposta',
            field=models.ManyToManyField(related_name='resposta', to='desafio.Resposta'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='questao',
            field=models.ManyToManyField(related_name='questao', to='desafio.Questao'),
        ),
    ]