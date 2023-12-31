# Generated by Django 4.2.2 on 2023-07-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consultas'], [1, 'reclamo'], [2, 'sugerencia']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
