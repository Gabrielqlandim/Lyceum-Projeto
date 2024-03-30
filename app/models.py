from django.db import models

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, null=False)
    serie_turma = models.CharField(max_length=8, null=False)
    data_matricula = models.DateField()