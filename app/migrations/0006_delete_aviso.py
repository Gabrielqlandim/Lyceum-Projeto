# Generated by Django 5.0.4 on 2024-05-22 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_aluno_materias_remove_materia_nome_aluno_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Aviso',
        ),
    ]
