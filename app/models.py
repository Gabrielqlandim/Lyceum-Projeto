from django.db import models

class SerieTurma(models.Model):
    id = models.AutoField(primary_key=True)
    nome_turma = models.CharField(max_length=120, null=False)

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, null=False)
    serie_turma = models.ForeignKey(SerieTurma, on_delete=models.CASCADE)
    data_matricula = models.DateField()

class Materia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    nome_materia = models.CharField(max_length=120, null=False)
    faltas = models.IntegerField(default=0)
    notas = models.DecimalField(max_digits=5, decimal_places=2)
    